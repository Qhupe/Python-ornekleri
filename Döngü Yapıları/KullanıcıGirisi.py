print("""******************

Kullanıcı Girişi Programı

******************
""")


sys_kullanıcı_adı="Ahmet Esat"

sys_parola="12345"

girishakki=3

while girishakki!=0:

    kullanıcı_adı = input("Kullanıcı Adı Giriniz:")
    parola = input("Parola:")


    if(kullanıcı_adı!=sys_kullanıcı_adı and parola==sys_parola):
        print("Kullanıcı Adı Hatalı...")
        girishakki -= 1
    elif(kullanıcı_adı==sys_kullanıcı_adı and parola!=sys_parola):
        print("Parola Hatalı...")
        girishakki -= 1
    elif(kullanıcı_adı!=sys_kullanıcı_adı and parola!=sys_parola):
        print("Kullanıcı Adı Ve Parola Yanlış")
        girishakki -= 1
    else:
        print("Giriş Başarılı")
        break

