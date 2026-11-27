from datetime import date
from models.buku import Buku
from models.anggota import Anggota
from models.peminjaman import Peminjaman
from aturan.aturan_peminjaman import HasilPeriksa

class HasilProses:
    def __init__(self, berhasil, pesan, data=None):
        self.berhasil, self.pesan, self.data = berhasil, pesan, data

class LayananPerpustakaan:
    def __init__(self, repo_buku, repo_anggota, repo_transaksi,
                 daftar_aturan, hari_ini=date.today):
        self._repo_buku = repo_buku
        self._repo_anggota = repo_anggota
        self._repo_transaksi = repo_transaksi
        self._daftar_aturan = list(daftar_aturan)
        self._hari_ini = hari_ini

    def tambah_buku(self, isbn, judul, penulis):
        try:
            buku = Buku(isbn, judul, penulis)
            if self._repo_buku.cari_isbn(buku.isbn):
                return HasilProses(False, f"ISBN {buku.isbn} sudah terdaftar")
            self._repo_buku.simpan(buku)
            return HasilProses(True, f"Buku '{buku.judul}' berhasil ditambahkan", buku)
        except (ValueError, AttributeError) as e:
            return HasilProses(False, str(e))

    def tambah_anggota(self, id_anggota, nama, kontak=""):
        try:
            anggota = Anggota(id_anggota, nama, kontak)
            if self._repo_anggota.cari_id(anggota.id_anggota):
                return HasilProses(False, f"ID anggota {anggota.id_anggota} sudah terdaftar")
            self._repo_anggota.simpan(anggota)
            return HasilProses(True, f"Anggota '{anggota.nama}' berhasil ditambahkan", anggota)
        except (ValueError, AttributeError) as e:
            return HasilProses(False, str(e))

    def cari_buku(self, kata_kunci):
        k = (kata_kunci or "").lower()
        return [b for b in self._repo_buku.semua()
                if k in b.isbn.lower() or k in b.judul.lower() or k in b.penulis.lower()]

    def daftar_buku(self): return self._repo_buku.semua()
    def daftar_anggota(self): return self._repo_anggota.semua()

    def cek_ketersediaan(self, isbn):
        buku = self._repo_buku.cari_isbn(isbn)
        if buku is None: return HasilProses(False, "Buku tidak ditemukan")
        return HasilProses(True, f"{buku.judul}: {buku.status}", buku)

    def _jumlah_pinjaman_aktif(self, anggota):
        if anggota is None: return 0
        return sum(1 for t in self._repo_transaksi.semua()
                   if t.anggota.id_anggota == anggota.id_anggota and t.status == Peminjaman.AKTIF)

    def _id_berikutnya(self):
        nomor = len(self._repo_transaksi.semua()) + 1
        while self._repo_transaksi.cari_id(f"T{nomor:03d}") is not None: nomor += 1
        return f"T{nomor:03d}"

    def catat_peminjaman(self, id_anggota, isbn):
        anggota = self._repo_anggota.cari_id(id_anggota or "")
        buku = self._repo_buku.cari_isbn(isbn or "")
        aktif = self._jumlah_pinjaman_aktif(anggota)
        for aturan in self._daftar_aturan:
            hasil = aturan.periksa(anggota, buku, aktif)
            if not isinstance(hasil, HasilPeriksa):
                raise TypeError("Aturan peminjaman harus mengembalikan HasilPeriksa")
            if not hasil.lolos:
                return HasilProses(False, f"Peminjaman ditolak: {hasil.pesan}")
        transaksi = Peminjaman(self._id_berikutnya(), buku, anggota, self._hari_ini())
        transaksi.proses_peminjaman()
        self._repo_transaksi.simpan(transaksi)
        return HasilProses(True, f"Peminjaman berhasil dicatat ({transaksi.id_transaksi})", transaksi)

    def kembalikan_buku(self, id_transaksi):
        transaksi = self._repo_transaksi.cari_id(id_transaksi or "")
        if transaksi is None: return HasilProses(False, "ID transaksi tidak ditemukan")
        if transaksi.status != Peminjaman.AKTIF:
            return HasilProses(False, "Transaksi sudah selesai")
        transaksi.proses_pengembalian(self._hari_ini())
        return HasilProses(True, f"Pengembalian '{transaksi.buku.judul}' berhasil; buku kembali tersedia", transaksi)

    def riwayat_transaksi(self):
        return self._repo_transaksi.semua()

    def riwayat_anggota(self, id_anggota):
        anggota = self._repo_anggota.cari_id(id_anggota or "")
        if anggota is None: return []
        return [t for t in self._repo_transaksi.semua()
                if t.anggota.id_anggota == anggota.id_anggota]
