"""
Metod: Metodlar bir obje üzerinde belirli işleri gerçekleştiren objelere özgü
fonksiyonlardır

"""

liste=[1,2,3,4,5,"Ahmet","Python"]
type(liste)
liste.insert(1,"Kopar")#insert() bir metottur ve ve girilen yere girilen veriyi ekler
liste.append("Java")#append() bir metottur ve girilen veriyi listenin sonuna ekler
print(liste)
liste.pop()#metodu ise bir girdi almaz ve listenin son elemanını siler
help(liste.append)#help()ise içine azılan petodud ne iş yaptığını açıklar

