# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 01:38:36 2024

@author: baqoyev
"""
# pyhton.sariq.dev saytidan topshiriqlar
# 3 - dars
#
# print(pow(5,3))
# print(22%4)
# a = 125
# print("S = ", a*a)
# print("P = ", 4*a)
# pi = 3.14
# D = 12
# print("S = ",(pi*D**2)/4)
# a = 5
# b = 6
# print("c = ",(a**2 + b**2)**1/2)

# 4 - dars.Variables
# a = 'Hello World'
# print(a)
#
# xabar = 'Bu bir xabar matni'
# print(xabar)
#
# radius = 5
# pi = 3.14159
# aylana_yuzi = pi*radius**2
# print("Radiusi", radius,"ga teng aylana yuzasi", aylana_yuzi)
#

# 5 - dars.String methods
# kocha = "Uzanon"
# mahalla = "G'ovshun"
# tuman = "G'ijduvon"
# viloyat = "Buxoro"
# natija = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
# print(natija)
#
# kocha = input("Ko'changiz nomini kiriting: ")
# mahalla = input("Mahalla nomini kiriting: ")
# tuman = input("Tumaningiz nomini kiriting: ")
# viloyat = input("Viloyatingiz nomini kiriting: ")
#
# addres = (f"{kocha.capitalize()} ko'chasi,\n{mahalla.capitalize()} mahallasi,"
#           f"\n{tuman.capitalize()} tumani,\n{viloyat.capitalize()} viloyati")
# print(addres)

    # String metodlari (by chatGPT-4o)

# # string.capitalize() faqat birinchi belgini kattalashtiradi
# print("Capitalize: ", "salom".capitalize())
#
# # string.casefold()  harflarni kichigiga almashtiradi
# print("Casefold: ", "SALOM".casefold())
#
# # str.center(int, char) stringni butun son uzunligida belgi bilan, ikki tomondan to'ldiradi
# print("Center: ", "salom".center(8, "m"))
#
# # str.count(char) stringdagi kiritilgan belgilar sonini aniqlaydi
# print("Count: ", "salom".count('s'))
#
# # str.encode()
# print("encode: ", "00000".encode())
#
# # str.endswith() kiritilgan belgini bor yoki yo'qligini tekshiradi
# print("endswith: ", "Salom".endswith("lom"))
#
# # str.expandtabs() \t operator ishlatilganda tashlanadigan tablar sonini aniq ko'rsatadi
# print("expandtabs: ", "salom\tsalom".expandtabs(tabsize=4))
#
# # str.find() stringdan qidirilayotgan belgi qaysi indeksdaligini ko'rsatadi, faqat birinchi uchraganini
# #            qidiruv nuqtasi kiritilsa shu indeksdan keyin birinchi boshlagan
# print("find: ", "saloml".find('l',3))
#
# # str.index() belgi indeksini aniqlaydi
# print("index: ", "salom".index('l'))
#
# # str.isalnum agar string alphanumeric bo'lsa true qaytaradi
# print("isalnum: ", "salom123".isalnum())
#
# # str.isalpha() stringni alphabetic ekanligini tekshiradi
# print("isalpha: ", "salom".isalpha())
#
# # str.isdigit() kiritilganlar raqam ekanligini tekshiradi
# print("isdigit: ", "6546".isdigit())
#
# # str.islower() kiritilgan string kichkinaligini belgilardan iboratligini tekshiradi
# print("islower: ", "Salom".islower())

        # SONLAR
# print("Istalgan sonni kiriting: ")
# a = int(input(">>> "))
# kv = a*a
# kub = pow(a,3)
# print(f"{str(a)} ning kvadrati {str(kv)}")
# print(f"{str(a)} ning kubi {str(kub)}")
#

# print("Yoshingiz nechada: ")
# yosh = int(input(">>> "))
# print(f"Siz {str(2024 - yosh)} - yilda tug'ilgansiz.")

# print("Birinchi sonni kiriting: ")
# a = int(input(">>> "))
# print("Ikkinchi sonni kiriting: ")
# b = int(input(">>> "))
# print(f"{str(a)} + {str(b)} = {str(a + b)}")
# print(f"{str(a)} - {str(b)} = {str(a - b)}")
# print(f"{str(a)} * {str(b)} = {str(a * b)}")
# print(f"{str(a)} : {str(b)} = {str(a / b)}")

            # LIST
# mevalar = ['olma', 'anjir', 'shaftoli', 'o`rik']
# narhlar = [5000, 15000, 10000, 8000]
# sonlar = ['bir', 'ikki', 50, 60] # sonlar va matndan iborat aralash ro'yxat
# ismlar = []
# print("Birinchi element: ", mevalar[0])
# print("Ikkinchi element: ", mevalar[1])
# # olingan elementlar uchun string metodlaridan foydalanish mumkin.
# print("Birinchi element: ", mevalar[0].upper())
# print("Oxirgi element: ", mevalar[-1])

# .append("name") metodi orqali ro'yxat oxiriga element qo'shish mumkin
# .insert(index, "qiymat") berilgan indexga qiymatni joylashtiradi
# mevalar.insert(1, "shaftoli")
# print(mevalar)

# del metodi elementni o'chirish uchun xizmt qiladi
# del mevalar[index]
# .remove("qiymat")  elementni qiymat bo'yicha o'chirish
# mevalar.remove("shaftoli")
# .pop(index)  ro'yxatdagi elementni boshqa o'zgaruvchiga o'zlashtirih
# meva = mevalar.pop(1)

# ismlar = ['qudrat', 'bekzod', 'james']
# print("Salom", ismlar[1].title(), " bugun qayerga boramiz.")
# print(ismlar[0].title(), " bugun qayerlarda bo'lding.")
#
# sonlar = [5, 6.6, -8, 0]
# sonlar.append(4)
# sonlar.insert(1,9)
# del sonlar[0]
# sonlar.remove(-8)
# sonlar[1] = 5.5
# print(sonlar)
#

# t_shaxslar = ['Amir Temur', 'Sharof Rashidov', 'Kir II']
# z_shaxslar = ['Elon Musk', 'Pavel Durov', 'Shavkat Mirziyoyev']
#
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan"
#       f" zamonaviy shaxslardan {z_shaxslar.pop(2)} bilan "
#       f"suhbat qilishni istar edim.")

#
# friends =[]
# friends.append("Javohir")
# friends.append("Og'abek")
# friends.append("Murod")
# friends.remove("Murod")
# print(friends)
# friends.insert(0, "Mirdovud")
# friends.insert(2, "Bahriddin")
# friends.insert(4,"Alex")
# print(friends)
#
# mehmonlar = []
# mehmonlar.insert(0, friends.pop(0))
# mehmonlar.append(friends.pop(2))
# print(friends)
# print(mehmonlar)


        # RO'YXATLAR BILAN ISHLASH
#
# cars = ['bmw', 'volvo', 'hovo', 'gm']
# print(sorted(cars, reverse=True))
# print(cars)
#

# .reverse() ro'yxatni aylantirish
# cars.reverse()
# print(cars)
# print(len(cars))

#  range() funksiyasi orqali ma'lum bir oraliqdagi sonlar ketma-ketligini yaratish mumkin
# sonlar = list(range(0, 10))
# print(sonlar)
# sonlar2 = list(range(0, 20, 2))
# print(sonlar2)


# min()  va max()  eng kichik va eng katta qiymatni topib beradi
# sum() listdagi barcha sonlar yig'indisini hisoblab beradi
# narhlar = [2000, 3000, 400, 5000]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print(arzon)
# print(qimmat)
# print(jami)

            # RO'YXATNI KESISH
#
# cars = ['bmw', 'volvo', 'hovo', 'gm']
# my_car = cars[0:2]
# my_car2 = cars[1:3]
# print(my_car)
# print(my_car2)
# print(cars[:1])
# print(cars[1:])

        # tuples o'zgarmas ro'yxat
# toy = ('kub', 'kcadrat', 'mol')
# print(type(toy))

# countries = ['USA', 'Jamaica', 'Uzbekistan']
# print(countries)
# print(len(countries))
# print(sorted(countries))
# print(sorted(countries, reverse=True))
# print(countries)
# countries.sort()
# print(countries)
# countries.sort(reverse=True)
# print(countries)

# j_sonlar = list(range(120, 1200, 2))
# print(j_sonlar)
# eng_kichik = min(j_sonlar)
# eng_katta = max(j_sonlar)
# jami = sum(j_sonlar)
# print("Yig'indi: ", jami)
# print("Ayirma: ", eng_katta - eng_kichik)
# print(len(j_sonlar))
# print("Boshidan: ", j_sonlar[:20])
# print("Oxiridan: ", j_sonlar[-20:])
# print("O'rtasidan: ", j_sonlar[260:280])


# taomlar = ['non','tuxum','somsa', 'norin', 'kabob', 'spagetti']
# nonushta = taomlar[:2]
# nonushta.append('choy')
# nonushta.append('sut')
# print(taomlar)
# print(nonushta)
# nonushta = tuple(nonushta)
# print(type(nonushta))

        # FOR TAKRORLANISH OPERATORI
# friends = ['Murod', "Mirdovud", "Bahriddin"]
# # for friend in friends:
# #     print(friend)
#
# for friend in friends:
#     print(f"Hurmatli {friend.upper()} sizni mehmondorchilikga taklif qilaman.")


         # LUG'AT LAR BILAN ISHLASH
my_car = {'rang':'qizil',
          'model':'ferrari'}
# print(my_car['rang'])

talaba1 = {'name':'feruzbek','surname':'baqoyev','birthday':'10th May','father':'baraka'}
# print(f"Men {talaba1['name'].title()} {talaba1['surname'].title()}")

talaba1['kurs'] = 2
talaba1['faculty'] = 'computer science'
# print(talaba1)
# del talaba1['kurs']
# print(talaba1)
#
# ism = talaba1.get('name','Mavjud emas')
# print(ism)
#
# father = {
#     'name':'baraka',
#     'surname':'bozorov',
#     'job':'teacher'
# }
# mother = {
#     'name':'ra\'no',
#     'surname':'abdullaeva',
#     'job':'nurse'
# }
# sister_first = {
#     'name':'nodira',
#     'surname':'baqoyeva',
#     'job':'don\'t work'
# }
# sister_sec = {
#     'name':'nozigul',
#     'surname':'baqoyev',
#     'job':'nurse'
# }
#
# print(f"Otamning ismi {father['name'].title()} ")
# print(f"Onamning ismi {mother['name'].capitalize()}")
# taomlar = {'feruzbek':'osh'}
# print(f"Mening yoqtirgan ovqatim {taomlar['feruzbek']} ")

# dictionary_python = {
#     'integer':'butun son',
#     'float':'o\'nlik son',
#     'list':'lug\'at',
#     'string':'matn',
#     'if':'agar'
# }
#
# nom = input("Kalit so'zni kiriting:  ")
# natija = dictionary_python.get(nom, "Mavjud emas !!!")
# print(natija)
#
# if nom in dictionary_python:
#     print(f"{nom.capitalize()} so'zi {natija} deb tarjima qilinadi.")
# else:
#     print("Bunday so'z mavjud emas !!!")

            # LUG'AT ELEMENTLARI BILAN ISHLASH

# .items()   <- bu metod orqali lug'at ichidagi barcha kalit-qiymat uftliklarni ko'rishimiz mumkin

talaba = {
    'name':'feruzbek',
    'faculty':'computer science',
    'university':'tuit'
}
# tarkib = talaba.items()
# print(tarkib)
#
# for kalit, qiymat in tarkib:
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n")


# .keys()  <-  metodi barcha kalit so'zlarni chiqarib beradi.

# print(talaba.keys())
# for kalit in talaba.keys():
#     print(f"Kalit: {kalit}")


# .values()  <-  metodikalit-qiymat juftligi dagi qiymatlarni chiqarib beradi.

# for qiymat in talaba.values():
#     print(f"Qiymat: {qiymat}")

# set(##)   <-   bu metod takrorlanadigan qiymatlarni chiqarib tashlaydi
# for qiymat in set(talaba.values()):
#     print(f"Qiymat: {qiymat}")

# dictionary_python = {
#     'Boolean':'Mantiqiy qiymat',
#     'Float':'O\'nlik qiymat',
#     'For':'Biror amalni qayta-qayta takrorlash tsikli',
#     'If':'Shartlarni tekshiruvchi operator'
# }
#
# for key, value in dictionary_python.items():
#     print(f"{key} - {value}")

# countries = {
#     'aqsh':'vashington d.c',
#     'uzbekistan':'tashkent',
#     'kazakhstan':'nursultan',
#     'italy':'rome'
# }

# print("Davlatlar :")
# for country in sorted(countries):
#     print(f"{country.upper()}")
#
# print("Poytaxtlar: ")
# for capital in sorted(countries.values()):
#     print(f"{capital.upper()}")

# ask_country = input("Qaysi davlat poytaxtini bilmoqchisiz? ")
# if ask_country.lower() in countries.keys():
#     print(f"{ask_country.title()} ning poytaxti  {countries[ask_country]}")


# taomnoma = {
#     'somsa':5000,
#     'osh':22000,
#     'manti':6000,
#     'non':3000,
#     'salat':10000
# }
# print("Nechta ovqat buyurtma bermoqchisiz?")
# n = int(input(">>> "))
# buyurtma = []
# for i in range(n):
#     taom = input(f"{i} - ovqat nomini kiriting >>> ")
#     buyurtma.append(taom)
#
# for ovqat in buyurtma:
#     if ovqat in taomnoma:
#         print(f"{ovqat.title()} {taomnoma[ovqat]}")
#     else:
#         print(f"Kechirasiz, bizda {ovqat} yo'q")










