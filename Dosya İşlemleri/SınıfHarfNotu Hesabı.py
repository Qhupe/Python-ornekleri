
def nothesapla(satır):

    satır=satır[:-1]
    liste = satır.split(",")
    isim=liste[0]
    not1=int(liste[1])
    not2 =int(liste[2])
    not3 =int(liste[3])
    notort=not1*(3/10)+not2*(3/10)+not3*(4/10)
    if(notort<50):
        print(" {} \n 1.Vize= {} \n 2.Vize= {} \n Final= {} \n Ortalama= {} \n Harf Notu=FF \n Durumu=Kaldı \n".format(isim,not1,not2,not3,notort))
    elif(notort>=50 and notort<=60):
        print(" {} \n 1.Vize= {} \n 2.Vize= {} \n Final= {} \n Ortalama= {} \n Harf Notu=CC \n Durumu=Geçti \n".format(isim,not1,not2,not3,notort))
    elif(notort>=61 and notort<=70):
        print(" {} \n 1.Vize= {} \n 2.Vize= {} \n Final= {} \n Ortalama= {} \n Harf Notu=CB \n Durumu=Geçti \n".format(isim,not1,not2,not3,notort))
    elif (notort >= 71 and notort <= 80):
        print(" {} \n 1.Vize= {} \n 2.Vize= {} \n Final= {} \n Ortalama= {} \n Harf Notu=BB \n Durumu=Geçti \n".format(isim,not1,not2,not3,notort))

    elif(notort>=81 and notort<=90):
        print(" {} \n 1.Vize= {} \n 2.Vize= {} \n Final= {} \n Ortalama= {} \n Harf Notu=BA \n Durumu=Geçti \n".format(isim,not1,not2,not3,notort))

    else:
        print(" {} \n 1.Vize= {} \n 2.Vize= {} \n Final= {} \n Ortalama= {} \n Harf Notu=AA \n Durumu=Geçti \n".format(isim,not1,not2,not3,notort))

    print("**************Dğer Öğrenci**************")





with open("Notlar.txt","r",encoding="utf-8")as file:

    for i in file:
        nothesapla(i)















