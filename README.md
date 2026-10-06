# Siber Güvenlik - Kriptografi Laboratuvarı

Bu repository, Siber Güvenlik dersi kapsamında gerçekleştirilen kriptografi laboratuvarının ilk dört deneyini içerir.

## Deneyler

1. **Kütüphane kurulumu ve kontrolü**
   - `cryptography`
   - `argon2-cffi`
   - `Pillow`

2. **AES-ECB ve AES-CTR ile görüntü şifreleme**
   - Aynı görüntü ECB ve CTR modlarında şifrelenir.
   - Sonuçlar yan yana karşılaştırılır.
   - Girdi dosyası: `indir.png`

3. **CTR bit-flipping ve AES-GCM bütünlük kontrolü**
   - `Tutar: 100 TL` mesajı CTR modunda şifrelenir.
   - Ciphertext üzerinde kontrollü değişiklik yapılarak mesajın `Tutar: 900 TL` olması gösterilir.
   - Aynı manipülasyon AES-GCM üzerinde denenir ve doğrulama hatası gözlemlenir.

4. **SHA-256 ve Argon2id süre karşılaştırması**
   - SHA-256 ve Argon2id hash işlemlerinin süreleri ölçülür.
   - Argon2id'in parola saklama amacıyla neden daha maliyetli olduğu gözlemlenir.

> Not: Laboratuvarın 5. maddesi olan CBC padding oracle deneyi bu çalışmaya dahil edilmemiştir.

## Kurulum

```bash
python -m pip install -r requirements.txt
```

## Çalıştırma

```bash
python 01_kurulum_test.py
python 02_ecb_ctr_gorsel.py
python 03_ctr_gcm_butunluk.py
python 04_sha256_argon2_sure.py
```

## 2. deney için görsel

`indir.png` dosyasını proje kök dizinine koyun. Program şu çıktıları oluşturur:

- `ecb_sifreli.png`
- `ctr_sifreli.png`
- `karsilastirma.png`

## Amaç

Bu laboratuvar; şifreleme modları arasındaki farkları, yalnızca gizlilik sağlayan CTR ile bütünlük doğrulaması da sağlayan AES-GCM arasındaki farkı ve parola hash algoritmalarının performans özelliklerini gözlemlemek amacıyla hazırlanmıştır.
