class PenampilPesan:
    def tampilkan_hasil(self, hasil):
        label = "[BERHASIL]" if hasil.berhasil else "[GAGAL]"
        print(f"{label} {hasil.pesan}")

class PenampilDaftar:
    def tampilkan_daftar(self, judul, data):
        print(f"\n--- {judul} ({len(data)} data) ---")
        if not data:
            print("Belum ada data.")
            return
        for i, item in enumerate(data, 1):
            if hasattr(item, "isbn"):
                print(f"{i}. {item.isbn} | {item.judul} | {item.penulis} | {item.status}")
            elif hasattr(item, "id_anggota"):
                print(f"{i}. {item.id_anggota} | {item.nama} | {item.kontak}")
            else:
                print(f"{i}. {item.id_transaksi} | {item.anggota.nama} | "
                      f"{item.buku.judul} | pinjam {item.tanggal_pinjam} | "
                      f"kembali {item.tanggal_kembali or '-'} | {item.status}")

class KonsolPenampil(PenampilPesan, PenampilDaftar):
    pass
