
import statistics


def hitung_statistik(data):
    if not data:
        raise ValueError("Data tidak boleh kosong.")

    hasil = {
        "jumlah_data": len(data),
        "rata_rata": statistics.mean(data),
        "median": statistics.median(data),
        "nilai_minimum": min(data),
        "nilai_maksimum": max(data),
        "rentang": max(data) - min(data),
    }

    return hasil
