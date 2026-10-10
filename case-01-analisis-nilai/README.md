# Studi Kasus 1 — Analisis Nilai Mahasiswa

## Apa yang saya kerjakan?
Bagian akademik punya data nilai mahasiswa (nama, NIM, nilai tugas, UTS, dan UAS).
Program ini membantu menjawab empat pertanyaan:
1. Berapa nilai akhir tiap mahasiswa? (Tugas 30%, UTS 30%, UAS 40%)
2. Siapa saja yang nilai akhirnya di atas 80?
3. Bagaimana urutan dari nilai tertinggi sampai terendah?
4. Siapa mahasiswa terbaiknya?

## Konsep Python yang saya pakai
- **List comprehension**: cara singkat membuat list baru dari list lama. Saya pakai untuk menghitung nilai akhir semua mahasiswa sekaligus dan untuk menyaring yang nilainya di atas 80, jadi tidak perlu loop `for` yang panjang.
- **Lambda**: fungsi kecil tanpa nama. Saya pakai di `sorted()` untuk bilang "urutkan berdasarkan nilai akhir".
- **Filter dan sorting**: filter lewat `if` di dalam list comprehension, urutan lewat `sorted(..., reverse=True)` supaya nilai terbesar ada di paling atas.

## Cara menjalankan
Buka terminal di folder ini, lalu ketik:
```bash
python main.py
```

