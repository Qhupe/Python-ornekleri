print("""*******************

KULLANICI GİRİŞİ

*******************
""")

sys_kullanıcı_adı = "Ahmet Esat"
sys_parola = "12345"

kullanıcı_adı = input("Kullanıcı Adı:")
parola = input("Parola:")

if (kullanıcı_adı==sys_kullanıcı_adı and parola!=sys_parola):
    print("Parola Hatalı")
elif (kullanıcı_adı!=sys_kullanıcı_adı and parola==sys_parola):
    print("Kullanıcı Adı Hatalı")
elif(kullanıcı_adı!=sys_kullanıcı_adı and parola!=sys_parola):
    print("Kullanıcı Adı ve Parola Hatalı")
else:
    print("Giriş Başarılı")

#Burada Ek olarak in operatörünü anlatalım, in operatörü girilen bir verinin karşılaştırılan
#verinin içinde olup olmadığını kontrol eder

örn1="Merhaba"

if ("Mer" in örn1):#Burada Mer kelimesinin örn1 deki Merhaba kelimesinin içinde varmı
    #sorusu soruldu ve var ise true yazıldı
    print(True)
    if("MEK" in örn1):#Burada ise MEK kelimesi ile karşılaştırıldı eğer varsa true yoksa false yazdırıldı
        print(True)
    else:
        print(False)