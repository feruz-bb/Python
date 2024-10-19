"""
Created time: 22:44:30 03.09.2024
Muallif: Baqoyev Feruzbek Barakayevich
Content: Qiymat qaytaruvchi funksiyalar (Amaliyot)
"""


## TASK 1,2
# def person_info(name, surname, age, birth_location = None, e_mail = None, phone_number = None):
#     """Shaxs haqida to'liq ma'lumotlarni lug'at shaklida qaytaradigan funksiya"""
#     info = {
#         'ism':name,
#         'familiya':surname,
#         'yosh':age,
#         't_joy':birth_location,
#         'e_mail':e_mail,
#         'tel_raqam':phone_number
#     }
#     return info

# mijozlar = []
# while True:
#     print("Quyida mijoz ma'lumotlarini to'ldiramiz.")
#     ism = input("Mijoz ismini kiriting >>> ")
#     familiya = input("Mijoz familiyasini kiriting >>> ")
#     yosh = input("Mijozning yoshini kiriting >>> ")
#     t_joy = input("Mijozning tug'ilgan joyini kiriting >>> ")
#     e_mail = input("Elektron pochta manzilini kiriting >>> ")
#     tel_raqam = input("Mijozning telefon raqamini kiriting >>> ")
#
#     mijozlar.append(person_info(ism,familiya,yosh,t_joy,e_mail,tel_raqam))
#     ask = input("Yana mijoz qo'shishni istaysizmi? (yes/no) >>> ")
#     if ask == 'yes':
#         continue
#     else:
#
#         break
#

## TASK 3
# def compare(number1, number2, number3):
#     big = 0
#     if number1 >= number2:
#         if number1 >= number3 :
#             big = number1
#         else:
#             big = number3
#     else:
#         if number2 >= number3:
#             big = number2
#         else:
#             big = number3
#     max = f"Eng kattasi: {big}"
#     return max
# import math as m
## TASK 4
# def info_circle(radius):
#     diametr = radius*2
#     perimetr = 2*m.pi*radius
#     surface = m.pi*pow(radius,2)
#     info = {
#         'radius':radius,
#         'diametr':diametr,
#         'perimet':perimetr,
#         'surface':surface
#     }
#     return info
## TASK 5
def tub_sonlar(number1, number2):
    if number1 >= number2:
        print("1-son 2-sondan kichik bo'lishi lozim !!!")
        return
    tub_son = []

    for n in range(number1,number2):
        bolinganlar = []
        for bolish in range(1,number2 + 1):
            if n % bolish == 0:
                bolinganlar.append(n)
        if len(bolinganlar) == 2:
           tub_son.append(n)
    print(tub_son)

tub_sonlar(1,10)