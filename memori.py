from .kontrak import RepositoriBuku, RepositoriAnggota, RepositoriTransaksi

class MemoriRepositoriBuku(RepositoriBuku):
    def __init__(self): self._data = {}
    def simpan(self, buku): self._data[buku.isbn] = buku
    def cari_isbn(self, isbn): return self._data.get(isbn.strip()) if isbn else None
    def semua(self): return list(self._data.values())

class MemoriRepositoriAnggota(RepositoriAnggota):
    def __init__(self): self._data = {}
    def simpan(self, anggota): self._data[anggota.id_anggota.upper()] = anggota
    def cari_id(self, id_anggota): return self._data.get(id_anggota.strip().upper()) if id_anggota else None
    def semua(self): return list(self._data.values())

class MemoriRepositoriTransaksi(RepositoriTransaksi):
    def __init__(self): self._data = {}
    def simpan(self, transaksi): self._data[transaksi.id_transaksi.upper()] = transaksi
    def cari_id(self, id_transaksi): return self._data.get(id_transaksi.strip().upper()) if id_transaksi else None
    def semua(self): return list(self._data.values())
