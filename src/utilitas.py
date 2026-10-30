
from pathlib import Path
from datetime import datetime


def tampilkan_hasil(hasil):
    print("\n" + "=" * 35)
    print("       HASIL ANALISIS FATIH")
    print("=" * 35)

    print(f"Jumlah data    : {hasil['jumlah_data']}")
    print(f"Rata-rata      : {hasil['rata_rata']:.2f}")
    print(f"Median         : {hasil['median']:.2f}")
    print(f"Nilai minimum  : {hasil['nilai_minimum']:.2f}")
    print(f"Nilai maksimum : {hasil['nilai_maksimum']:.2f}")
    print(f"Rentang        : {hasil['rentang']:.2f}")

    print("=" * 35)


def simpan_laporan(hasil, lokasi_file="output/laporan.txt"):
    path = Path(lokasi_file)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        file.write("LAPORAN ANALISIS STATISTIK FATIH\n")
        file.write(f"Waktu pembuatan: {datetime.now()}\n\n")

        for nama, nilai in hasil.items():
            if isinstance(nilai, float):
                file.write(f"{nama}: {nilai:.2f}\n")
            else:
                file.write(f"{nama}: {nilai}\n")

    print(f"\nLaporan berhasil disimpan di: {path}")
