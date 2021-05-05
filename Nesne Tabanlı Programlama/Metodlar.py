
class Yazılımcı():

    def __init__(self,isim,soyisim,numara,maaş,diller):
        self.isim=isim
        self.soyisim=soyisim
        self.numara=numara
        self.maaş=maaş
        self.diller=diller
    def bilgilerigöster(self):#burada yeni bir metod açıp parametreyi sadece self belirledik
        #ve sınıfımızın içine bilgileri gösterecek olan bir metod tanımlamış olduk
        print("""
        
        Yazılımcı Nesnesinin Özellikleri
        
        İsim:{}
        
        Soyisim:{}
        
        Numara:{}
        
        Maaş:{}
        
        Bilinen Diller:{}
        
        """.format(self.isim,self.soyisim,self.numara,self.maaş,self.diller))
    def zamyap(self,zam_miktarı):
        print("Zam Yapılıyor...")
        self.maaş+=zam_miktarı
    def dilekle(self,dil):
        print("Dil Ekleniyor...")
        self.diller.append(dil)


yazılımcı=Yazılımcı("Ahmet Esat","Kopar",568965421,5500,["Python","Java","Kotlin","HTML","CSS"])#burada ise
#Yazılımcı sınıfından oluşturduğumuz yazılımcı nesnesine parametreleri girdik
yazılımcı.bilgilerigöster()#ve oluşturduğumuz fonksiyonu çağırdık
yazılımcı.zamyap(500)
yazılımcı.dilekle("JavaScript")
yazılımcı.bilgilerigöster()
