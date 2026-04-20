def uzunluk_kontrol(sifre):
    return len(sifre) >= 8

def buyuk_harf_kontrol(sifre):
    for karakter in sifre:
        if karakter.isupper():
            return True
    return False

def kucuk_harf_kontrol(sifre):
    for karakter in sifre:
        if karakter.islower():
            return True
    return False

def rakam_kontrol(sifre):
    for karakter in sifre:
        if karakter.isdigit():
            return True
    return False

def sifre_kontrol(sifre):

    eksikler = []
    
    if not uzunluk_kontrol(sifre):
        eksikler.append("En az 8 karakter uzunluğunda olmalıdır.")
        
    if not buyuk_harf_kontrol(sifre):
        eksikler.append("En az 1 büyük harf içermelidir.")
        
    if not kucuk_harf_kontrol(sifre):
        eksikler.append("En az 1 küçük harf içermelidir.")
        
    if not rakam_kontrol(sifre):
        eksikler.append("En az 1 rakam içermelidir.")
        
    return eksikler

if _name_ == "_main_":
    kullanici_sifresi = input("Lütfen bir şifre giriniz: ")
    
    eksik_kurallar = sifre_kontrol(kullanici_sifresi)
    
    if len(eksik_kurallar) == 0:
        print("Şifre Geçerli")
    else:
        print("Geçerli Değil")
        print("Şifrenizde eksik olan kurallar şunlardır:")
        for kural in eksik_kurallar:
            print("-", kural)