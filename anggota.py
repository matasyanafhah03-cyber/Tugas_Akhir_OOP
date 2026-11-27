class Anggota:
    def __init__(self, id_anggota: str, nama: str, kontak: str):
        if not id_anggota or not id_anggota.strip():
            raise ValueError("ID anggota tidak boleh kosong")
        if not nama or not nama.strip():
            raise ValueError("Nama anggota tidak boleh kosong")
        self._id_anggota = id_anggota.strip().upper()
        self._nama = nama.strip()
        self._kontak = kontak.strip() if kontak else ""

    @property
    def id_anggota(self): return self._id_anggota
    @property
    def nama(self): return self._nama
    @property
    def kontak(self): return self._kontak
