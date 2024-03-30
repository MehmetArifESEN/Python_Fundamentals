from pprint import pprint
from uuid import uuid4

students = {}

def create_students(first_name: str, last_name: str, phone: str):
    student_id = str(uuid4())
    students[student_id] = {
        'first_name': first_name,
        'last_name': last_name,
        'phone': phone
    }

def update_students(student_id: str, first_name: str, last_name: str, phone: str):
    students.update({
        student_id: {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone
        }
    })

def delete_students(student_id: str):
    del students[student_id]
    print(f'{student_id} has been deleted')

while True:
    print('Manuel Guide \n'
          '===============\n'
          'Create\n'
          'Update\n'
          'Delete\n'
          'Exit')
    process = input('Type your process upon manuel guide: ').lower()

    match process:
        case 'create':
            first_name = input('First name: ')
            last_name = input('Last name: ')
            phone = input('Phone: ')
            create_students(first_name, last_name, phone)
        case 'list':
            pprint(students)
        case 'update':
            student_id = input('Student ID: ')
            first_name = input('First name: ')
            last_name = input('Last name: ')
            phone = input('Phone: ')

            update_students(student_id, first_name, last_name, phone)
        case 'delete':
            delete_students()
        case 'exit':
            print('Application has been closing...!')
            break
        case _:
            print('Please type  valid process name ..!')

print(students)