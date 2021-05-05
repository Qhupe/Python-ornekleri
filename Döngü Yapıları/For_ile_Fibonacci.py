"""Fibonacci Serisi"""

a=1
b=1

fibonacci = [a,b]
adım=int(input("Kaç Fibonacci Adımı Oluşturulacağını Giriniz:"))

for i in range(adım):
    print("a: ",a, "b: ",b)

    a,b=b,a+b
    fibonacci.append(b)

print(fibonacci)
