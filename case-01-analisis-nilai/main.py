"""Studi Kasus 1 - Analisis Nilai Mahasiswa.

Konsep: list comprehension, lambda, filtering & sorting.
"""

BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40
BATAS_PRESTASI = 80

data_mahasiswa = [
    {"nama": "Aisyah", "nim": "230101", "tugas": 85, "uts": 80, "uas": 88},
    {"nama": "Budi", "nim": "230102", "tugas": 70, "uts": 65, "uas": 75},
    {"nama": "Cantika", "nim": "230103", "tugas": 90, "uts": 85, "uas": 92},
    {"nama": "Dimas", "nim": "230104", "tugas": 78, "uts": 82, "uas": 80},
    {"nama": "Eka", "nim": "230105", "tugas": 60, "uts": 70, "uas": 65},
]


def hitung_nilai_akhir(data):
    """Kembalikan list baru: setiap mahasiswa + kunci 'akhir' (list comprehension)."""
    return [
        {
            **m,
            "akhir": round(
                m["tugas"] * BOBOT_TUGAS + m["uts"] * BOBOT_UTS + m["uas"] * BOBOT_UAS, 2
            ),
        }
        for m in data
    ]


def filter_berprestasi(data, batas=BATAS_PRESTASI):
    """Mahasiswa dengan nilai akhir di atas batas (tanpa for bertingkat)."""
    return [m for m in data if m["akhir"] > batas]


def buat_ranking(data):
    """Urutkan dari nilai akhir tertinggi ke terendah (sorted + lambda)."""
    return sorted(data, key=lambda m: m["akhir"], reverse=True)


def cetak_tabel(judul, data):
    print(f"\n=== {judul} ===")
    if not data:
        print("(tidak ada data)")
        return
    print(f"{'No':<3} {'NIM':<8} {'Nama':<10} {'Tugas':>5} {'UTS':>5} {'UAS':>5} {'Akhir':>7}")
    print("-" * 49)
    for i, m in enumerate(data, start=1):
        print(
            f"{i:<3} {m['nim']:<8} {m['nama']:<10} "
            f"{m['tugas']:>5} {m['uts']:>5} {m['uas']:>5} {m['akhir']:>7.2f}"
        )


def main():
    dengan_nilai = hitung_nilai_akhir(data_mahasiswa)
    cetak_tabel("1. Nilai Akhir Seluruh Mahasiswa", dengan_nilai)

    berprestasi = filter_berprestasi(dengan_nilai)
    cetak_tabel(f"2. Mahasiswa Berprestasi (nilai akhir > {BATAS_PRESTASI})", berprestasi)

    ranking = buat_ranking(dengan_nilai)
    cetak_tabel("3. Ranking (tertinggi -> terendah)", ranking)

    terbaik = ranking[0]
    print("\n=== 4. Mahasiswa Terbaik ===")
    print(f"Nama        : {terbaik['nama']}")
    print(f"NIM         : {terbaik['nim']}")
    print(f"Tugas / UTS / UAS : {terbaik['tugas']} / {terbaik['uts']} / {terbaik['uas']}")
    print(f"Nilai Akhir : {terbaik['akhir']:.2f}")


if __name__ == "__main__":
    main()
