print("Oyuncu Kaydetme Programı")

ad = input("Oyuncunun Adı:")
soyad = input("Oyuncun Soyadı:")
takım = input("Oyuncunun Takımı:")

bilgiler = [ad,soyad,takım]

print("Bilgiler Kaydediliyor...")

print("Oyuncu Adı: {} \nOyuncunun Soyadı: {}\nOyuncunun Takımı: {}\n".format(bilgiler[0],bilgiler[1],bilgiler[2]))