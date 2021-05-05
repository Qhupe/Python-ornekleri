

with open("YazılanDosya.txt","r+",encoding="utf8") as file:#burada r+ tanımladığımız
    #yer ise hem okuma hemde write ile yazma yapmamızı sağlar
    print(file.read())


with open("YazılanDosya.txt","r+",encoding="utf8") as file:
    file.seek(10)#10. byte temsil ediyor
    file.write("Deneme")
print("**************************************************")
with open("YazılanDosya.txt", "r+", encoding="utf8") as file:
    print(file.read())

print("*********Sona Ekleme*********")

with open("YazılanDosya.txt","a",encoding="utf-8")as file:
    file.write("Yeni En Sonasd")

with open("YazılanDosya.txt","r",encoding="utf-8")as file:
    print(file.read())

print("*********başa Ekleme*********")


with open("YazılanDosya.txt","r+",encoding="utf-8")as file:
    icerik= file.read()
    icerik="Mehmet Keper\n"+icerik
    file.seek(0)
    file.write(icerik)

with open("YazılanDosya.txt", "r+", encoding="utf-8")as file:
    print(file.read())




print("*********Ortaya Ekleme*********")

with open("YazılanDosya.txt", "r+", encoding="utf-8")as file:
    liste=file.readlines()
    print(liste)
    liste.insert(int(len(liste)/2),"Burası Ortası\n")
    for i in liste:
        file.write(i)


with open("YazılanDosya.txt", "r+", encoding="utf-8")as file:
    print(file.read())





