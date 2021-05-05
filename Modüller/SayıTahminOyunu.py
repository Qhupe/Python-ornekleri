import random
import time

print("""*****************************

Sayı Tahmin Oyunu

1 ile 40 arasında sayıyı tahmin edin

*****************************
""")

rastgele_sayi=random.randint(1,40)

hak = 5
while True:
    tahmin=int(input("SAyıyı Tahmin Edin :"))

    if(tahmin<rastgele_sayi):
        print("Cevap Analiz Ediliyor...")
        time.sleep(1)
        print("Tahmininizi Arttırın")
        hak-=1
    elif(tahmin>rastgele_sayi):
        print("Cevap Analiz Ediliyor...")
        time.sleep(1)
        print("Tahmininizi Azaltın")
        hak-=1
    else:
        print("Cevap Analiz Ediliyor...")
        time.sleep(1)
        print("Tebrikler Tahmininiz Doğru\nSayı=",rastgele_sayi)
        break
    if (hak==0):
        print("Hakkınız Bitti Tekrar Deneyin")
        print("Sayı =",rastgele_sayi)
        devam=input("Tekrar Denemek için 1 çıkış yapmak için 0 giriniz")
        if(devam=="0"):
            break
        elif(devam=="1"):
            rastgele_sayi=random.randint(1,40)
        else:
            print("Yanlış giriş Yaptınız")
            break








