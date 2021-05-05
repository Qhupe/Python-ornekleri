def toplama(a,b,c):
    toplam=a+b+c
    print("Toplamları =",toplam)
    return toplam #Eğer toplam değerini geri döndürmeseydik 12. satırdaki işlem
                  #hata verecekti çünkü toplama nontype olarak görünecekti


def ikiilecarp(a):
    return a*2

toplama=toplama(2,4,9)
print(ikiilecarp(toplama))

def üçleçarp(a):
    print("1.Fonksiyon Çalıştı")
    return a*3

def besletopla(a):
    print("2.Fonksiyon Çalıştı")
    return a+5
def mod6bul(a):
    print("3.Fonksiyon Çalıştı")
    return a%6

#print(mod6bul(69))
#print(besletopla(56))
#print(üçleçarp(77))
print(mod6bul(besletopla(üçleçarp(53))))
