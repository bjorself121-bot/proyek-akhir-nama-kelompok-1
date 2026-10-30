# Pengujian Program FATIH

## Tujuan
Memastikan program dapat membaca data, menghitung statistik, dan menangani kesalahan.

## Tabel Pengujian

| No. | Kondisi Pengujian | Data/Input | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|---|---|
| 1 | Data normal | 60, 70, 80 | Rata-rata 70, median 70 | Rata-rata 70, median 70 | PASS |
| 2 | Satu data | 75 | Rata-rata 75, median 75 | Rata-rata 75, median 75; rentang 0 | PASS |
| 3 | Data kosong | File kosong | Pesan kesalahan ditampilkan | Pesan file tidak memiliki data angka | PASS |
| 4 | Data bukan angka | 70, abc, 80 | Pesan kesalahan menyebut baris bermasalah | Pesan kesalahan menyebut baris 2 | PASS |
| 5 | File tidak ditemukan | File input sementara diganti nama | Pesan file tidak ditemukan | Pesan file tidak ditemukan | PASS |
| 6 | Semua nilai sama | 80, 80, 80 | Rata-rata 80, rentang 0 | Rata-rata 80, rentang 0 | PASS |
| 7 | Data desimal | 70.5, 80.5 | Rata-rata 75.5, median 75.5 | Rata-rata 75.50, median 75.50 | PASS |

## Kriteria Keberhasilan
Pengujian berhasil jika hasil program sesuai dengan hasil yang diharapkan dan kesalahan ditangani dengan pesan yang jelas.

## Catatan
- PASS: hasil aktual sesuai dengan hasil yang diharapkan.
- FAIL: hasil aktual tidak sesuai dengan hasil yang diharapkan.
- Belum diuji: pengujian belum dijalankan.
