import random
import csv
import os

DOSYA_ADI = "skorlar.csv"


def sayi_tahmin():
    """
    1-100 arasında rastgele bir sayı üretir ve kullanıcıya tahmin ettirir.

    Kullanıcıya 7 hak verilir. Her yanlış tahminde yönlendirme yapılır
    ('daha büyük' / 'daha küçük').

    Returns:
        int: Doğru tahmin edilirse 50 puan, aksi halde 0 puan.
    """
    sayi = random.randint(1, 100)
    hak = 7

    print("\n1-100 arasında bir sayı tuttum!")

    for i in range(hak):
        try:
            tahmin = int(input(f"{i+1}. tahmin: "))

            if tahmin == sayi:
                print("Doğru bildin! +50 puan")
                return 50
            elif tahmin < sayi:
                print("Daha büyük!")
            else:
                print("Daha küçük!")

        except ValueError:
            print("Hatalı giriş! Sayı girmen lazım.")

    print(f"Bilemedin! Sayı: {sayi}")
    return 0


def yazi_tura():
    """
    Yazı-tura oyunu oynatır.

    Kullanıcı 'y' (yazı) veya 't' (tura) seçer.
    Rastgele sonuç ile karşılaştırılır.

    Returns:
        int: Doğru tahmin edilirse 20 puan, aksi halde 0 puan.
    """
    secim = input("Yazı mı Tura mı? (y/t): ").lower()
    sonuc = random.choice(["y", "t"])

    if secim == sonuc:
        print("Kazandın! +20 puan")
        return 20
    else:
        print("Kaybettin!")
        return 0


def skor_kaydet(oyuncu, oyun, puan):
    """
    Oyuncunun skorunu CSV dosyasına kaydeder.

    Dosya yoksa otomatik oluşturulur ve başlık satırı eklenir.

    Args:
        oyuncu (str): Oyuncu adı
        oyun (str): Oynanan oyun adı
        puan (int): Kazanılan puan
    """
    dosya_var = os.path.isfile(DOSYA_ADI)

    with open(DOSYA_ADI, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        if not dosya_var:
            writer.writerow(["Oyuncu", "Oyun", "Puan"])

        writer.writerow([oyuncu, oyun, puan])


def skor_goster():
    """
    CSV dosyasındaki tüm skorları okuyup ekrana yazdırır.

    Eğer dosya bulunamazsa otomatik oluşturur.
    """
    try:
        with open(DOSYA_ADI, "r", encoding="utf-8") as file:
            reader = csv.reader(file)

            print("\n--- SKORLAR ---")
            for satir in reader:
                print(" | ".join(satir))

    except FileNotFoundError:
        print("Skor dosyası yoktu, oluşturuluyor...")
        with open(DOSYA_ADI, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Oyuncu", "Oyun", "Puan"])