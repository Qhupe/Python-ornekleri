import random
import time

class Kumanda():

    def __init__(self,tvDurum="Kapalı",tvSes=0,kanalListesi=["TRT"],kanal="TRT"):

        self.tvDurum=tvDurum
        self.tvSes=tvSes
        self.kanalListesi=kanalListesi
        self.kanal=kanal

    def tvAc(self):

        if(self.tvDurum=="Açık"):
            print("Televizyon Zaten Açık")
        else:
            print("Televizyon Açılıyor...")
            self.tvDurum="Açık"

    def tvKapat(self):

        if(self.tvDurum=="Kapalı"):
            print("Televizyon Zaten Kapalı")
        else:
            print("Televizyon Kapanıyor...")
            self.tvDurum="Kapalı"

    def sesAyar(self):

        while True:
            cevap=input("Sesi Azalt : -\n Sesi Arttır : +\n Çıkış için : 0")


            if(cevap=="-"):
                if(self.tvSes!=0):
                    self.tvSes-=1
                    print("Ses Seviyesi :",self.tvSes)
            elif(cevap=="+"):
                if(self.tvSes!=40):
                 self.tvSes+=1
                 print("Ses Seviyesi :", self.tvSes)
            elif(cevap=="0"):
                break
            else:
                print("Ses Seviyesi :",self.tvSes)

    def kanalEkle(self,kanalİsmi):
        print("Kanal Ekleniyor...")
        self.kanalListesi.append(kanalİsmi)
        time.sleep(1)
        print(kanalİsmi,"Kanalı Eklendi")

    def rastgeleKanal(self):

        rastgele =random.randint(0,len(self.kanalListesi)-1)

        self.kanal=self.kanalListesi[rastgele]

        print("Kanal :",self.kanal)

    def __len__(self):
        return len(self.kanalListesi)

    def __str__(self):
        return "Tv Durumu : {}\n Ses Seviyesi : {}\n Kanal Listesi : {}\n Kanal : {}"\
            .format(self.tvDurum,self.tvSes,self.kanalListesi,self.kanal)


kumanda=Kumanda()

print("""
********************Televizyon Uygulaması********************
1-Tv Aç

2-Tv Kapat

3-Ses Seviyesi

4-Kanal Ekleme

5-Kanal Sayısı

6-Rastgele Kanal

7-Televizyon Bilgileri

0-Çıkış

*************************************************************
""")

while True:

    işlem=int(input("İşlemi Seçiniz"))

    if(işlem==0):
        print("Program Sonlandırılıyor...")
        time.sleep(1)
        print("Program Sonlandı")
        break
    elif(işlem==1):
        kumanda.tvAc()
    elif(işlem==2):
        kumanda.tvKapat()
    elif(işlem==3):
        kumanda.sesAyar()
    elif(işlem==4):
        kanalİsmi=input("Kanal İsimlerini '-' ile ayırarak giriniz :")
        kanalListesi=kanalİsmi.split("-")

        for eklenecekler in kanalListesi:
            kumanda.kanalEkle(eklenecekler)

    elif(işlem==5):

        print("Kanal Sayısı :",len(kumanda))
    elif(işlem==6):
        kumanda.rastgeleKanal()
    elif(işlem==7):
        print(kumanda)
    else:
        print("Geçersiz İşlem")











