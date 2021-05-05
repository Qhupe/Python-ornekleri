# Mantıksal Değerler (Boolean) bir veri tipi olup iki değere sahiptirler
# True ve False değerleri alan değişkenlerdir

a = True
b = False
print(type(a), type(b)) # satır çalıştığında tip olarak bool çıktısı alacağız

#Pythonda bir sayı değeri 0 dan farklı olduğu sürece true değeri dönderir
print(bool(14),bool(-5),bool(0.5))
print(bool(0),bool(0.0))

#Eğer Pythonda bir değişkenin değerini sonradan belirllemek isterseniz geçici olarak
#bu değişkebe None(atanmamış anlamında) değerine eşitleyebilirsiniz

a = None # henüz değer atanmadı
print(a)
a =4 # Şimdi değer atıyoruz
print(a)

yaş=int(input("Yaşınızı Giriniz:"))

if yaş<18:
    print("Bu Mekana Giremezsiniz")
else:
    print("Yaşınız Mekana Girmek İçin Yeterli")
    
