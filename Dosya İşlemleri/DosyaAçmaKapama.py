

#   open("İlkDosya.txt","w")   #Bu kodun açıklaması kısaca ben İlkdosya adında bir dosya
# oluşturmak istiyorum diyoruz ve burdaki w kipi ise eğer böyle bir doysa yoksa aç,
# var ise var olan dosyayı sil ve yeni dosya aç manasına gelir bu yüzden tehlikelidir

#   file=open("Bilgiler.txt")   #burada ise file adı ile bu dosya üzerinde işlemler yapabilriz
#file.close()#dosya işlemleri bittiğinde dosyayı kapatmak için kullanılır



#   file1=open("C:/Users/hupes/Desktop/Bilgiler.txt","w")   #yukarıdaki kullanım proje dosyasının
#bulunduğu konuma dosya açar bu kullanım ile istediğimiz yere dosya açmasını isteyebiliriz

file=open("bilgiler.txt","w",encoding="utf-8")#burada encodin="utf-8" yapmamızın sebebi türkçe
# karakterleri hata almadan kullanabilmek
file.write("Ahmet Esat Kopar Çalış abcçdei")
file.close()
open("bilgiler.txt","w",encoding="utf-8")#burada ise dosyayı tekrar açtığımız için bilgiler gidecek

file1=open("YazılanDosya.txt","a",encoding="utf-8")#buradaki a kipi ise w den farklı olarak dosyanın üzerine yazar
#eski bilgileri silmez ekleme yapabiliriz
file1.write("Ahmet Esat kopar\n")
file.close()
file1.write("Burada Yazılar Silinmicek\n")






