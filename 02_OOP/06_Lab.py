from math import factorial, pow
from time import sleep, time


# Abstraction (Soyutlama)
# OOP yapıları arasında en önemlisidir.
# Üst seviyeli yazılım prensiplerine ve yasarım desenlerıne uymak istiyorsak kod bloklarımızda soyutlama muhakkak olmalıdır. Soyutlama ile amaçlanan ana mantık şudur: ata sınıfları soyut yaparak alt sınıflara kural koymak.

# Soyutlama geçmeden once öğrenmeniz gereken 1-2 husus bulunmaktadı. Bunlardan 1. decorator bir diğeri ise meta class

# region Decorator
# python proglamlama dilinde kullanılan bir keyword'Tür. Bir fonksiyonu bir devorator ile var olan yetenği üüzerine bir yetenek daha ekleyebılırız. Methodlarımız yoğun kod yazmadan yeni bir yetenek ile extend etmiş oluyoruz. Python'da built-in bir çok decorator vardır. bunlardan bazıları @abstractmethod, @static, @property vb. tabi ki custom decorator yazılınabılır.
# def uppercase_name(function):
#     def inner_func():
#         func = function()
#         make_uppercase = func.upper()
#         return make_uppercase
#     return inner_func()
#
# def get_fullname():
#     return 'Mike Tyson'
#
# print(uppercase_name(get_fullname))
#
# @uppercase_name
# def get_name():
#     return 'burak yilmaz'
#
# print(get_name)
# endregion


def calculate_time_execute():
    pass

# kendi görevlerını ne kadar surede tamamlamıs onu yazdıracagız.


def us_alma(a: int, b: int):
    print(f'Sonuc: {pow(a, b)}')

def faktoriyel_hesaplama(number: int):
    print(f'Sonuç: {factorial(number)}')

def toplama(x: int, y: int, z: int):
    print(f'Sonuç: {x + y + z}')


us_alma(2, 3)
faktoriyel_hesaplama(5)
toplama(3, 4, 5)