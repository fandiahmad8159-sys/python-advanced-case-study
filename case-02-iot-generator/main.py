"""Studi Kasus 2 - Streaming Data Sensor IoT Hemat Memori.

Konsep: generator function (yield), iterator (next), efisiensi memori.
"""

import random
import sys
import time

SUHU_MIN = 15.0
SUHU_MAX = 38.0


def sensor_suhu(jumlah=None, seed=None):
    """Generator: menghasilkan suhu satu per satu, tidak pernah membuat list besar.

    jumlah=None berarti aliran tak terbatas (seperti sensor sungguhan).
    """
    rng = random.Random(seed)
    terkirim = 0
    while jumlah is None or terkirim < jumlah:
        yield round(rng.uniform(SUHU_MIN, SUHU_MAX), 1)
        terkirim += 1


def kategori_suhu(suhu):
    """Dingin < 20, Normal 20-30, Panas > 30."""
    if suhu < 20:
        return "Dingin"
    if suhu <= 30:
        return "Normal"
    return "Panas"


def main():
    stream = sensor_suhu(seed=42)  # generator: belum ada data yang dibuat
    print("=== Pemantau Suhu Stasiun Cuaca (streaming) ===")
    print(f"{'Bacaan':<8} {'Suhu':>8}   Status")
    print("-" * 28)

    for nomor in range(1, 11):  # ambil 10 bacaan berturut-turut
        suhu = next(stream)  # data baru dibuat tepat saat diminta
        print(f"#{nomor:<7} {suhu:>6.1f}°C   {kategori_suhu(suhu)}")
        time.sleep(0.05)  # simulasi jeda antar bacaan

    # Bukti efisiensi memori: generator vs list
    print("\n=== Perbandingan Memori (1.000.000 data) ===")
    sebagai_list = [round(random.uniform(SUHU_MIN, SUHU_MAX), 1) for _ in range(1_000_000)]
    sebagai_generator = sensor_suhu(jumlah=1_000_000)
    print(f"List      : {sys.getsizeof(sebagai_list):>12,} byte")
    print(f"Generator : {sys.getsizeof(sebagai_generator):>12,} byte")


if __name__ == "__main__":
    main()
