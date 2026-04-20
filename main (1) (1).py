import oyun_modulu


def menu():
    """
    Kullanıcıya ana menüyü gösterir.
    """
    print("\n--- ŞANS OYUNLARI ---")
    print("1. Sayı Tahmin")
    print("2. Yazı-Tura")
    print("3. Skorlarım")
    print("4. Çıkış")


def main():
    """
    Programın ana kontrol fonksiyonudur.

    Kullanıcıdan isim alır ve menü üzerinden oyunları yönetir.
    """
    oyuncu = input("Oyuncu adını gir: ")

    while True:
        menu()
        secim = input("Seçim: ")

        if secim == "1":
            puan = oyun_modulu.sayi_tahmin()
            oyun_modulu.skor_kaydet(oyuncu, "Sayı Tahmin", puan)

        elif secim == "2":
            puan = oyun_modulu.yazi_tura()
            oyun_modulu.skor_kaydet(oyuncu, "Yazı-Tura", puan)

        elif secim == "3":
            oyun_modulu.skor_goster()

        elif secim == "4":
            print("Çıkılıyor...")
            break

        else:
            print("Geçersiz seçim!")


if __name__ == "__main__":
    main()