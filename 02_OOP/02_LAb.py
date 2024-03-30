from pprint import pprint
# CRUD
# categories = {}

from uuid import uuid4

categories = {}

class Category:
    def __init__(self,name: str, description: str):
        self.description = description
        self.name = name
        self.id = uuid4()

class Category_Service:
    def create(self, category_obj: Category) -> None:
        categories[str(category_obj.id)] = {
            'name': category_obj.name,
            'description': category_obj.description
        }
        print(f'{category_obj.name} has been created..!')


    def get_all(self, category_dict: dict) -> None:
        pprint(category_dict)

    def get_by_id(self, id: str) -> dict:
        for key in categories.keys():
            if key == id:
                return categories.get(key)

    def update(self, id: str, name: str, description: str):
        current_category = self.get_by_id(id)

        current_category.update({
            'name': name,
            'description': description
        })

        print(f'{id} has been updated..!')

    def delete(self, id: str) -> None:
        current_category = self.get_by_id(id)

        if current_category != {}:
            del categories[id]
            print('Categories has been deleted..!')
        else:
            print('There is no such category..!')




def main():
    while True:
        service = Category_Service()

        process = input('Please type a transaction name: ').lower()

        match process:
            case 'exit':
                print('Applicartioon has been closing..!')
                break
            case 'create':
                category_name = input('Category Name: ')
                category_description = input('Category Description: ')
                category_obj = Category(category_name, category_description)
                service.create(category_obj)
                service.get_all(categories)
            case 'get all':
                service.get_all(categories)
            case 'get by id':
                id = input('Category ID: ')
                pprint(service.get_by_id(id))
            case 'update':
                id = input('Category Name:')
                category_name = input('Category: ')
                category_description = input('Description: ')
                service.update(id= id, name= category_name, description= category_description)
                print(service.get_by_id(id))
            case 'delete':
                id = input('Category ID: ')
                service.delete(id)
            case _:
                print('Please type a corretc transaction name..!')

main()