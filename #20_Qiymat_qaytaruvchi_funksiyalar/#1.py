"""
Created time: 22:07:40 02.09.2024
Muallif: Baqoyev Feruzbek Barakayevich
Maqsad: Qiymat qaytaruvchi funksiyalarni o'rganish
"""

def toliq_ism(name, surname, otasining_ismi = ''):
    """To'liq ismni qaytaruvchi funksiya"""
    if otasining_ismi:
        full_name = f"{name.title()} {surname.title()} {otasining_ismi.title()}"
    else:
        full_name = f"{name.title()} {surname.title()}"
    return full_name

talaba1 = toliq_ism('feruzbek', 'baqoyev', 'barakayevich')
print(talaba1)

## Funksiya ichidagi o'zgaruvchilar local variables deyiladi. Ular faqat funksiya ichida mavjud bo'ladi.
## ularga tashqaridan murojaat etib bo'lmaydi.

def avto_info(make,model,colour, korobka, year, price=None):
    avto = {
        'kompaniya':make,
        'model':model,
        'rang':colour,
        'korobka':korobka,
        'yil':year,
        'narx':price
    }
    return avto
# avto1 = avto_info('GM', 'Gentra', 'Black', "Auto", 2024)
# avto2 = avto_info("GM", "Malibu", "White", "Auto", 2023, 23000)
# avtolar = [avto1, avto2]
# print("Onlayn bozordagi mavjud avtomashinalar. ")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].upper()}, Narxi: {narx}")

def oraliq(min,max, qadam = 1):
    sonlar =[]
    while min < max:
        sonlar.append(min)
        min += qadam
    return sonlar
#print(oraliq(3, 10, 2))
