# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 15:04:57 2024

Muallif: Baqoyev Feruzbek Barakayevich
Maqsad: Lug`at elementlari bilan ishlash
"""

# .items() METODI

talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
    #print(f"Kalit: {kalit}")
    #print(f"Qiymat: {qiymat} \n")
    
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
"""
for k, q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q.title()}")
"""

# .keys() METODI
"""
print(telefonlar.keys())
"""

# sorted() METODI - lug`at elemntlarini tartiblab chiqaradi
"""
for mahsulot in sorted(telefonlar):
    print(mahsulot)
"""

# .values() metodi - lug`atdagi qiymatlarni chiqarib beradi
"""
print(telefonlar.values())
for telefon in telefonlar.values():
    print(telefon)
"""

# takrorlangan qiymatlarni chiqarmaslik uchun set() funksiyasidan foydalanamiz


