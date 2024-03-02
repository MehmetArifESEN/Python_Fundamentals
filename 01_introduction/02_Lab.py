# If - Else

# region Example 1
# Kullanıcıdan 2 adet sayı alalım ve bu sayılardan büyük olanı ekrana yazalım
# x = int(input("Enter a number: "))
# y = int(input("Enter another number: "))
#
# if x>y :
#     print(f'{x} büyüktür')
# elif x<y :
#     print(f'{y} büyüktür')
# else:
#     print('Sayılar eşittir.')
# endregion

# region Example 2
#Kullanıcıdan alına sayı çift mi tek mi ?
# sayi = int(input("Enter a number: "))
# if sayi%2==0:
#     print(f'{sayi} çifttir')
# else:
#     print(f'{sayi} tektir')
# endregion

# region Example 3
# Kullanıcıdan alınan sayı çift mi tek mi ?
# number = int(input("Enter a number: "))
# if number>0:
#     print(f'{number} sayısı pozitiftir')
# elif number==0:
#     print(f'{number} sayısı nötrdür')
# else:
#     print(f'{number} sayısı negatiftir')
# endregion

# region Example 4
# kullankıcıdan mevsim bilgisi alalım. gele mevsime göre ayları ekrana yazalım
# bu soruyu match-case kullanarak yapalım. python 3.10 sürümü ile gelen bir yapı. if-else alternatifdir.
# sadece string kontrollerde kullanabılıyoruz
# ay = str(input("Lütfen bir ay giriniz? "))
# match ay:
#     case "Haziran" | "Temmuz" | "Ağustos":
#         print("Yaz mevsimi")
#     case "Eylül" | "Ekim" | "Kasım":
#         print("Sonbahar mevsimi")
#     case "Aralık" | "Ocak" | "Şubat":
#         print("Kış mevsimi")
#     case "Mart" | "Nisan" | "Mayıs":
#         print("İlkbahar mevsimi")
#     case _:
#         print("Lütfen İlk harfi büyük olacak şekilde geçerli bir ay giriniz")


# endregion

# region
# Kullanıcıdan alınan araç türü ve hız bilgisi üzerinden ceza var yada ceza yok
# otomobil, kamyon, motorsiklet
# 50, 30, 60

# hiz=int(input("Hızı giriniz"))
# tur= str(input("Araç türünü giriniz"))
#
# if hiz > 0:
#     if tur=='otomobil':
#         if hiz>= 50:
#             print('Cezalısın')
#         else:
#             print('Cezalı değilsin')
#     elif tur=='kamyon':
#         if hiz>= 30:
#             print('Cezalısın')
#         else:
#             print('Cezalı değilsin')
#     elif tur=='motor':
#         if hiz>= 60:
#             print('Cezalısın')
#         else:
#             print('Cezalı değilsin')
#     else:
#         print('Araç türünü doğru giriniz')
# else:
#     print('Hız bilgisi negatif olamaz..!')



# endregion

# region
# Kullanıcıdan alınan 3 tane sayıdan büyük olaı ekrana yazın
# sayi1 = int(input("Birinci Sayı giriniz: "))
# sayi2 = int(input("İkinci Sayı giriniz: "))
# sayi3 = int(input("Üçüncü Sayı giriniz: "))
#
# if sayi1 > sayi2 and sayi1 > sayi3:
#     print(f'{sayi1} sayısı en büyüktür')
# elif sayi2>sayi1 and sayi2>sayi3:
#     print(f'{sayi2} sayısı en büyüktür')
# elif sayi3>sayi1 and sayi3>sayi2:
#     print(f'{sayi3} sayısı en büyüktür')
# else:
#     print('Sayılardan bazıları birbirine eşit..!')
# endregion

# region Example 7
# Kullanıcıdan aradığı ürün bilgisini alıyoruz hangi reyonda ise ona yönlendiriyoruz
# urun=input("Ürün ismini giriniz: ")
#
# if urun == 'domates' or urun 'patlican'
# endregion

# region Example 8
# Kullanıcıdna satın aldığı kitap sayısını alalım
# bir kitap 5 TL
# 1-20 'dan arasında kitap alırsa yüzde 5 indirim
# 21-50 arasında kitap alırsa yüzde 10
# 51-75 arasında kitap alırsa yüzde 15
# 76-100 arasında da kitap alırsa yüzde 20

# price = 5
# adet = int(input("Kitap sayısını giriniz: "))
#
# if 1<=adet<=20:
#     toplam=price*adet*0.95
#     print(f'{toplam} TL ödemeniz bulunmaktadır')
# elif 21<=adet<=50:
#     toplam=price*adet*0.90
#     print(f'{toplam} TL ödemeniz bulunmaktadır')
# elif 51<=adet<=75:
#     toplam = price * adet * 0.85
#     print(f'{toplam} TL ödemeniz bulunmaktadır')
# elif 76<=adet:
#     toplam = price * adet * 0.80
#     print(f'{toplam} TL ödemeniz bulunmaktadır')
# else:
#     print("Sepette kitap mevcut değil")

# endregion

# region Examle 9
# lineer bir doğrunun katsayılarını bulun
# delta = b ** 2 - 4 * a * c
# delta sıfırdan büyükse 2 katsayı
# delta sıfırsa 1 katsayı

# from math import sqrt
# a = int(input('(a) katsayısını girin: '))
# b = int(input('(b) katsayısını girin: '))
# c = int(input('(c) katsayısını girin: '))
#
# delta = b ** 2 - 4 * a * c
#
# if delta > 0:
#     x1 = -b - sqrt(delta) / 2 * a
#     x2 = -b + sqrt(delta) / 2 * a
#     print(f'there is two real root. \n First Real Root: {x1}\n Second Real Root: {x2}')
# elif delta == 0:
#     x1 = -b -sqrt(delta) / 2 * a
#     print(f'There is one real root. \n First Real Root: {x1}')
# else:
#     print('There is no real root.')
# endregion

# region Example 10
# Kullanıcıdan username, password, kilo, boy bilgilerini alıyoruz
# kullanıcı login olacak. (beast, 123)
# bmi bilgisini vereceğiz
username=input("Kulllanıcı adını giriniz: ")
password=input("Parolayı giriniz: ")
if username=='beast' and password=='123':
    print("Giriş başarılı")
    boy=float(input('Boyunuzu m cinsinden giriniz: '))
    kilo=float(input('Kilonuzu kg cinsinden giriniz: '))
    if 0.50<=boy<=2.5 and 1<=kilo<500.5:
        bmi=kilo/(boy**2)
        if bmi<18.5:
            print(f'{bmi} değerine göre zayıfsınız')
        elif 18.5<=bmi<=24.9:
            print(f'{bmi} değerine göre Normal ağırlıktasınız')
        elif 24.9 < bmi <= 29.9:
            print(f'{bmi} değerine göre Kilolusunuz')
        elif 29.9 < bmi <= 34.9:
            print(f'{bmi} değerine göre 1. Derece Obezite')
        elif 34.9 < bmi <= 39.9:
            print(f'{bmi} değerine göre 2. Derece Obezite')
        elif 40 < bmi:
            print(f'{bmi} değerine göre 3. Derece Obezite')
    else:
        print('Değerleri yanlış girdiniz.Tekrardan deneyiniz')
else:
    print('Hatalı giriş yaptınız.Tekrardan deneyiniz.')


# endregion