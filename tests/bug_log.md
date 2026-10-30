# Bug Log dan Catatan Penanganan Kesalahan FATIH

## BUG-01 — Input mengandung data bukan angka

- **Gejala:** Program menerima file yang berisi nilai `70`, `abc`, dan `80`.
- **Hasil yang diharapkan:** Program menolak data yang tidak valid dan menunjukkan baris yang bermasalah.
- **Hasil aktual:** Program menampilkan pesan bahwa data pada baris 2 bukan angka yang valid.
- **Penanganan:** Validasi input berjalan dan kesalahan ditampilkan dengan jelas.
- **Status:** Closed — pengujian validasi berhasil.

## Catatan
BUG-01 merupakan catatan pengujian penanganan input tidak valid. Pengujian ini tidak membuktikan adanya cacat pada program karena program telah menangani input tersebut sesuai harapan.
