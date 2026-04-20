karakterler = [
    {"isim": "Aragorn",   "sinif": "savasci", "seviye": 15, "hp": 220, "altin": 500},
    {"isim": "Gandalf",   "sinif": "buyucu",  "seviye": 20, "hp": 140, "altin": 300},
    {"isim": "Legolas",   "sinif": "okcu",    "seviye": 12, "hp": 160, "altin": 550},
    {"isim": "Gimli",     "sinif": "savasci", "seviye": 10, "hp": 200, "altin": 600},
    {"isim": "Thranduil", "sinif": "okcu",    "seviye": 14, "hp": 175, "altin": 900},
    {"isim": "Saruman",   "sinif": "buyucu",  "seviye": 18, "hp": 130, "altin": 800}
]

okcu_mu = lambda k: k["sinif"] == "okcu"
guclu_mu = lambda k: k["seviye"] > 10 and k["hp"] > 150

seviye_15_ustu = [k["isim"] for k in karakterler if k["seviye"] > 15]
zenginlik_durumu = [(k["isim"], "Zengin" if k["altin"] > 500 else "Fakir") for k in karakterler]

print("--- Legolas Bilgi ---")
ornek_karakter = karakterler[2]
print(f"{ornek_karakter['isim']} Okçu mu ?: {okcu_mu(ornek_karakter)}")
print(f"{ornek_karakter['isim']} Güçlü mü ?: {guclu_mu(ornek_karakter)}")

print("\n--- Karakter Bilgileri ---")
print(f"* Seviyesi 15'ten Büyük Olanlar: \n{seviye_15_ustu}")
print("* Karakterlerin Zenginlik Durumları:")
for durum in zenginlik_durumu:
    print(durum)