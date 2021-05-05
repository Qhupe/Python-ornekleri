"""
Özel Metodlar bizim özel olarak çağırmadığımız fakat her classa ait metodlardır
bunların çoğu varsayılan olarak tanımlanır bazı durumlarda biz özel olarak
tanımlamalıyız
"""

class Kitap():
    pass

kitap=Kitap()#Burada mesela init metodu python tarafından direkt tanımlı olarak çağırıldı
print(kitap)#burada ise otomatik olarak str metodu çalışır ve python kendi ekrana yazdırır
#buradaki __str__ fonksiyonu ekrana '<__main__.Kitap object at 0x00000240C4966FD0>' çıktısını verir

#len(kitap) burada len fonksiyonu kitap sınıfına tanımlı olmadığı için hata verecektir

del kitap #burada ise __del__ metodu python tarafından çağırılarak kitap nesnesi silinir

class Kitap1():

     def __init__(self,isim,yazar,sayfasayisi,tür):
         print("İnit Fonksiyonu")
         self.isim=isim
         self.yazar=yazar
         self.sayfasayisi=sayfasayisi
         self.tür=tür
     def __str__(self):#burada ise __str__ metodudnu kendimiz tanımladık ve diziyi direkt
         #ekrana bastırdığımızda istediğimiz yazının çıkmasını sağladık
         return " İsim :{}\n Yazar :{}\n Sayfa Sayısı :{}\n Türü :{}".format(self.isim,self.yazar,self.sayfasayisi,self.tür)
     def __len__(self):#burada ise Kitap1 sınıfına bir len metodu tanımladık ve bu
         #metoddan ona sayfa sayısını geri döndermesini istedik
         return self.sayfasayisi

     def __del__(self):
         print("kitap Objesi Siliniyor...")
         #burada ise del metodunu değiştirmedik birlikte kullandık gibi oldu
         #del metodunu ve vb metodları değiştiremeyiz sadece onlara yeni özellikler ekleriz

kitap=Kitap1("Satranç","Stefan Zweig",85,"Hikaye")
print(kitap)
print("",len(kitap))#burada ise tanımladığımız len metodunu ekrana yazdırdığımızda ise
#sayfa sayısı ekrana yazdırılıcaktır
del kitap



