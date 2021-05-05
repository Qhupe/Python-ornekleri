#dosyaları okumak için r kipini yani read kipini kullanmamız gerekiyor,eğer
#r kipi ile açılmaya çalışılan dosya bulunamıyorsa FileNotFoundError hatası alırız


try:
    file = open("İlkDosya.txt", "r", encoding="utf-8")
except FileNotFoundError:
    print("Böyle Bir Dosya Bulunamadı")
"""Dosya Okumanın 1. Yöntemi"""
for i in file:
    print(i,end="")#buradaki end parametresi ile yazının sonuna ne konulması gerektiğini söyler
file.close()

"""Dosya Okumanın 2. Yöntemi read()"""

file1=open("YazılanDosya.txt", "r", encoding="utf-8")
icerik=file1.read()
print("\nDosyanın İçeriği :")
print(icerik)


"""Dosya Okumanın 3. Yöntemi  readline()--->Tek Satır Okur"""

file2=open("bilgiler.txt","r",encoding="utf-8")
print("*****************************************")
print(file2.readline())
print(file2.readline())
print(file2.readline())
print(file2.readline())
print(file2.readline())

"""Dosya Okumanın 4. Yöntemi  readlines()--->Dosya içeriğini satır satır bir dizi haline getirir"""

file3=open("dizidosya.txt","a",encoding="utf-8")
while True:
    s=input("Litfen dosyaya yazılması istenen veriyi giriniz :")
    print("Çıkmak için exit yazınız")
    if(s=="exit"):
        file3.close()
        break
    else:
        file3.write(s+"\n")


file3=open("dizidosya.txt","r",encoding="utf-8")
liste=file3.readlines()
print(liste)
file3.close()








