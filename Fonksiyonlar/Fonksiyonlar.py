"""
Fonksiyonlar Programlamada belirli işlevleri olan ve terkrar tekrar kullandığımız
yapılardır,print() bir fonksiyondur ve içine gönderilen değeri ekrana yazdırır

programalamacıda kendi fonksiyonlarını def anahtar kelimesi ile yazabilir

def fonksiyonAdi(parametre1,parametre2,...(opsiyonel))

"""

def selamla():
    print("Merhaba")
    print("Nasılsınız")

print(type(selamla))

selamla()#parametresiz fonksiyon olduğu için içeri parametre yazmadık

def selamver(isim):#Burada ise parametre alan bir fonksiyon yazdık

    print("Adınız:",isim)

isim=input("İsminizi Giriniz :")#burada isim olarak bir klavye girişi aldık
selamver(isim)#ve aldığımızı girişi fonksiyonumuza parametro olarak gönderdik

def faktöriyel (sayi):
    faktöriyel=1
    if (sayi==0 or sayi==1):
        print("Faktöriyel =",faktöriyel)
    else:
        while(sayi>=1):
            faktöriyel*=sayi
            sayi-=1

    return faktöriyel #burada ise faktöriyel değerini geri dönderdik buna ayrıca değineceğiz

sayi=int(input("Faktöriyeli Alınacak Sayıyı Giriniz:"))
print(faktöriyel(sayi))


