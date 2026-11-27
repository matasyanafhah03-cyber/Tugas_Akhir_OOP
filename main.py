import sys
from aturan.aturan_peminjaman import aturan_bawaan
from repositories.memori import (MemoriRepositoriBuku, MemoriRepositoriAnggota,
                                 MemoriRepositoriTransaksi)
from services.layanan_perpustakaan import LayananPerpustakaan
from tampilan.menu_cli import MenuCLI
from tampilan.penampil import KonsolPenampil

def buat_layanan():
    repo_buku = MemoriRepositoriBuku()
    repo_anggota = MemoriRepositoriAnggota()
    repo_transaksi = MemoriRepositoriTransaksi()
    return LayananPerpustakaan(repo_buku, repo_anggota, repo_transaksi, aturan_bawaan())

def isi_data_contoh(layanan):
    layanan.tambah_buku("978-602-0001-01-1", "Dasar Pemrograman Python", "Andi Pratama")
    layanan.tambah_buku("978-602-0001-02-8", "Pemrograman Berorientasi Objek", "Siti Rahmawati")
    layanan.tambah_buku("978-602-0001-03-5", "Struktur Data dengan Python", "Budi Santoso")
    layanan.tambah_anggota("A001", "Matasya Nafhah Defrizal", "0815-5555-6666")
    layanan.tambah_anggota("A002", "Revian Bagas Maulana", "0812-1111-2222")

if __name__ == "__main__":
    layanan = buat_layanan()
    if "--kosong" not in sys.argv:
        isi_data_contoh(layanan)
    MenuCLI(layanan, KonsolPenampil()).jalankan()
