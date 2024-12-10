Nama: ANDREAN PUTRA ARYA

Kelas: TI.24.A4

NIM: 312410341

Matkul: Bahasa Pemrograman

# Latihan OOP

![gambar](https://github.com/andreanbadeh/Latihan-OOP/blob/d0d378be0428cf95cec28d28e1b5ee234729d04c/Images/Screenshot%202024-12-10%20075305.png)

# Penjelasan Code

data -> mahasiswa.py

Mahasiswa: Class yang mewakili entitas mahasiswa. Memiliki atribut: `nim, nama, dan jurusan`. 

Fungsi utama:
`tambah_mahasiswa(nim, nama, jurusan)`: Menambah data mahasiswa baru.

`hapus_mahasiswa(nim)`: Menghapus mahasiswa berdasarkan NIM.

`ubah_mahasiswa(nim, nama_baru, jurusan)`: Memperbarui data mahasiswa tertentu.

`cari_mahasiswa(nim)`: Mencari mahasiswa berdasarkan NIM.

`semua_mahasiswa()`: Mengembalikan seluruh data mahasiswa.

view -> input_form.py

Berisi class InputForm untuk menangani input dari pengguna.

`input_mahasiswa()`: Fungsi untuk meminta pengguna memasukkan data mahasiswa berupa NIM, Nama, dan Jurusan.

view/mahasiswa.py

Berisi class `ViewMahasiswa` untuk menampilkan data mahasiswa ke layar.

Fungsi utama:

`tampilkan_semua_mahasiswa(data)`: Menampilkan semua data mahasiswa dalam bentuk daftar.

`tampilkan_mahasiswa(mahasiswa)`: Menampilkan detail satu mahasiswa tertentu.

main.py

File utama program yang berisi menu untuk berinteraksi dengan pengguna.

Cara kerjanya:

- Tampilkan menu pilihan kepada pengguna.
- Pengguna memasukkan opsi, seperti:
`Tambah mahasiswa`: Memasukkan NIM, Nama, dan Jurusan untuk disimpan.
`Lihat semua mahasiswa`: Menampilkan seluruh data mahasiswa yang sudah tersimpan.
`Cari mahasiswa`: Mencari mahasiswa berdasarkan NIM.
`Ubah mahasiswa`: Memperbarui data mahasiswa tertentu.
`Hapus mahasiswa`: Menghapus data mahasiswa berdasarkan NIM.
`Keluar`: Mengakhiri program.
Setiap pilihan akan memanggil fungsi yang relevan dari modul di folder `data` atau `view`.
