
# FATIH — AI Statistical Assistant

## 1. Deskripsi Proyek
FATIH adalah program berbasis Python yang dirancang untuk membantu pengguna mengolah data numerik dan memperoleh informasi statistik deskriptif secara sederhana.

Proyek ini dikembangkan sebagai tugas mata kuliah Algoritma dan Pemrograman dengan pendekatan bertahap, dimulai dari aplikasi berbasis terminal.

## 2. Tujuan
- Mempermudah pengolahan data numerik.
- Menghitung statistik deskriptif secara otomatis.
- Melatih penerapan fungsi, struktur data, validasi input, dan pengolahan file dalam Python.
- Menyimpan hasil analisis dalam bentuk laporan teks.

## 3. Fitur
- Membaca data angka dari file teks.
- Memvalidasi data dan menangani kesalahan input.
- Menghitung jumlah data.
- Menghitung rata-rata dan median.
- Menentukan nilai minimum dan maksimum.
- Menghitung rentang data.
- Menampilkan hasil analisis di terminal.
- Menyimpan laporan hasil analisis.

## 4. Teknologi
- Python 3
- Visual Studio Code
- Git dan GitHub

## 5. Struktur Proyek
```text
FATIH-Alpro/
├── data/
│   └── nilai_contoh.txt
├── output/
│   └── .gitkeep
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
├── tests/
│   └── test_case.md
├── .gitignore
├── proposal.md
└── README.md
```

## 6. Cara Menjalankan
1. Pastikan Python sudah terpasang.
2. Buka terminal pada direktori utama proyek.
3. Jalankan perintah berikut:

```bash
python src/main.py
```

Program akan membaca data dari `data/nilai_contoh.txt`, menghitung statistik, menampilkan hasil, dan menyimpan laporan ke direktori `output/`.

## 7. Format Data
Data disimpan dalam file teks dengan satu angka pada setiap baris.

Contoh:

```text
78
85
90
67
88
75
92
80
```

## 8. Pengujian
Pengujian dirancang untuk memeriksa:
- Data normal.
- Satu data.
- Data kosong.
- Data bukan angka.
- File tidak ditemukan.
- Semua nilai sama.
- Data desimal.

Hasil aktual setiap pengujian perlu dicocokkan dengan hasil yang diharapkan dan dicatat dalam `tests/test_case.md`.

## 9. Batasan Versi Saat Ini
Versi awal FATIH menggunakan antarmuka terminal dan membaca data numerik dari file teks. Versi ini belum menyediakan antarmuka web, database, akun pengguna, maupun analisis berbasis AI.

## 10. Rencana Pengembangan
- Mendukung pembacaan data CSV.
- Menambahkan perhitungan simpangan baku.
- Menambahkan pilihan file input.
- Mengembangkan pengujian otomatis.
- Menambahkan visualisasi dan interpretasi data pada tahap berikutnya.

## 11. Status Proyek
Proyek dikembangkan secara bertahap sebagai tugas Algoritma dan Pemrograman. Fitur yang dicantumkan sebagai fitur saat ini perlu sesuai dengan implementasi yang benar-benar sudah diuji.
