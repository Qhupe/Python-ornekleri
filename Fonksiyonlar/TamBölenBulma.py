
def tambölenbul(sayi):
    TamBölenler= []

    for i in range(2,sayi):

        if (sayi % i==0):
            TamBölenler.append(i)
    return TamBölenler

while True:

    sayi=input("Sayı :")

    if(sayi=="q"):
        print("Çıkış Yapılıyor...")
    else:
        sayi=int(sayi)
        print("Tam Bölenler",tambölenbul(sayi))

