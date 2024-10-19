"""
Created time: Idon't know.
Muallif: Baqoyev Feruzbek Barakayevich
Content: funksiyalardan iborat fayl
"""

def avto_info(kompaniya, model,rangi, korobka, yili, narhi = None):
    avto = {
        'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'korobka':korobka,
        'yili':yili,
        'narhi':narhi
    }
    return avto

def avto_kirit():
    """Avtomobil haqida to'liq ma'lumotni lug'at ko'rinishida shakllantirib ro'yxatga qo'shadi"""
    avtolar = []
    while True:
        kompaniya = input("Ishlab chiqaruvchi nomini kiriting: >>> ")
        model = input("Mashina modelini kiriting: >>> ")
        rang = input("Mashinaning rangini kiriting: >>> ")
        korobka = input("Mashina korobkasi qanaqa: >>> ")
        yili = input("Nechanchi yilda ishlab chiqarilgan: >>> ")
        narhi = input("Narhi: >>> ")
        avtolar.append(avto_info(kompaniya,model,rang,korobka,yili, narhi))
        ask = input("Yana avtomobil qo'shasizmi? (yes/no) >>> ")
        if ask == 'no':
            break
    return avtolar

def avto_print(info_avto):
    print(f"{info_avto['rang'].title()} {info_avto['kompaniya'].upper()} "
          f"{info_avto['model'].title()} {info_avto['korobka'].title()} korobka"
          f" {info_avto['yili']}, {info_avto['narhi']}$")