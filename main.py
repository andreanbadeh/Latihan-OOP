from data.mahasiswa import DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import ViewMahasiswa

def main():
    data_mahasiswa = DataMahasiswa()

    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Lihat Semua Mahasiswa")
        print("3. Cari Mahasiswa")
        print("4. Ubah Mahasiswa")
        print("5. Hapus Mahasiswa")
        print("6. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim, nama, jurusan = InputForm.input_mahasiswa()
            data_mahasiswa.tambah_mahasiswa(nim, nama, jurusan)
            print("Mahasiswa berhasil ditambahkan.")

        elif pilihan == "2":
            ViewMahasiswa.tampilkan_semua_mahasiswa(data_mahasiswa.semua_mahasiswa())

        elif pilihan == "3":
            nim = input("Masukkan NIM yang dicari: ")
            mahasiswa = data_mahasiswa.cari_mahasiswa(nim)
            ViewMahasiswa.tampilkan_mahasiswa(mahasiswa)

        elif pilihan == "4":
            nim = input("Masukkan NIM yang akan diubah: ")
            nama_baru = input("Masukkan Nama baru (kosongkan jika tidak diubah): ")
            jurusan_baru = input("Masukkan Jurusan baru (kosongkan jika tidak diubah): ")
            data_mahasiswa.ubah_mahasiswa(nim, nama_baru, jurusan_baru)
            print("Data mahasiswa berhasil diubah.")

        elif pilihan == "5":
            nim = input("Masukkan NIM yang akan dihapus: ")
            data_mahasiswa.hapus_mahasiswa(nim)
            print("Mahasiswa berhasil dihapus.")

        elif pilihan == "6":
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
