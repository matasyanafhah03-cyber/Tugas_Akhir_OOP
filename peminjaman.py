from datetime import date

class Peminjaman:
    AKTIF = "aktif"
    SELESAI = "selesai"

    def __init__(self, id_transaksi: str, buku, anggota, tanggal_pinjam=None):
        self._id_transaksi = id_transaksi.strip().upper()
        self._buku = buku
        self._anggota = anggota
        self._tanggal_pinjam = tanggal_pinjam or date.today()
        self._tanggal_kembali = None
        self._status = self.AKTIF

    @property
    def id_transaksi(self): return self._id_transaksi
    @property
    def buku(self): return self._buku
    @property
    def anggota(self): return self._anggota
    @property
    def tanggal_pinjam(self): return self._tanggal_pinjam
    @property
    def tanggal_kembali(self): return self._tanggal_kembali
    @property
    def status(self): return self._status

    def proses_peminjaman(self):
        self._buku.tandai_dipinjam()

    def proses_pengembalian(self, tanggal_kembali=None):
        if self._status != self.AKTIF:
            raise ValueError("Transaksi sudah selesai")
        self._buku.tandai_tersedia()
        self._tanggal_kembali = tanggal_kembali or date.today()
        self._status = self.SELESAI
