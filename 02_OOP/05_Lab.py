from datetime import datetime
from enum import Enum
from pprint import pprint
from uuid import uuid4

from _socket import gethostname, gethostbyname


# Encapsulation (Veri Gizleme)
# Bir sınıfın her hangi bir üyesini enbcapsulation ettiğimizde , ilgili üyeye alt sınıflardan erişimi engellemiş oluruz. Bir başka deyiş ile ilgili sınıfın üyesini erişime kapatmış oluruz. Bu bağlamda erişemediğimiz üyenin üzerine alt sınıfta değer yazamayız. Lakin belirli şartlar doğrultusunda bu erişimi dolaylı yollar ile yapabikriz.

class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3


class BaseEntity:
    def __init__(self):
        self.__id = ''
        self.__created_date = ''
        self.__created_computer_name = ''
        self.__created_ip_address = ''
        self.__status = ''

    # Not: double underscore ile tanımladıpımız alanlara ene snıfırn orneklemınden (instance) nede bu sınıftan kalıtım alan alt sınıfın ornekleminden erişebiliyorum. Encapsule ettıgığımz alanlara sadece sınıfın yaşam alanında erişim yapabılıyourm. Aşağıda bir custom functıon yazarak bu private alanlara değer atadık.

    def set_values_private_attribute(self):
        self.__id = uuid4()
        self.__created_date = not datetime.now()
        self.__created_computer_name = gethostname()
        self.__created_ip_address = gethostbyname(gethostname())
        self.__status = Status.Active.name

    def show_information(self):
        return self.__dict__


# class Product(BaseEntity):
#     def __init__(self, name:str, description:str):
#         super().__init__()
#         self.name = name
#         self.description = description
#         self.__price = 0
#         self.__stock = 0
#
#     def set_value_product_attribute(self, price: float, stock: int):
#         super().set_values_private_attribute()
#         if price > 0 and stock >0:
#             self.__price = price
#             self.__stock = stock
#             print('Product has been created..!')
#             pprint(self.__dict__)
#         else:
#             print('Invalid Input..! \n'
#                   'Product stock and price can noy be negative value or zero..!')
#
#
# p1 = Product('Training Gloves', 'Everlast training gloves are best..!')
# p1.set_value_product_attribute(12.44, 160)


class Car(BaseEntity):
    def __init__(self, brand: str, model: str):
        super().__init__()
        self.model = model
        self.brand = brand
        self.__price = 0
        self.__sase_no = 0

    def set_value_car_attribute(self, price):
        if price > 0 :
            super().set_values_private_attribute()
            self.__sase_no = uuid4()
            self.__price = price
            print('Car has been created..!')
            pprint(self.__dict__)


c1 = Car('Dodge', 'TRX 1500')
c1.set_value_car_attribute(35000)