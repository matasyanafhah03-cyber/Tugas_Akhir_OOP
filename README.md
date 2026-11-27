# Sistem Peminjaman Buku Perpustakaan

Aplikasi CLI Python untuk pengelolaan katalog buku, anggota, peminjaman, pengembalian, dan riwayat transaksi. Proyek menggunakan OOP dan prinsip SOLID sesuai rancangan Milestone 2 Kelompok 3.

## Kebutuhan
- Python 3.10 atau lebih baru
- Tidak membutuhkan library eksternal

## Menjalankan aplikasi
Dari folder utama proyek:

```bash
python --version
python main.py
```

Mode tanpa data contoh:

```bash
python main.py --kosong
```

## Menjalankan pengujian

```bash
python -m unittest discover -v
```

## Struktur proyek

```text
sistem-peminjaman-buku/
├── main.py
├── models/
│   ├── buku.py
│   ├── anggota.py
│   └── peminjaman.py
├── aturan/
│   └── aturan_peminjaman.py
├── repositories/
│   ├── kontrak.py
│   └── memori.py
├── services/
│   └── layanan_perpustakaan.py
├── tampilan/
│   ├── penampil.py
│   └── menu_cli.py
└── tests/
    ├── test_models.py
    ├── test_aturan.py
    └── test_layanan.py
```

## Fitur
1. Tambah buku
2. Lihat katalog
3. Cari buku
4. Cek ketersediaan
5. Tambah anggota
6. Lihat anggota
7. Pinjam buku (validasi anggota, buku, status, dan batas maksimal tiga pinjaman aktif)
8. Kembalikan buku
9. Riwayat transaksi
10. Riwayat transaksi per anggota

## Catatan
Versi ini menggunakan repositori memori. Data akan kembali kosong ketika program ditutup. Penyimpanan permanen JSON merupakan pengembangan berikutnya (Milestone 3).
