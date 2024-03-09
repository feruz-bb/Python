# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 14:10:44 2024

Muallif: Baqoyev Feruzbek Barakayevich
"""
# TASK 1
# Maqsad: oila a`zolari uchun lug`at yaratish va uni konsolga chiqarish
"""
otam = {
        'ism':'Baraka',
        'familiya':'Bozorov',
        'sharif':'Baqoyevich',
        'yosh':'58',
        't_yil':'1966'
        }
onam = {
        'ism':'Ra\'no',
        'familiya':'Abdullayeva',
        'sharif':'Fazliddinovna',
        'yosh':'53',
        't_yil':'1971'
        }

print(f"Otamning ismi {otam['ism']}, {otam['yosh']} yoshda")
"""

# TASK 2
# Maqsad: sevimli taomlar lug`atini tuzish kamida uchta insonning 
#        taomini konsolga chiqarish
"""
taomlar = {
    'Feruzbek':'manti',
    'Murodjon':'lavash',
    'Ahmadjon':'Lag\'mon'
    }

print(f"Feruzbekning sevimli taomni {taomlar['Feruzbek']}")
"""

# TASK 3
# Maqsad: pyhton izohli lug`atini tuzish va unga murojaat qilish
"""
izoh = {
        'integer' : 'Butun son',
        'float' : 'Haqiqiy son',
        'string' : 'Matn',
        'list' : 'Ro\'yxat',
        'tuple' : 'O\'zgarmas ro\'yxat'        
        }

kalit = input("Kalit so\'z kiriting >>> ")
print(izoh.get(kalit.lower(),'Bunday so\'z mavjud emas!'))
"""