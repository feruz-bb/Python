# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 18:42:03 2023

@author: baqoy
"""

# ismlar = ["Bekzod", "Botir", "Asadbek", "Avazbek", "Aziz"]
# for ism in ismlar:
#     print(f"Assalom-u alaykum {ism}")
# print(f"Kod {len(ismlar)} marta takrorlandi.")


# for n in range(11,100,2):
#     print(f"{n} ning kubi {n**3}.")

# kinolar = []
# for kino in range(1,6):
#     kinolar.append(input(f"{kino} - kino nomi >>> "))
# print(kinolar)


u_soni = int(input("Bugun nechta inson bilan uchrashdingiz >>> "))
ismlar = []
for n in range(0,u_soni):
    ismlar.append(input(f"{n+1}-insonning ismi >>> "))
print(ismlar)