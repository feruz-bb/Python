"""
Created time: 14:36:50 31.08.2024
Muallif: Baqoyev Feruzbek Barakayevich
Maqsad: while orqali ro'yxat va lug'atlar
"""

## While yordamida ro'yxatni to'ldirish
# names = []
# print("Ro'yxatga ism qo'shing ")
# while True:
#     name = input(">>> ")
#     names.append(name)
#     print("Yana ism qo'shishni istaysizmi(ha/yo'q) ?")
#     ask = input(">>> ")
#     if ask == 'ha':
#         continue
#     else:
#         print("Yordamingiz uchun tashakkur")
#         break

## while yordamida lug'atni to'ldirish
#print("Do'stlaringiz yoshini saqlaymiz. ")
# friends = {}
# ishora = True
# n = 1
# while ishora:
#     print(f"{n}-do'stingizni ismini kiriting.")
#     name = input(">>> ")
#     age = input(f"{name.title()}ning yoshini kiriting >>> ")
#     age = int(age)
#     friends[name] = age
#     print("Yana ma'lumot qo'shasizmi? (ha/yo'q) ")
#     n += 1
#     ask = input(">>> ")
#     if ask == 'ha':
#         continue
#     else:
#         print("Ma'lumotlar uchun raxmat !!!")
#         break
# for name, age in friends.items():
#     print(f"{name.title()}ning yoshi {age} da.")

## RO'YXAT ELEMENTLARINI O'CHIRISH
# cars = ['lacetti', 'nexia', 'nexia', 'nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)

# RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH
# students = ['feruzbek', 'nurmatjon','murodjon','mirdovud']
# grades = {}
# while students:
#     student = students.pop()
#     grade = input(f"{student.title()}ning bahosini kiriting >>> ")
#     print(f"{student.title()} baholandi.")
#     grades[student] = grade

