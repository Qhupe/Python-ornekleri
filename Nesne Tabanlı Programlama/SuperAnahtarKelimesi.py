"""***************************Süper Anahtar Kelimesi***************************"""
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
    def __init__(self,isim,maaş,departman,kişisayısı):#burada ise yukarıdaki isim maaş departman
        #verilerini kullanmak istediğimizi söyledik ve self ile bunları alt tarafta
        super().__init__(isim,maaş,departman)
        print("Yönetici Sınıfının init fonksiyonu")

        self.kişisayisi=kişisayısı#burada tanımlamaya ihtiyaç duymadık

    def bilgilerigöster(self):
        print("Yönetici Sınıfının bilgileri...")
        print(" İsim : {}\n Maaş : {}\n Departman : {}\n Sorumlu Kişi Sayısı {}".format(self.isim,self.maaş,self.departman,self.kişisayisi))


    def zamyap(self,zam_miktarı):
        self.maaş+=zam_miktarı

yönetici=Yönetici("Utku Bayrak",4500,"Tasarım",6)
yönetici.bilgilerigöster()