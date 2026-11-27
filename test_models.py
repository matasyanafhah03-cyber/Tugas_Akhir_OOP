import unittest
from datetime import date
from models.buku import Buku, TERSEDIA, DIPINJAM
from models.anggota import Anggota
from models.peminjaman import Peminjaman

class TestModels(unittest.TestCase):
    def test_buku_baru_tersedia(self):
        self.assertEqual(Buku("1","Judul","Penulis").status, TERSEDIA)
    def test_status_tidak_bisa_diubah_langsung(self):
        b=Buku("1","Judul","Penulis")
        with self.assertRaises(AttributeError): b.status="hilang"
    def test_isbn_kosong_ditolak(self):
        with self.assertRaises(ValueError): Buku(" ","Judul","Penulis")
    def test_siklus_peminjaman_pengembalian(self):
        b=Buku("1","Judul","Penulis"); a=Anggota("A1","Nama","")
        p=Peminjaman("t001",b,a,date(2026,1,1)); p.proses_peminjaman()
        self.assertEqual(b.status,DIPINJAM)
        p.proses_pengembalian(date(2026,1,2))
        self.assertEqual(p.status,Peminjaman.SELESAI)
        self.assertTrue(b.tersedia())
