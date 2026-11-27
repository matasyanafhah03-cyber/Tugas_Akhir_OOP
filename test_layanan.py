import unittest
from datetime import date
from main import buat_layanan
from aturan.aturan_peminjaman import AturanPeminjaman, HasilPeriksa, aturan_bawaan
from services.layanan_perpustakaan import LayananPerpustakaan
from repositories.memori import MemoriRepositoriBuku, MemoriRepositoriAnggota, MemoriRepositoriTransaksi

class TestLayanan(unittest.TestCase):
    def setUp(self):
        self.l=buat_layanan()
        self.l.tambah_buku("978-1","Python","Andi")
        self.l.tambah_buku("978-2","OOP","Budi")
        self.l.tambah_anggota("A001","Mata","0812")

    def test_tambah_dan_cari_buku(self):
        self.assertEqual(len(self.l.cari_buku("python")),1)

    def test_isbn_kosong_ditolak(self):
        self.assertFalse(self.l.tambah_buku(" ","Kosong","X").berhasil)

    def test_isbn_ganda_ditolak(self):
        self.assertFalse(self.l.tambah_buku("978-1","Duplikat","X").berhasil)

    def test_peminjaman_valid(self):
        self.assertTrue(self.l.catat_peminjaman("a001","978-1").berhasil)

    def test_anggota_tidak_terdaftar_ditolak(self):
        self.assertFalse(self.l.catat_peminjaman("A999","978-1").berhasil)

    def test_buku_sedang_dipinjam_ditolak(self):
        self.l.catat_peminjaman("A001","978-1")
        self.assertFalse(self.l.catat_peminjaman("A001","978-1").berhasil)

    def test_batas_pinjam_tiga(self):
        for isbn in ["978-1","978-2"]:
            self.l.catat_peminjaman("A001",isbn)
        self.l.tambah_buku("978-3","Buku 3","X")
        self.l.tambah_buku("978-4","Buku 4","X")
        self.l.catat_peminjaman("A001","978-3")
        self.assertFalse(self.l.catat_peminjaman("A001","978-4").berhasil)

    def test_pengembalian_dan_riwayat(self):
        h=self.l.catat_peminjaman("A001","978-1")
        self.assertTrue(self.l.kembalikan_buku(h.data.id_transaksi).berhasil)
        self.assertEqual(self.l.riwayat_transaksi()[0].status,"selesai")

    def test_id_transaksi_salah(self):
        self.assertFalse(self.l.kembalikan_buku("T099").berhasil)

    def test_tambah_aturan_tanpa_ubah_layanan(self):
        class AturanTutup(AturanPeminjaman):
            def periksa(self, anggota, buku, jumlah_pinjaman_aktif):
                return HasilPeriksa.gagal("Perpustakaan tutup")
        layanan=LayananPerpustakaan(MemoriRepositoriBuku(),MemoriRepositoriAnggota(),
            MemoriRepositoriTransaksi(),[AturanTutup()])
        layanan.tambah_buku("1","Judul","Penulis")
        layanan.tambah_anggota("A1","Nama","")
        self.assertIn("Perpustakaan tutup",layanan.catat_peminjaman("A1","1").pesan)

    def test_aturan_rusak_melanggar_kontrak(self):
        class AturanRusak(AturanPeminjaman):
            def periksa(self, anggota, buku, jumlah_pinjaman_aktif): return True
        layanan=LayananPerpustakaan(MemoriRepositoriBuku(),MemoriRepositoriAnggota(),
            MemoriRepositoriTransaksi(),[AturanRusak()])
        layanan.tambah_buku("1","Judul","Penulis")
        layanan.tambah_anggota("A1","Nama","")
        with self.assertRaises(TypeError): layanan.catat_peminjaman("A1","1")

    def test_repositori_fake_dan_tanggal_injeksi(self):
        class RepoFake(MemoriRepositoriBuku):
            def __init__(self): super().__init__(); self.dicatat=[]
            def simpan(self,buku): self.dicatat.append(buku.isbn); super().simpan(buku)
        rb=RepoFake()
        layanan=LayananPerpustakaan(rb,MemoriRepositoriAnggota(),MemoriRepositoriTransaksi(),
                                     aturan_bawaan(),hari_ini=lambda:date(2026,11,27))
        layanan.tambah_buku("978-1","Python","Andi")
        self.assertEqual(rb.dicatat,["978-1"])
