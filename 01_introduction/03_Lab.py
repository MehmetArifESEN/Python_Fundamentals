# Try - Except - Finally
# Uygulamalarda anlık oalrak alınan hatalara (exception) yani istisnai durumlar diyorız. bu durumları try - except blokları ile handle etmeye çalışıyoruz.
# try:
#     x = int(input("Tam sayı giriniz: "))
#     # sonuc = x / 1
#     sonuc = x / 0
#     print(sonuc)
# except ZeroDivisionError as err:
#     print(f'Bir tam sayı sıfıra bölünemez..! \n {err}')
# finally:
#     print('Ne olursa olsun çalışırım ben')
#
try:
    age = int(input('Age: '))
    print(age)
    # x = int(input('Tam sayı giriniz: '))
    # sonuc = x / 0
    # print(sonuc)
except ValueError as err:
    print(f'{err}')
else:
    print('Exception çalışmazsa çalışır.')