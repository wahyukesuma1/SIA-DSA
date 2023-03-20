# Object untuk Node LL
class Mahasiswa:
    def __init__(self, data):
        # data untuk menyimpan LL
        self.data = {
            "nim"         : data[0],
            "nama"        : data[1],
            "prodi"       : data[2],
            "kelas"       : data[3],
        }
        # next untuk data berikutnya pada LL
        self.next = None