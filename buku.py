TERSEDIA = "tersedia"
DIPINJAM = "dipinjam"

class Buku:
    def __init__(self, isbn: str, judul: str, penulis: str):
        if not isbn or not isbn.strip():
            raise ValueError("ISBN tidak boleh kosong")
        if not judul or not judul.strip():
            raise ValueError("Judul buku tidak boleh kosong")
        if not penulis or not penulis.strip():
            raise ValueError("Penulis tidak boleh kosong")
        self._isbn = isbn.strip()
        self._judul = judul.strip()
        self._penulis = penulis.strip()
        self._status = TERSEDIA

    @property
    def isbn(self): return self._isbn
    @property
    def judul(self): return self._judul
    @property
    def penulis(self): return self._penulis
    @property
    def status(self): return self._status

    def tersedia(self) -> bool:
        return self._status == TERSEDIA

    def tandai_dipinjam(self) -> None:
        if not self.tersedia():
            raise ValueError(f"Buku '{self._judul}' sedang dipinjam")
        self._status = DIPINJAM

    def tandai_tersedia(self) -> None:
        if self.tersedia():
            raise ValueError(f"Buku '{self._judul}' sudah tersedia")
        self._status = TERSEDIA
