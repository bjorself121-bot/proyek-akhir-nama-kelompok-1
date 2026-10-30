
from pathlib import Path


def baca_data(lokasi_file):
    path = Path(lokasi_file)

    if not path.exists():
        raise FileNotFoundError(
            f"File tidak ditemukan: {lokasi_file}"
        )

    data = []

    with path.open("r", encoding="utf-8") as file:
        for nomor_baris, baris in enumerate(file, start=1):
            isi = baris.strip()

            if not isi:
                continue

            try:
                angka = float(isi)
            except ValueError:
                raise ValueError(
                    f"Data pada baris {nomor_baris} "
                    "bukan angka yang valid."
                )

            data.append(angka)

    if not data:
        raise ValueError("File tidak memiliki data angka.")

    return data
