#
#
# # Python programlama dilinde bir nesne yaratmak için "class" anahtar sözcüğü kullanıyoruz. class ile tanımladığımız yapının içerisine yaratacağım ya da
# # projemizde ihtiyaç duyduğumuz nesnenin(objenin) özelliklerinin tanımlıyoruz. class'ları gerçek dünyada ki prototiplere benzetebilriz.
#
# class Vehicle:
#     # attribute (özelliklerini tanımladık.
#     door_number = 0
#     brand = ''
#     model = ''
#     engine_size = ''
#     torque = 0
#
# # Aşağıda Vehicle() sınıfından bir nesne ürettik. Yazılım dünyasında bu işleme örneklem çıkartma (instance) denir. Üretilen nesnein adını "x" koyduk. artık "x"
# # Vehicle() sınıfının bütün özelliklerine sahip. x bir objedir.
#
# x = Vehicle()
# x.brand = 'Mercedes'
# x.model = 'C'
# x.engine_size = 5
# x.torque = 4
# print(f'Brand: {x.brand}')
#
# #Artık istediğimiz hyerde istediğimiz kadar Vehicle() sınıfndan nesne üretebilriiz. Nasıl ki built-in nesnesini istediğimiz yerde istediğimiz kadar kullanabiliyorsak custom nesneler içinde geçerlidir.
#
# y = Vehicle()
# y.brand = 'Ford'
# y.model = 'Shelby'
# y.door_number = 4
# y.engine_size = 6
# y.torque = 5
#
# print(f'Brand: {y.brand}'
#       f'\nModel: {y.model}'
#       f'\nEngineSize: {y.engine_size}'
#       f'\nTorque: {y.torque}'
#       f'\nDoorNumber: {y.door_number}')
#
#
# class Boxer:
#     #class attribute
#     alias = ''
#
#
#     def __init__(self, first_name, last_name, age):
#         # aşağıdaki "adi" ve "soyadi" attribute'leri için object attribute denir.
#         self.adi = first_name
#         self.soyadi = last_name
#         self.yas = age
#         # self sınıfı temsil eder.
#
# boxer_1 = Boxer(first_name='Mike', last_name='Tyson', age=75)
# print(dir(Boxer))
# print(dir(boxer_1))
# boxer_2 = Boxer(first_name='Mike', last_name='Tyson', age=57)
# print(dir(boxer_2))
#
#
# class Circle:
#     pi = 3.14
#
#     def __init__(self, r):
#         self.radius = r
#
#     def calculate_area(self, r):
#         return self.pi * self.radius ** 2
#
#     def calculate_perimeter(self):
#         return 2 * self.pi * self.radius
#
#
# yari_cap = float(input('Yari çap: '))
# c1 = Circle(r=yari_cap)
# print(f'Çevre: {c1.calculate_perimeter()}')
# print(f'Alan: {c1.calculate_area()}')

# Depatmant adında bir sınıf oluşturalım
# departmant_name ve employee_cunt class attribute
# name, age object attribute
# show_information() olsun
# show_employee_count() fonksiyonu olsun. Departmant sınıfından her instance alındığında
# employee_count 1 attrılısın ve bu arttırma işleminin sonucu ekrana yazılsın.

class Departmant:
    departmant_name = 'Software Developer'
    employee_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Departmant.employee_count +=1
        self.show_information()
        self.show_employee_count()

    def show_information(self):
        print(f'Name: {self.name}'
              f' Age: {self.age}'
              f' Department Name: {self.departmant_name}')

    def show_employee_count(self):
        print(f'Total Employee: {self.employee_count}')


e1 = Departmant('burak',35)
e1 = Departmant('hakan',38)
e1 = Departmant('ipek',40)
