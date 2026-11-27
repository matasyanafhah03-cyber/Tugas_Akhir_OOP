class MenuCLI:
    def __init__(self, layanan, penampil):
        self._layanan, self._penampil = layanan, penampil

    def jalankan(self):
        while True:
            try:
                print("\\n===== SISTEM PEMINJAMAN BUKU PERPUSTAKAAN =====")
                print("1. Tambah buku")
                print("2. Lihat katalog")
                print("3. Cari buku")
                print("4. Cek ketersediaan")
                print("5. Tambah anggota")
                print("6. Lihat anggota")
                print("7. Pinjam buku")
                print("8. Kembalikan buku")
                print("9. Riwayat transaksi")
                print("10. Riwayat per anggota")
                print("0. Keluar")
                pilihan = input("Pilih menu: ").strip()
                if pilihan == "0":
                    print("Terima kasih. Program selesai.")
                    break
                if pilihan == "1":
                    self._penampil.tampilkan_hasil(self._layanan.tambah_buku(
                        input("ISBN: "), input("Judul: "), input("Penulis: ")))
                elif pilihan == "2":
                    self._penampil.tampilkan_daftar("Katalog buku", self._layanan.daftar_buku())
                elif pilihan == "3":
                    self._penampil.tampilkan_daftar("Hasil pencarian", self._layanan.cari_buku(input("Kata kunci: ")))
                elif pilihan == "4":
                    self._penampil.tampilkan_hasil(self._layanan.cek_ketersediaan(input("ISBN: ")))
                elif pilihan == "5":
                    self._penampil.tampilkan_hasil(self._layanan.tambah_anggota(
                        input("ID anggota: "), input("Nama: "), input("Kontak: ")))
                elif pilihan == "6":
                    self._penampil.tampilkan_daftar("Daftar anggota", self._layanan.daftar_anggota())
                elif pilihan == "7":
                    self._penampil.tampilkan_hasil(self._layanan.catat_peminjaman(
                        input("ID anggota: "), input("ISBN buku: ")))
                elif pilihan == "8":
                    self._penampil.tampilkan_hasil(self._layanan.kembalikan_buku(input("ID transaksi: ")))
                elif pilihan == "9":
                    self._penampil.tampilkan_daftar("Riwayat transaksi", self._layanan.riwayat_transaksi())
                elif pilihan == "10":
                    self._penampil.tampilkan_daftar("Riwayat anggota", self._layanan.riwayat_anggota(input("ID anggota: ")))
                else:
                    print(f"[GAGAL] Menu '{pilihan}' tidak tersedia")
            except (EOFError, KeyboardInterrupt):
                print("\\nProgram dihentikan.")
                break
