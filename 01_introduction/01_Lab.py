from builtins import print

# Değişken nedir
# Algoritma konusunda çalışırken kutulara benzetmiştik . Kullanıcıdan alınan değeri depoladığımız şeylerdir.
#ya da sabit olarak bizim için değer tutan yapılardı.

# Diğer programlama dillerinde bir değişken tnaımlarken ilk önce ilgili değişkenin tutacağı değere göre bir tip geçilir.
# Örneğin;
# int x = 5;

# Pythonda değişken tanımlama diğre programlama dillerinde olduğu gibi tip belirtmiyoruz. Pythonda değişkenler su gibidir. Nasıl ki su girdiği kabın
# şeklini alıyorsa pythonda'da değişkene atılan değerin tipini alır.
#
# x=5
# print(x) # pytrhonda built-in fonksiyonudur. yani python'ın çekirdek dosyasına gömülmüş bir fonksiyonudur.
# # fonksiyon => üzerine bir görev atanmış yapılardır. istediğimz yerde istediğimiz kadar çağırıp kullanabiliriz.
# print(type(x)) # type () built-in bir fonksiyondur. içerisine verdiğimiz değerin tipini yazar
# x = "Mike Tyson"
# print(x)
# print(type(x))
# x = True
# print(x)
# print(type(x))
# x = 12.9
# print(x)
# print(type(x))

# Kullanıcıdan 2 adet sayı alalım ve temel 4 işlem yapalım
# x = int(input("Lütfen bir sayı giriniz: "))
# y = int(input("Lütfen bir sayı giriniz: "))

# işlemin sonucunu ne zaman değişkene atamalıyım?
# toplam = x + y
# cikarma = x - y
# carpma = x * y
# bolme = x / y
# print(f'Toplama Sonuç: {toplam}')
# print(f'Sonuç: ', toplam)
# print('Sonuç: {}'.format(toplam))
# print('{} + {} = {}'.format(x, y, toplam))
# print(f'Çıkarma Sonuç: {cikarma}')
# print(f'Çarpma Sonuç: {carpma}')
# print(f'Bölme Sonuç: {bolme}')

# Kullanıcıdan alınan kenar bılgısıne göre karenın alanını ve çevresini heasplayan uygulamayı yazınız.

# x = int(input("Lütfen kenar uzunluğunu giriniz: "))
#
# alan = x*x
# cevre = 4*x
#
# print(f'Alan: {alan}, Cevre: {cevre}')

# dikdotrgenın alanını ve çevreisni hesaplayın

kenar1=int(input("kenar1: "))
kenar2=int(input("kenar2: "))

alan = kenar1 * kenar2
cevre = 2*(kenar1 + kenar2)
print(f'Alan={alan}\n'
      f'Cevre={cevre}')
