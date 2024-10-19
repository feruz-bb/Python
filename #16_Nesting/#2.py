"""
Create time: 14:58:20 29.08.2024
Muallif: Baqoyev Feruzbek Barakayevich
Maqsad: Nesting (Amaliyot)
"""

#    TASK 1,2
# beruniy = {
#     'name':'abu rayhon beruniy',
#     't_yil':'xv asr',
#     't_joy':'kat',
#     'projects':['hindiston', 'geodeziya']
# }
#
# xorazmiy = {
#     'name':'muso al-xorazmiy',
#     't_yil':'783',
#     't_joy':'xorazm',
#     'projects':['zij', 'arifmetika']
# }
# musk = {
#     'name':'elon musk',
#     't_yil':'1971',
#     't_joy':'pretoriya',
#     'projects':['tesla','yana','spaceX']
# }
# m_shaxslar = [beruniy, xorazmiy, musk]
#
# for shaxs in m_shaxslar:
#     print(f"\n \nName: {shaxs['name'].title()}")
#     print(f"Tug'ilgan yil: {shaxs['t_yil']} ")
#     print(f"Tug'ilgan joy: {shaxs['t_joy'].title()}")
#     print(f"Asarlari: ", end=' ')
#     for project in shaxs['projects']:
#         print(f"{project.title()}", end=" ")

# TASK 3
# my_friends = {
# }
# print("Nechta do'stingizni kiritmoqchisiz? >>> ")
# n = int(input())
# for i in range(n):
#     friend = input(f"{i+1}-do'stingizni ismini kiriting >>> ")
#     my_friends[friend] = []
#     print(f"{friend.title()} nechta filmni yoqtiradi >>> ")
#     film_number = int(input())
#     for k in range(film_number):
#         film_name = input(f"{k+1} - film nomini kiriting >>> ")
#         my_friends[friend].append(film_name)
# for name in my_friends.keys():
#     print(f"\n\nName: {name.title()}")
#     print("Yoqtirgan filmlari: ", end='')
#     for film in my_friends[name]:
#         print(f"{film.upper()}, ", end='')

# TASK 4, 5

# countries = {
#     'usa':{
#         'language':'american english'
#     },
#     'uzbekistan':{
#         'language':'uzbek'
#     }
# }
#
# for country, info in countries.items():
#     print(f"\n\nCountry: ", end='')
#     print(f"{country.upper()}")
#     print("Language: ", end='')
#     for value in info.values():
#         print(f"{value.title()}", end='')
#
#
# print(f"\n\nQaysi mamlakat haqida ma'lumot olmoqchisiz? ")
# area = input(">>> ")
# if area in countries.keys():
#     print(f"\n\nCountry: ", end='')
#     print(f"{area.upper()}")
#     print("Language: ", end='')
#     print(f"{countries[area]['language'].title()}")
# else:
#     print("Not info")
