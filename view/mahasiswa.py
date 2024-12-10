class ViewMahasiswa:
    @staticmethod
    def tampilkan_semua_mahasiswa(data):
        if not data:
            print("Tidak ada data mahasiswa.")
        else:
            for m in data:
                print(f"NIM: {m.nim}, Nama: {m.nama}, Jurusan: {m.jurusan}")

    @staticmethod
    def tampilkan_mahasiswa(mahasiswa):
        if mahasiswa:
            print(f"NIM: {mahasiswa.nim}, Nama: {mahasiswa.nama}, Jurusan: {mahasiswa.jurusan}")
        else:
            print("Mahasiswa tidak ditemukan.")
