
# Pengujian Program FATIH

## Tujuan
Memastikan program dapat membaca data, menghitung statistik, dan menangani kesalahan.

| No. | Kondisi Pengujian | Data/Input | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Data normal | 60, 70, 80 | Rata-rata 70, median 70 |
| 2 | Satu data | 75 | Rata-rata 75, median 75 |
| 3 | Data kosong | File kosong | Pesan kesalahan ditampilkan |
| 4 | Data bukan angka | 70, abc, 80 | Pesan kesalahan menyebut baris bermasalah |
| 5 | File tidak ditemukan | Lokasi file salah | Pesan file tidak ditemukan |
| 6 | Semua nilai sama | 80, 80, 80 | Rata-rata 80, rentang 0 |
| 7 | Data desimal | 70.5, 80.5 | Rata-rata 75.5, median 75.5 |

## Kriteria Keberhasilan
Pengujian dinyatakan berhasil jika hasil program sesuai dengan hasil yang diharapkan dan kesalahan ditangani dengan pesan yang jelas.
