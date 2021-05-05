class Araba():# burada araba adında bir sınıf oluşturduk ve arabanın özelliklerini
              #sınıfa tanımladık
    marka="Nissan Qasqahi"
    model="2012 plat"
    beygir= 96
    renk="Beyaz"

araba1=Araba()#burada ise araba sınıfından araba1 isimli yeni bir nesne oluşturduk
print(araba1)#ve ekrana yazdırdığımızda araba sınıfından bir nesne olduğunu gördük
araba2=Araba()#burada ise Araba sınıfından araba2 isminde yeni bir nesne oluşturduk
araba2.model="2016"
araba2.renk="Siyah"
araba2.marka="Fiat Freemont"
araba2.beygir=140
#ve araba2 nesnesinin özelliklerini değiştirdik

print(araba2.marka)#ekrana araba2 nesnesinin markasını yazdırdığımızda ise alacağımız
#çıktı Fiat freemont olmalıdır çünkü araba2 nesnesinin markasını değiştirmiştik


print(dir(Araba))#burda alacağımız çıktıda ise Araba sınıfına kendi tanımladığımız
# değişkenler ve pythonun otomatik olarak deffoult değer atadığı veriler değişkenler olacaktır


class Araba1():
    def __init__(self,model="Bilgi Yok",renk="Bilgi Yok",beygir="Bilgi Yok",marka="Bilgi Yok"):#burada init metodunu yazdık nedir bu init metodu: burada init metodu
        #Yapıcı constructor fonksiyon olarak tanımlanır bu metod objeler oluşturulurken otomatik
        # olarak çağırılır, self ise tanımlanan sınıftaki nesne özelliklerine erişimde kullanılır
        print("init fonksiyonu çağırıldı")
        self.model=model
        self.marka=marka
        self.renk=renk
        self.beygir=beygir


araba3=Araba1("2020","Kırmızı",120,"Renault")
araba4=Araba1("2021","Beyaz",96,"Peugeot")

print("1.Arabanın Markası :",araba3.marka," 2.Arabanın Markası :",araba4.marka)
araba5=Araba1(beygir=130)#burada araba5 nesnesinin sadece beygir gücüne özellik tanıttık
print(araba5.marka)#burada ise araba5 nesnesinin markasına bir şet atamadığımız için
#tanımlı olan Bilgi Yok yazısı gelecektir
print(araba5.renk)
print(araba5.beygir)#buradada tanıttığımız beygir gücü ekrana yazılacaktır

