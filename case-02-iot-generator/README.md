# Studi Kasus 2 — Membaca Data Sensor Suhu Tanpa Boros Memori

## Apa yang saya kerjakan?
Sensor cuaca mengirim ribuan data suhu setiap jam. Kalau semuanya dimasukkan ke satu
list sekaligus, memori komputer bisa penuh. Jadi di program ini data tidak
ditumpuk dulu. Suhu dibuat satu per satu, tepat saat dibutuhkan, lalu langsung
dikelompokkan:
- **Dingin**: di bawah 20°C
- **Normal**: 20°C sampai 30°C
- **Panas**: di atas 30°C

Program menampilkan 10 bacaan berturut-turut di terminal.

## Konsep Python yang saya pakai
- **Generator (`yield`)**: fungsi biasa memakai `return` lalu selesai. Fungsi generator memakai `yield`, jadi bisa "berhenti sebentar" setelah memberi satu nilai dan lanjut lagi saat diminta. Dengan begitu suhu dibuat satu per satu.
- **Iterator (`next()`)**: perintah `next()` meminta satu data berikutnya dari generator.
- **Hemat memori**: di akhir program ada perbandingan. List 1 juta data memakai sekitar 8 MB, sedangkan generator hanya sekitar 240 byte.

## Cara menjalankan
Buka terminal di folder ini, lalu ketik:
```bash
python main.py
```


