from PIL import Image
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

print("Program başladı.")

dosya_adi = "indir.png"

if not os.path.exists(dosya_adi):
    print(f"HATA: {dosya_adi} bulunamadı.")
    print("Resmi Python dosyasıyla aynı klasöre koy.")
    input("Çıkmak için Enter'a bas...")
    raise SystemExit

img = Image.open(dosya_adi).convert("RGB")
width, height = img.size
data = img.tobytes()

print("Resim bulundu.")
print("Boyut:", width, "x", height)

key = os.urandom(16)

# AES-ECB
padding_length = (16 - len(data) % 16) % 16
padded_data = data + bytes([0] * padding_length)

cipher_ecb = Cipher(algorithms.AES(key), modes.ECB())
encryptor_ecb = cipher_ecb.encryptor()
encrypted_ecb = encryptor_ecb.update(padded_data) + encryptor_ecb.finalize()
encrypted_ecb = encrypted_ecb[:len(data)]

img_ecb = Image.frombytes("RGB", (width, height), encrypted_ecb)
img_ecb.save("ecb_sifreli.png")
print("ECB tamamlandı.")

# AES-CTR
nonce = os.urandom(16)
cipher_ctr = Cipher(algorithms.AES(key), modes.CTR(nonce))
encryptor_ctr = cipher_ctr.encryptor()
encrypted_ctr = encryptor_ctr.update(data) + encryptor_ctr.finalize()

img_ctr = Image.frombytes("RGB", (width, height), encrypted_ctr)
img_ctr.save("ctr_sifreli.png")
print("CTR tamamlandı.")

# Yan yana karşılaştırma
result = Image.new("RGB", (width * 3, height))
result.paste(img, (0, 0))
result.paste(img_ecb, (width, 0))
result.paste(img_ctr, (width * 2, 0))

result.save("karsilastirma.png")

print("\nOluşan dosyalar:")
print("ecb_sifreli.png")
print("ctr_sifreli.png")
print("karsilastirma.png")

try:
    result.show()
except Exception:
    print("Görüntü otomatik açılamadı; karsilastirma.png dosyasını açabilirsin.")

input("\nProgram bitti. Çıkmak için Enter'a bas...")
