import uuid
from datetime import datetime
from enum import Enum

from _socket import gethostbyname, gethostname


# Kalıtım
# Nasıl ki biyolojide olduğu gibi bizler anne ve babalarımızdan kalıtım vasıtasıyla ozellikler kazandıysak yazılımda da ust sınıflar (base class) vasıtasıyla alt sınıflara (child class) özellik atratabılıyoruz. Burada ki amaç aly sınıfların oırtak özelliklerinin bir ata sınıfta toplanmasıdır. Kod tekrarını engelleyerek merkezi bir yerden yani atadan özellikler alt sınıflara aktarılırlar. Ayrıca üst seviyeli yazılım prensiblerine ve tasarım desenlerine uymak ıcın atılması gereken adımlarlarda biridir.

class Human:
    def __init__(self,height: float, weight: float, alias: str):
        self.alias = alias
        self.weight = weight
        self.height = height

    def show_information(self):
        return self.__dict__

class Knight(Human):
    pass

class Rogue(Human):
    pass

k1 = Knight(height=1.84, weight=98, alias='beast')
print(k1.show_information())
r1 = Rogue(height=1.50, weight=68, alias='hıhız')
print(r1.show_information())

employees = []


class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3

class BaseEntity:
    def __init__(self, first_name: str, last_name: str, department: str):
        self.first_name = first_name
        self.last_name = last_name
        self.department = department
        self.id = str(uuid.uuid4())
        self.status = Status.Active.name
        self.create_date = datetime.now()
        self.created_ip_address = gethostbyname(gethostname())
        self.created_machine_name = gethostname()


class Employee(BaseEntity):
    pass

class Employee_Service:
    def create(self, employee: Employee):
        employees.append(employee)
        print(f'{employee.first_name} {employee.last_name} has been created..!')

    def get_all(self):
        for item in employees:
            print(f'{item.__dict__}')

    def get_by_full_name(self, full_name: str):
        for employee in employees:
            if f'{employee.first_name} {employee.last_name}'.lower().__contains__(full_name):
                print(employee.__dict__)

def main():

    service = Employee_Service()

    while True:

        process = input('Type process: ')

        match process:
            case 'create':
                first_name = input('First Name: ')
                last_name = input('Last Name: ')
                department = input('Department: ')
                employee = Employee(first_name=first_name, last_name=last_name, department=department)
                service.create(employee)
            case 'get all':
                service.get_all()

