"""
 Inharitance yani kalıtım konusuna gelirsek bunu gerçek hayattaki miras
 veya gen mantığına benzetebilriz nasılsa annemizden ve babamızdan
 davranış yüz şekli göz rengi gibi genetik özellikleri miras olarak alıyorsak
 burdada nesneler birbirine miras olarak bırakabilir
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
    def zamyap(self,zam_miktarı):
        self.maaş+=zam_miktarı

yönetici=Yönetici("Ahmet Esat Kopar",3500,"Tasarım")#burada Yönetici sınıfını tanımlarken
#Çalışan sınıfını miras olarak aldığımız için isim,maaş ve departman gönderdiğimizde
#hata almadan kullanabildik
yönetici.bilgilerigöster()
yönetici.departman_degistir("Yazılım")
yönetici.bilgilerigöster()

yönetici1=Yönetici("Batuhan Önder",5000,"Planlama")
yönetici1.bilgilerigöster()
yönetici1.zamyap(500)
yönetici1.departman_degistir("Yönetim")
yönetici1.bilgilerigöster()





