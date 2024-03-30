# from uuid import uuid4
# from datetime import datetime
# from enum import Enum
# from _socket import gethostname, gethostbyname
# from pprint import pprint
#
#
# # Method overriding
# # Ata sınıflarda (parent class) bulunan methodların alt sınıflareda ezilerek onlara yeni işlevler kazandırılmasına method overriding diyoruz. Ata sınıftan gelen fonksiyonun illa var olan yeteneğinin geçersiz kılıp ona yeni yetenek kazandırmaya gerek yoktur.Bazen var olan yetenek extend edinebilir.
#
# class Status(Enum):
#     Active = 1
#     Modified = 2
#     Passive = 3
#
# class BaseEntity:
#     def __init__(self, name: str, description: str):
#         self.name = name
#         self.description = description
#         self.id = str(uuid4())
#         self.status = Status.Active.name
#         self.create_date = datetime.now()
#         self.created_ip_address = gethostbyname(gethostname())
#         self.created_machine_name = gethostname()
#
#     def show_info(self):
#         pprint(f'Id: {self.id}\n'
#                f'Name: {self.name}\n'
#                f'Description: {self.description}')
#
#
# class Category(BaseEntity):
#     pass
#
# class Product(BaseEntity):
#     def __init__(self, name: str,description: str, price: float, stock: float):
#         super().__init__(name,description)
#         self.stock = stock
#         self.price = price
#
#     def show_info(self):
#         super().show_info()
#         print(f'Stock: {self.stock}\n'
#               f'Price: {self.price}')
#
# c1 = Category('Boxing Gloves', 'Best boxing gloves')
# c1.show_info()
# p1 = Product('Training Gloves', 'Best training gloves', 12.2, 34)
# p1.show_info()
from datetime import datetime


# BasePhone adında bir ata sınıf oluşturalım. phone_şd, brand, model, price attribute'leri olsun.
# show_info() fonksiyonu olsun. phone_ring_sound() fonksiyonu 'genel telefon sesi' string ifadesini return
# Samsung adında bir sınıf oluşturalım. BasePhone kalıtım olacak . operating_system attriburte u olsun. phone_ring_sound fonksiyonu da 'samsung_telefon sesi' return etsin
# IPhone adında bir sınıf oluşturalım. BasePhone kalıtım alacak. camera attribute olsun. 'IPhone telefon sesi dönsğn
#

# class BasePhone:
#     def __init__(self, phone_id: int, brand: str, model: str, price: float):
#         self.price = price
#         self.brand = brand
#         self.model = model
#         self.phone_id = phone_id
#
#     def show_info(self):
#         print(f'Id: {self.phone_id}\n'
#               f'Model: {self.model}\n'
#               f'Brand: {self.brand}\n'
#               f'Price: {self.price}')
#
#     def phone_ring_sound(self):
#         return f'Genel telefon sesi'
#
# class Samsung(BasePhone):
#     def __init__(self, phone_id: int, brand: str, model: str, price: float, operation_system: str):
#         super().__init__(phone_id, brand, model, price)
#         self.operation_system = operation_system
#
#     def phone_ring_sound(self):
#         return 'Samsung telefon sesi'
#
#     def show_info(self):
#         super().show_info()
#         print(f'Operating System: {self.operation_system}\n')
#
#
# class IPhone(BasePhone):
#     def __init__(self, phone_id: int, brand: str, model: str, price: float, camera: str):
#         super().__init__(phone_id, brand, model, price)
#         self.camera = camera
#
#     def phone_ring_sound(self):
#         return 'Iphone telefon sesi'
#
#     def show_info(self):
#         super().show_info()
#         print(f'Camera: {self.camera}\n')
#
#
# s1 = Samsung(1, 'Samsung', 'Galaxy 20', 76.00, 'Android')
# print(s1.phone_ring_sound())
# s1.show_info()
#
# i1 = IPhone(1, 'IPhone', '15 pro max', 89.89, '5.5x')
# print(i1.phone_ring_sound())
# i1.show_info()


class BaseBill:
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.amount = amount
        self.bill_name = bill_name
        self.value_add_task = value_add_task

    def calculate_bill(self):
        return self.amount * self.value_add_task

    def create_log(self):
        with open(file='bill_info.txt', mode='a', encoding='utf-8') as file:
            file.write(f'Bill Name: {self.bill_name}\n'
                       f'Total Amount : {self.amount}\n'
                       f'Create Date: {datetime.now()}')


class Electricity_Bill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw = kw

    def calculate_bill(self):
        return super().calculate_bill() * self.kw

class Water_Bill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, mill: float):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill

    def calculate_bill(self):
        return super().calculate_bill() * self.mill


class Naturel_Gas_Bill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float, m3: float):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3

    def calculate_bill(self):
        return super().calculate_bill() * self.m3