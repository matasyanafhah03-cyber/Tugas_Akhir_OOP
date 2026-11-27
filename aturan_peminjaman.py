from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass(frozen=True)
class HasilPeriksa:
    lolos: bool
    pesan: str = ""

    @classmethod
    def ok(cls): return cls(True, "")
    @classmethod
    def gagal(cls, alasan): return cls(False, alasan)

class AturanPeminjaman(ABC):
    @abstractmethod
    def periksa(self, anggota, buku, jumlah_pinjaman_aktif) -> HasilPeriksa:
        raise NotImplementedError

class AturanAnggotaTerdaftar(AturanPeminjaman):
    def periksa(self, anggota, buku, jumlah_pinjaman_aktif):
        return HasilPeriksa.ok() if anggota is not None else HasilPeriksa.gagal("ID anggota tidak terdaftar")

class AturanBukuDitemukan(AturanPeminjaman):
    def periksa(self, anggota, buku, jumlah_pinjaman_aktif):
        return HasilPeriksa.ok() if buku is not None else HasilPeriksa.gagal("Buku tidak ditemukan")

class AturanBukuTersedia(AturanPeminjaman):
    def periksa(self, anggota, buku, jumlah_pinjaman_aktif):
        if buku is not None and not buku.tersedia():
            return HasilPeriksa.gagal(f"Buku '{buku.judul}' sedang dipinjam")
        return HasilPeriksa.ok()

class AturanBatasPinjam(AturanPeminjaman):
    def __init__(self, maksimal=3): self._maksimal = maksimal
    def periksa(self, anggota, buku, jumlah_pinjaman_aktif):
        if anggota is not None and jumlah_pinjaman_aktif >= self._maksimal:
            return HasilPeriksa.gagal(f"Anggota telah mencapai batas {self._maksimal} pinjaman")
        return HasilPeriksa.ok()

def aturan_bawaan():
    return [AturanAnggotaTerdaftar(), AturanBukuDitemukan(),
            AturanBukuTersedia(), AturanBatasPinjam(3)]
