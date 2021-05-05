try:
    a=int("AhmEtPython56982")#burada inte çevirmek istediğimiz değerde string
    # ifadeler olduğu için hata verecektir fakat burada program hatayı görünce
    print("Program Burada")
except:#otomatik olarak bir except bloğu arar ve orayı çalıştırır fakat hata vermezse
       #herhangi bir except bloğuna girmeyecektir
    print("Bir Hata Oluştu")




try:
    b=int("AhmEtPython56982")#
    print("Program Burada")
except ValueError:#Burada ise hata türünü belirttik böyle bir kullanımda ise sadece
    #value Error olduğu durumda bu except bloğuna gidecek
    print("Bir Hata Oluştu")


try:
    b=5/0#burada zero division error vermesi gerek
    print("Program Burada")
except ValueError:#yukarıda zero division error vereceği için ve bu except bloğu ise
    #valu error tanımlı olduğu için bu blok çalışmayacaktır
    print("Bir Hata Oluştu")

except ZeroDivisionError:#program yukarıdaki except bloğuna gitmeyecek buraya gelecektir
    print("Bir Sayı Sıfıra Bölünemez")# çıktı olarak bunu göreceğiz
print("Bloklar Sona Erdi")


try:
    sayi = int(input("Lütfen Sayı Giriniz :"))
    sayi1 = int(input("Lütfen Diğer Sayıyı Giriniz :"))
    print(sayi/sayi1)
except ValueError:
    print("Lütfen Sayıyı doğru girin")
except ZeroDivisionError:
    print("Bir Sayı Sıfıra Bölünemez")
print("Program sona erdi")

def terscevir(s):
    if (type(s)!= str):
        raise ValueError("Lütfen String Bir İfade Girin")#burada ise program eğer str bir
    #veri girilmemişse hata vermesini ve hata mesajında istediğimiz şeyin çıktı verilmesini
    #sağladık bu olaya hata fırlatma denir
    else:
        return s[::-1]
print(terscevir("Python"))
print(terscevir(589652))







