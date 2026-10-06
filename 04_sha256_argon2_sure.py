import hashlib
import time
from argon2 import PasswordHasher

password = "SiberGuvenlik123!".encode()

# SHA-256
sha_tekrar = 100000
baslangic = time.perf_counter()

for _ in range(sha_tekrar):
    hashlib.sha256(password).digest()

bitis = time.perf_counter()
sha_toplam = bitis - baslangic
sha_ortalama = sha_toplam / sha_tekrar

print("=" * 50)
print("SHA-256")
print("=" * 50)
print(f"{sha_tekrar} işlem toplam süre: {sha_toplam:.6f} saniye")
print(f"Tek SHA-256 ortalama: {sha_ortalama * 1000:.6f} ms")

# Argon2id
ph = PasswordHasher()
argon_tekrar = 5
baslangic = time.perf_counter()

for _ in range(argon_tekrar):
    ph.hash(password.decode())

bitis = time.perf_counter()
argon_toplam = bitis - baslangic
argon_ortalama = argon_toplam / argon_tekrar

print("\n" + "=" * 50)
print("Argon2id")
print("=" * 50)
print(f"{argon_tekrar} işlem toplam süre: {argon_toplam:.6f} saniye")
print(f"Tek Argon2id ortalama: {argon_ortalama * 1000:.3f} ms")

oran = argon_ortalama / sha_ortalama

print("\n" + "=" * 50)
print("KARŞILAŞTIRMA")
print("=" * 50)
print(f"Argon2id yaklaşık {oran:.0f} kat daha yavaş.")
