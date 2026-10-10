# Studi Kasus 3 — Login Aman dengan Catatan Riwayat (Audit Log)

## Apa yang saya kerjakan?
Program login sederhana yang memeriksa dulu apakah username dan password sudah
sesuai aturan. Setiap percobaan login, berhasil maupun gagal, otomatis dicatat:
kapan dicoba, siapa yang mencoba, dan hasilnya (BERHASIL atau DITOLAK beserta alasannya).

Aturan yang dipakai:
- **Username**: minimal 5 karakter, hanya huruf dan angka (tanpa spasi atau simbol).
- **Password**: minimal 8 karakter dan harus ada minimal satu angka.

## Konsep Python yang saya pakai
- **RegEx**: pola untuk mengecek isi teks. Contohnya `[A-Za-z0-9]{5,}` artinya "huruf atau angka, minimal 5 karakter". Cara ini lebih rapi daripada menulis banyak `if`.
- **@property**: class `User` menjaga username dan password. Setiap kali diisi, nilainya dicek dulu. Kalau tidak sesuai aturan, muncul pesan error. Password juga disimpan dalam bentuk hash, jadi teks aslinya tidak tersimpan.
- **Decorator dan closure**: `@audit_log` dipasang di atas fungsi `login()`. Fungsi pencatatan terpisah dari logika login. Jadi `login()` tetap bersih, tetapi setiap percobaan tetap tercatat.

## Cara menjalankan
Buka terminal di folder ini, lalu ketik:
```bash
python main.py
```

Akun untuk mencoba: username `fandi2026`, password `rahasia123`.

## Skenario yang diuji
1. Username salah format, hasilnya ditolak.
2. Password terlalu pendek atau tidak ada angka, hasilnya ditolak.
3. Format benar tetapi password salah, hasilnya ditolak.
4. Semua benar, hasilnya login berhasil.


