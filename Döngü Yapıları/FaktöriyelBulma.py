print("""**************************

Faktöriyel Bulma

Çıkmak İçin 'q' ya basınız

**************************
""")


while True:
    sayi =input("Faktöriyeli Bulunacak Sayıyı Giriniz:")
    if(sayi=="q"):
        print("Program Sonlandırılıyor...")
        break

    else:
        sayi =int(sayi)

        faktöriyel = 1

        for i in range(2,sayi+1):
            faktöriyel*=i
    print("Faktöriyel ",faktöriyel)#Eğer Sürekli Yazılmasını istemiyorsak döngü hizasının dışına yazılmalı
