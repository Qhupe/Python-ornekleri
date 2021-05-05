""""******************************LAMBDA İFADELERİ******************************"""
"""Lambda ifadeleri fonksiyon oluşturmak için kullanılan pratik bir yöntemdir"""

liste1 = [5,6,3,4,8,2]#burada normal bir liste tanımlama yöntemi ile liste 1 i oluşturduk

liste2 = [i * 2 for i in liste1]#burada ise liste 1'in bütün elemanlarının x2 olacak şekilde liste 2 yi oluşturduk

print(liste1)
print(liste2)

def ikiyleçarp(a):#normal bir fonksiyon tanımı ile girilen sayıyı 2 ile çarpıp gönderen bir fonk tanımladık
    return a*2
print(ikiyleçarp(8))

ikileböl = lambda a:a/2#Burada ise aynı fonksiyonun bölümlü olanını lambda ile tanımladık burada return manasını
#taşıyan kod ise a/2 oluyor : öncesi a ise alnıan parametreyi ifade eder

print(ikileböl(589))

toplama = lambda a,b,c,e : a+b+c+e#burada mesela 4 parametreli bir toplama ifadesi tanımladık

print(toplama(8,12,65,20))

terscevir = lambda s:s[::-1] # burada ise tek parametre alan bir lambda ifadesi tanımladık ve alınan parametreyi
#ters çevirilmiş halini geri dönderme emrini verdik
print(terscevir("Ahmet Esat Kopar"))# Çıktısı 'rapoK tasE temhA' olacaktır

çiftbul = lambda x:x%2==0

print(çiftbul(49))
print(çiftbul(52))





