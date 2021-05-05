# with open metodu ise içerisine yazılan kod blokları bittiğinde otomatik sonlanır
#yani dosya otomatik ollarak kapanır
with open("bilgiler.txt","r",encoding="utf-8") as file:
    for i in file:
        print(i)

print("*******************************************")
"""
biz file yani dosya imlecini istediğimiz yere götürmek istersek seek() fonksiyonunu
kullanıcaz fakat dosyanın hangi imlecte olduğunu görmek için tell() fonksiyonunu 
kullanmamız gerekecek
"""
with open("bilgiler.txt","r",encoding="utf-8") as file:
   liste=file.readlines()
   for i in range(len(liste)):
        s=liste[i]
        print(s[::-1])












