print("""******************
Hesap Mainesi Programı

İşlemler

1. Toplama İşlemi

2. Çıkarma İşlemi

3. Çarpma İşlemi

4. Bölme İşemi


******************

""")

sayi1= int(input("1. Sayıyı Giriniz:"))
sayi2= int(input("2. Sayıyı Giriniz:"))

islem=input("İşlemi Giriniz")

if islem == "1":
    print("{} ile {} in toplamı {} dir".format(sayi1,sayi2,sayi1+sayi2))

elif islem == "2":
        print("{} ile {} in Farkı {} dir".format(sayi1, sayi2, sayi1 - sayi2))

elif     islem == "3":
            print("{} ile {} in çarpımı {} dir".format(sayi1, sayi2, sayi1 * sayi2))

elif islem == "4":
                print("{} ile {} in bölümü {} dir".format(sayi1, sayi2, sayi1 / sayi2))
else:
    print("***Geçersiz İşlem***")

