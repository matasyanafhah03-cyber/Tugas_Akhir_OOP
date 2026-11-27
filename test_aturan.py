import unittest
from models.buku import Buku
from models.anggota import Anggota
from aturan.aturan_peminjaman import *

class TestAturan(unittest.TestCase):
    def setUp(self):
        self.a=Anggota("A1","Nama",""); self.b=Buku("1","Judul","Penulis")
    def test_anggota_terdaftar(self):
        self.assertTrue(AturanAnggotaTerdaftar().periksa(self.a,self.b,0).lolos)
    def test_anggota_tidak_terdaftar(self):
        self.assertFalse(AturanAnggotaTerdaftar().periksa(None,self.b,0).lolos)
    def test_buku_ditemukan(self):
        self.assertFalse(AturanBukuDitemukan().periksa(self.a,None,0).lolos)
    def test_buku_tidak_tersedia(self):
        self.b.tandai_dipinjam()
        self.assertFalse(AturanBukuTersedia().periksa(self.a,self.b,0).lolos)
