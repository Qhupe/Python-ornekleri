
"""
**********************************Overriding**********************************
eğer biz miras aldığımız metodları aynı isimle miras alınan sınıfada tanımlarsak artık
metodu çağırdığımız zaman kendi sınıfımızda tanımladığımız fonksiyon çalışacaktır
böylelikle miras alınan sınıfa yeni özellikler ekleyebiliriz

"""

class Çalışan():

    def __init__(self,isim,maaş,departman):
        print("Çalışan Sınıfının init fonksiyonu")
        self.isim=isim
        self.maaş=maaş
        self.departman=departman

    def bilgilerigöster(self):
        print("Çalışan Sınıfının bilgileri...")

        print(" İsim : {}\n Maaş : {}\n Departman : {}\n".format(self.isim,self.maaş,self.departman))

    def departman_degistir(self,yenidepartman):
        self.departman = yenidepartman


class Yönetici(Çalışan):
    def __init__(self,isim,maaş,departman,kişisayısı):#Burada gördüğünüz gibi Çalışan
     #sınıfını miras almamıza rağmen yeni bir init fonksiyonu yazdık yani overriding
     #işlemi yaptık çünkü eğer çalışan sınıfının init fonksiyonunu kullansaydık yönetici
     #sınıfına yeni parametreler ekleyemeyecektik böylelikle hem Çalışan sınıfının hemde
     #yönetici sınıfının özelliklerine ulaşabilir olduk
        print("Yönetici Sınıfının init fonksiyonu")

        self.isim = isim
        self.maaş = maaş
        self.departman = departman
        self.kişisayisi=kişisayısı

    def zamyap(self,zam_miktarı):
        self.maaş+=zam_miktarı

yönetici=Yönetici("Utku Bayrak",4500,"Tasarım",6)
yönetici.bilgilerigöster()









