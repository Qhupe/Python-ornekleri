def selamla(isim = "İsimsiz"):#Burada ise eğer parametre girilmez ise varsayılan bir parametre ekledik
    print("Selam  :",isim)
selamla("Ahmet")#parametre girilirse isimsiz yerine ahmet geçecek
selamla()#parametre girilmezse isismsiz olarak çıktı verecek

def bilgileriGoster(ad="Bilgi Girilmedi",soyad="Bilgi Girilmedi",numara="Bilgi Girilmedi"):
    print("\nAdı :",ad,"\nSoyadı :",soyad,"\nNumarası :",numara)

bilgileriGoster("Ahmet Esat","Kopar","180260051")
bilgileriGoster(soyad="Kopar",numara="180260051")#burada ise sadece girmek istediğimiz bilgileri girerek parametre gönderdik


"""****************************************Esnek Sayıda Değerler****************************************"""

def toplama(a,b,c):
    print(a+b+c)

toplama(5,6,12)
#toplama((6,2,78,21) burda fazladan parametre girdiğimiz için hata verecektir bu yüzden esnek sayıda değerler kullanırız

def toplama1(*a):
    toplam=0
    for i in a:
        toplam+= i
    print(toplam)

toplama1(5,9,1)#burada fonksiyonuı tanımlarken a* işareti grilen değerleri touple olarak hafızada tutacaktır
#içerisindeki for döngüsü ile eleanlar arası gezinip bunları toplayabildik

"""****************************************Global ve Yerel Değişkenler****************************************"""

#Burada ise Global ve yerel değişkenlere göz atacağız nedir ne değildir bundan bahsedeceğiz
"""

Pythonda değişkenlerin sınıfların ve fonksiyonların bir kapsamı bulunur kapsama alanı gibi düşünelim
fonksiyonlara tanımlanan değişkenler yerel değişkenlerdir ve sadece fonskiyon içinde tanımlıdırlar
fonksiyon dışında aslında böyle bir değişken yoktur eğer biz bir değişkeni bütün fonksiyonlarda kullanmak
istiyorsak Global olarak tanımlamamız gerekir

"""

sayiglobal=77#Burada Tüm fonksiyonların dışında tanımladığımız değişken ise global değişkendir

def fonksiyon():
    sayi=25#Bir yerel değişkendir fonksiyon dışında kullanılamaz
    print(sayi+25)

def fonkglobal():
    print(sayiglobal)#gördüğünüz gibi fonksiyo içinde ve dışında erişilebilmesi mümkündür


def çıkarma():
    sayiglobal=51#burada ise fonksiyon içinde sayiglobali 51e eşitlediğimiz için aslında yerelde
    #yeni bir sayiglobal değişkeni tanımlamış olduk yani programda yerel ve global olmak üzere 2
    #adet sayiglobal değişkeni mevcut oldu
    print(sayiglobal-2)#burda alacağı değer ise 51-2 olur yerelde tanımlanan değişkeni kapsar
çıkarma()#çıktısı 49
print(sayiglobal)#çıktısı 77 olur


def çarpglobal():
    global sayiglobal#burada ise yerelde tanımlamak istemediğimizi global olan değer üzerinden işlem yapmak
    #istediğimizi belirttik
    sayiglobal*=3#yani burada 77*3 değeri oluştu ve yeni sayiglobal değerimizi 231 oldu
    print(sayiglobal)
çarpglobal()
print(sayiglobal)#yukarıdaki fonksiyonda global olan sayiglobal değeri üzerinden işlem yaptığımız için
#77 değeri artık 231 olarak değişti
