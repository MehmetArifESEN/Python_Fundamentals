
# For Loop
# For Loop'a geçmeden önce incelememiz gereken yardımcı fonksiyon ve operatör bulunmaktadır.
# Bunlar "in" , "not in" ayrıca range() built-in fonksiyonlardır.

# "in" & "not in"
# name = 'mike tyson'
# # not: string ifadeler karakter listeleridir.
#
# print('b' in name)  # output => false
# print('m' in name)  # output => true
# print('M' in name)  # output => false
#
# # not in operatoru
# print('M' not in name)  # output => true
# print('m' not in name)  # output => false

# Not: fonksiyonalrın içerisine verdiğimiz argümanlara göre fonksiyonlar farklı işler icra ederler.
# Burada farklı işlerden kastımız birbirinden alakasız işlemler değildir.
# Ana bir iş mantığının farklı versiyonalrıdır. Aşağıdaki range fonksiyonunu bu cümleye göre inceleyelim.

# range() => range fonksiyonun ana iş mantığı bize bir sayı listesi dönmesidir. range aldığı argumanlara gore yaratacağı sayı listesinin özellikleri farklılaşmaktadır
# 1 argüman aldığında => default olarak 0'dan başlayarak argüman olarak verilen tamsayı(n-1) olarak bir tamsayı listesi döner.

# for i in range(10):
#     print(i, end=",")
#
# 2 argüman aldığında range(10,20) bu durumda 10 dan başlayıp 19 a kadar gıder
# for i in range(10,20):
#     print(i, end=",")
# 3 argüman aldığında => range(10,101,5) bu durumda 10dan başlayıp 100 e kadar 5 er 5 er artacak sekılde bır lıste olusturur
# for i in range(10,101,5):
#     print(i, end=",")

