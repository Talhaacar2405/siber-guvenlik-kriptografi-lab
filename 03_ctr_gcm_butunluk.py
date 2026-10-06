from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidTag
import os

mesaj = b"Tutar: 100 TL"

print("=" * 50)
print("AES-CTR DENEYI")
print("=" * 50)

key = os.urandom(16)
nonce = os.urandom(16)

encryptor = Cipher(algorithms.AES(key), modes.CTR(nonce)).encryptor()
ciphertext = encryptor.update(mesaj) + encryptor.finalize()

print("Orijinal mesaj:", mesaj)
print("Ciphertext:", ciphertext.hex())

# "100" -> "900" olacak şekilde ciphertext üzerinde bit-flipping
eski = b"100"
yeni = b"900"
offset = mesaj.index(eski)

degistirilmis = bytearray(ciphertext)
for i in range(len(eski)):
    degistirilmis[offset + i] ^= eski[i] ^ yeni[i]

decryptor = Cipher(algorithms.AES(key), modes.CTR(nonce)).decryptor()
cozulmus = decryptor.update(bytes(degistirilmis)) + decryptor.finalize()

print("Değiştirilmiş ciphertext çözüldüğünde:", cozulmus)

print("\n" + "=" * 50)
print("AES-GCM DENEYI")
print("=" * 50)

gcm_key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(gcm_key)
gcm_nonce = os.urandom(12)

gcm_ciphertext = aesgcm.encrypt(gcm_nonce, mesaj, None)
bozuk_ciphertext = bytearray(gcm_ciphertext)
bozuk_ciphertext[0] ^= 1

try:
    sonuc = aesgcm.decrypt(gcm_nonce, bytes(bozuk_ciphertext), None)
    print("Çözülen mesaj:", sonuc)
except InvalidTag:
    print("GCM değişikliği tespit etti.")
    print("Mesaj üzerinde oynama yapıldığı için doğrulama başarısız.")
