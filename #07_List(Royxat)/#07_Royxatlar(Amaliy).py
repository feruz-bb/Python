# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 17:13:23 2023

@author: pc
"""

ismlar = ["Bekzod", "Asadbek", "Ogabek"]
print(f"Salom {ismlar[0]} bugun bayramga boramizmi ?")
print(f"Salom {ismlar[1]} bugun bayramga boramizmi ?")
print(f"Salom {ismlar[2]} bugun bayramga boramizmi ?")

t_shaxslar = ["Abu ali Ibn Sino", "Abu Rayhon Beruniy"]

z_shaxslar = ["Shavkat Mirziyoyev", "Baraka Bozorov"]

print(f"Men tarixiy shaxslardan {t_shaxslar.pop(0)} bilan zamonaviy shaxslardan" 
      f" esa {z_shaxslar.pop(0)} bilan suhbat qilishni istar edim.")

friends = []
friends.append("Bekzod")
friends.append("Sherali")
friends.append("Bekmurod")

friends.remove("Bekzod")

friends.insert(0, "Feruzbek")
friends.insert(1, "Murod")
friends.insert(4, "Alijon")

mehmonlar = []
mehmonlar.append(friends[1])
