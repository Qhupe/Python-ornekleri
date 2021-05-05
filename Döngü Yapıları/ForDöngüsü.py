toplam=0
sayac=0
liste =[1,2,3,4,5,6,7,8]
s = "Python"
for eleman in liste:#burada ise in parametresi listede gezinmemize yardımcı oluyo
                    toplam  = toplam+eleman
                    sayac=sayac+1

                    if (eleman%2==0):#burada ise gezindiğimiz elemanın 2 ile bölümünden kalanı kontrol
                                     #edip çift mi tek mi ekrana yazdırıyoruz
                        print(eleman," Sayısı Çift Sayı")
                    else:
                        print(eleman,"Saysı Tek Sayı")

print("Toplam {} Eleman {}".format(toplam,eleman))

print(toplam)
for i in s:#burada ise bir string içinde karakter karakter gezebileceğimizi gördük
            print(i)

            liste1=[(1,2),(3,4),(5,6),(7,8)]
for i in liste1:
    print(i)

