print("""******************

ATM Makinesi

İşlemler:

1.Bakiye Sorgulama

2.Para Yatırma

3.Para Çekme

Programdan Çıkmak İçin 'q' ya Basınız

******************
""")

bakiye = 1000

while True:
    işlem =input("İşlem Seçiniz:")

    if (işlem=="q"):
        print("Güle Güle")
        break
    elif(işlem=="1"):
        print("Bakiyeniz {} TL'dir".format(bakiye))
    elif(işlem=="2"):
        yatırmik=int(input("Yatırılacak Miktarı Giriniz:"))
        bakiye+=yatırmik
        print("Yeni Bakiye {}".format(bakiye))
    elif(işlem=="3"):
        çekmik=int(input("Çekilecek Miktarı Giriniz:"))
        if(çekmik>bakiye):
            print("Bakiye Yetersiz")
        elif(çekmik==0):
            print("0'dan Farklı Bir Miktar Girin:")
        elif(çekmik<0):
            print("Çekilecek Miktar 0'dan Küçük Olamaz")
        else:
            bakiye-=çekmik
            print("Yeni Bakiye {}".format(bakiye))

    else:
        print("Hatalı İşlem Girdiniz")



