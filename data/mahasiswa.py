class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

class DataMahasiswa:
    def __init__(self):
        self.data = []

    def tambah_mahasiswa(self, nim, nama, jurusan):
        mahasiswa = Mahasiswa(nim, nama, jurusan)
        self.data.append(mahasiswa)

    def hapus_mahasiswa(self, nim):
        self.data = [m for m in self.data if m.nim != nim]

    def ubah_mahasiswa(self, nim, nama_baru=None, jurusan_baru=None):
        for m in self.data:
            if m.nim == nim:
                if nama_baru:
                    m.nama = nama_baru
                if jurusan_baru:
                    m.jurusan = jurusan_baru

    def cari_mahasiswa(self, nim):
        return next((m for m in self.data if m.nim == nim), None)

    def semua_mahasiswa(self):
        return self.data
