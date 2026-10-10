"""Studi Kasus 3 - Sistem Keamanan Akun & Audit Log Login.

Konsep: RegEx, decorator & closure, @property (enkapsulasi OOP).
"""

import functools
import hashlib
import re
from datetime import datetime

# ---------- Aturan validasi (RegEx) ----------
POLA_USERNAME = re.compile(r"[A-Za-z0-9]{5,}")  # alfanumerik, minimal 5, tanpa spasi/simbol
POLA_PASSWORD = re.compile(r"(?=.*\d).{8,}")    # minimal 8 karakter & ada minimal 1 angka


def _hash(teks):
    return hashlib.sha256(teks.encode()).hexdigest()


# ---------- Model Pengguna (@property) ----------
class User:
    def __init__(self, username, password):
        self.username = username  # memicu setter -> validasi
        self.password = password

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, nilai):
        if not POLA_USERNAME.fullmatch(nilai):
            raise ValueError(
                "Format username salah (minimal 5 karakter, hanya huruf & angka)"
            )
        self._username = nilai

    @property
    def password(self):
        return "********"  # password asli tidak pernah dibuka

    @password.setter
    def password(self, nilai):
        if not POLA_PASSWORD.fullmatch(nilai):
            raise ValueError(
                "Format password salah (minimal 8 karakter & memuat minimal 1 angka)"
            )
        self._hash_password = _hash(nilai)  # simpan hash, bukan teks asli

    def cek_password(self, kandidat):
        return self._hash_password == _hash(kandidat)


# ---------- Decorator audit log (closure) ----------
def audit_log(fungsi):
    @functools.wraps(fungsi)
    def pembungkus(username, password):
        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        berhasil, alasan = fungsi(username, password)
        status = "BERHASIL" if berhasil else f"DITOLAK ({alasan})"
        print(f"[{waktu}] user='{username}' -> {status}")
        return berhasil, alasan

    return pembungkus


# "Database" akun terdaftar (password disimpan sebagai hash)
AKUN_TERDAFTAR = {"fandi2026": _hash("rahasia123")}


@audit_log
def login(username, password):
    """Kembalikan (berhasil, alasan). Logika pencatatan ada di decorator."""
    try:
        user = User(username, password)  # validasi format via @property + RegEx
    except ValueError as err:
        return False, str(err)

    hash_tersimpan = AKUN_TERDAFTAR.get(user.username)
    if hash_tersimpan is None or hash_tersimpan != _hash(password):
        return False, "Username atau password salah"
    return True, "OK"


def main():
    print("=== Skenario Pengujian Login ===")
    print("\n1) Username tidak sesuai aturan (ada simbol & terlalu pendek)")
    login("ab!", "rahasia123")

    print("\n2a) Password terlalu pendek")
    login("fandi2026", "abc1")

    print("\n2b) Password tidak mengandung angka")
    login("fandi2026", "passwordpanjang")

    print("\n3) Format benar tetapi password salah")
    login("fandi2026", "salahsalah9")

    print("\n4) Login sukses")
    login("fandi2026", "rahasia123")


if __name__ == "__main__":
    main()
