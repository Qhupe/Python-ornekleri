import math #Burada kullanmak istediğimiz modülü import ederek programa dahil ettik

print(math.factorial(13))#math modülünün içinden faktöriyel fonksiyonunu direkt kullanabilriz
print(math.pow(3,5))#burada ise math modülünün içinden pow yani üs fonksiyonunu çağırdık
print(math.log(3,9))
print(math.ceil(5.1))# yukarı yuvarlama fonksiyonu


import math as matematik #burada ise modülü tanımladık ve modülün ismini değiştirdik

print(matematik.pow(5,6))
print(matematik.ceil(6.2))
print(matematik.pi)

from math import * #bu kullanımda ise herhangi bir isim gerekmeden her bir fonksiyonu direkt
#programa tanımlamış oluyoruz

print(factorial(9))
print(pow(3,4))
print(sqrt(8))

# from math import floor,ceil --> burdaki kullanım ise sadece istenilen fonksiyonları programa tanımlar

"""**************************Kendi Modüllerimizi Yazma**************************"""
"""
1.İlk olarak bir klasör oluşturuyoruz
2.Modülümüz ve deneme python dosyamız aynı dizinde olması gerektiği için 2 tane
python dosyasını da bu klasör altına oluşturuyoruz
3.modul1.py ve deneme.py dosyası oluşturuyoruz
4.modul1.py dosyasının içine istediğimiz kadar fonksiyon yazıyoruz
5.son olarak deneme.py dosyasının içinde bu modül1.py modülünü kopyalıyoruz

* yazdığımız modülü her yerde kullanmak için Python39/Lib klasörünün altına atmanız
yeterli olacaktır

"""


