# # Değer Döndüren Fonksiyonlar (Returnable)
#
# lst = [12, 11, 19, 2, 99]
# lst_1 = []
# lst_2 = []
#
# # lst içerisinde ki çift sayıları 2 ile çarparak lst_! içerisine ekleyelim. tek sayıları 3 ile çarparak lst_2 ' ye ekleyelim.
# def tek_cift_mi(sayi: int) -> str:
#     if sayi % 2 == 0:
#         return 'cift'
#     else:
#         return 'tek'
#
# def append_list(result: str, sayi: int) -> None:
#     if result == 'cift':
#         lst_1.append(sayi*2)
#     else:
#         lst_2.append(sayi*3)
#
#
# def main():
#     for i in lst:
#         result = tek_cift_mi(i)
#         append_list(result, i)
#     print(lst_1)
#     print(lst_2)
#
#
#
# main()

#Kullanıcıdan alınan 3 adet sayıyı topladımktan sonra karesını alarak sonucunu ekrana yazdıralım

# def toplam(s1: int, s2: int, s3: int) -> int:
#     return s1 + s2 + s3
#
# def karesini_hesapla(sayi: int) -> None:
#     print(f'Sonuç: {sayi ** 2}')
#
# def main():
#     x = int(input('Sayi: '))
#     y = int(input('Sayi: '))
#     z = int(input('Sayi: '))
#
#     sonuc = toplam(x, y, z)
#
#     karesini_hesapla(sonuc)
#
#     # karesini_hesapla(toplam(x, y, z)) yukarıkai 2 satırı bu skeılde de yazabılırdık.
#
# main()

# Aşağıdaki listede bulunan rakamların liste içerisinde geçme sıklığını bulun ve sözlük tipinde çıktı verin. Rakamın kendisi key geçme sıklığı value olacak sekılde

# rakamlar = [1, 1, 1, 5, 5, 3, 1, 3, 3, 2, 4, 4, 4, 4, 2, 2, 4, 3, 5]
#
# def frequency_count(numbers: list) -> None:
#     frequency_dict = {}
#
#     for item in numbers:
#         if item in frequency_dict:
#             frequency_dict[item] += 1
#         else:
#             frequency_dict[item] = 1
#
#     for key, value in frequency_dict.items():
#         print(f'key: {key}, value: {value}')
#
# frequency_count(rakamlar)

# bir söz öbeğinde tekrar eden kelimeklerden arındırarak çıktı verelim
# örnek input => merhaba ben burak burak ben burak
# çıktı = merhaba ben burak

# def remove_duplicate_word(sentece: str) -> None:
#     lst = []
#
#     for item in sentece.split(' '):
#         if item not in lst:
#             lst.append(item)
#
#     result = ' '.join(lst)
#
#
#     print(result)
#
# cumle = input("Please type something: ")
# remove_duplicate_word(cumle)

# Kullanıcıdan alınan söz öbeğindeki kelimeleri alfabetik olarak sıralayalım

# def sort_word(sentece: str) -> None:
#     words = []
#     for item in sentece.split(' '):
#         words.append(item)
#
#     words.sort()
#
#     print(words)
#
# sort_word(input('Type Something: '))

user_dict = {
    '1': {
        'user_name': 'beast',
        'password': '123'
    },
    '2': {
        'user_name': 'savage',
        'password': '123'
    }
}

def sign_in(user_name: str, password: str) -> None:
    is_active = False

    for i in range (1, len(user_dict) + 1):
        if user_dict.get(str(i)).get('user_name') == user_name and user_dict.get(str(i)).get('password') == password:
            is_active = True
            break


def get_user_name(users: dict) -> list:
    user_name_list = []

    for i in range (1, len(users) + 1):
        user_name = users.get(str(i)).get('user_name')
        user_name_list.append(user_name)

    return user_name_list

def sign_up(user_name: str, password: str) -> None:
    if user_name in get_user_name(user_dict):
        print('Invalid user name. Please choose a different user name..!')
    else:
        user_dict[str(user_dict)] = {
            'user_name': user_name,
            'password': password
        }
def main():
    while True:
        process = input('Type a process: ').lower()
        if process == 'exit':
            print('Application has been closing..!')
        elif process == 'sign in':
            user_name = input('User Name: ')
            password = input('Password: ')
            sign_in(user_name, password)
        elif process == 'sign up':
            user_name = input('User Name: ')
            password = input('Password: ')
            sign_up(user_name, password)
        else:
            print('Please type a valid process')


main()
