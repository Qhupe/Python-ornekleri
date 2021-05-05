"""
2. Dereceden Bir Bilinmeyenli Denklem Kökleri Bulma

Denklem = ax^2 + bx + c

Delta= b^2 - 4*a*c

Birinci Kök : (-b - Delta ** 0,5)/(2*a)
İkinci Kök : (-b + Delta ** 0,5)/(2*a)

"""

a = int(input("a Katsayısını Giriniz:"))
b = int(input("b Katsayısını Giriniz:"))
c = int(input("c Katsayısnı Giriniz:"))

denklem=str(a)+"X^2+"+str(b)+"x+"+str(c)
print("Denklem",denklem)

delta=b**2 - 4*a*c;
print("Delta:",delta)

kökbir= (-b-delta**0.5)/(2*a)
kökiki= (-b+delta**0.5)/(2*a)

print("Birinci Kök =",kökbir)
print("İkinci Kök =",kökiki)