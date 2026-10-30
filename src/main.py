
from pathlib import Path

from data_io import baca_data
from analisis import hitung_statistik
from utilitas import tampilkan_hasil, simpan_laporan


def main():
    print("=" * 35)
    print("       FATIH - ANALISIS DATA")
    print("=" * 35)

    lokasi_data = Path(__file__).resolve().parent.parent / "data" / "nilai_contoh.txt"

    try:
        data = baca_data(lokasi_data)
        hasil = hitung_statistik(data)

        tampilkan_hasil(hasil)
        simpan_laporan(hasil)

    except (FileNotFoundError, ValueError) as error:
        print(f"\nTerjadi kesalahan: {error}")


if __name__ == "__main__":
    main()
