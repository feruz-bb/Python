"""
Created time: 17:32:25 05.09.2024
Muallif: Baqoyev Feruzbek Barakayevich
Content: Moslashuvchan funksiyani o'rganish
"""

def summa(*sonlar):
    natija = 0
    for n in sonlar:
        natija += n
    return natija
print(summa(4,5,5,6,4,7,8,8,9,))

def avto_info(kompaniya, model, **malumotlar):
    malumotlar['kompaniya'] = kompaniya
    malumotlar['model'] = model
    return malumotlar
print(avto_info('GM', 'Gentra', narh = 13000, yili = 2005))

