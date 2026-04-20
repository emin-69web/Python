urunler = [
    {"ad": "SÜT", "fiyat": 35, "stok": 10},
    {"ad": "EKMEK", "fiyat": 10, "stok": 2},
    {"ad": "YUMURTA", "fiyat": 3, "stok": 15},
    {"ad": "ÇİKOLATA", "fiyat": 20, "stok": 1}
]
# for Döngüsü İle Listeleme
print("|---- MARKET ÜRÜN LİSTESİ ----|")
for urun in urunler:
    print(f"Ürün Adı: {urun['ad']} | Ürün Fiyatı: {urun['fiyat']}TL | Ürün Stoğu: {urun['stok']} Adet Mevcut")

# 3 Taneden Az Stoğu Olan Ürünlerde Uyarı Ver
print(f"\n|---- KRİTİK STOK UYARISI ----|")
for urun in urunler:
    if urun['stok'] < 3:
        print(f"{urun['ad']} Ürününün Stoğu Tükenmek Üzere (Kalan Adet = {urun['stok']})")

# Toplam Stok Bul
print("\n|---- TOPLAM STOK DEĞERİ ----|")
toplamdeger = 0
for urun in urunler:
    urundegeri = urun["fiyat"] * urun["stok"]
    toplamdeger += urundegeri
print(f"Marketin Toplam Stok Değeri = {toplamdeger}TL")