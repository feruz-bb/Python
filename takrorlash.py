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

kocha = input("Ko'changiz nomini kiriting: ")
mahalla = input("Mahalla nomini kiriting: ")
tuman = input("Tumaningiz nomini kiriting: ")
viloyat = input("Viloyatingiz nomini kiriting: ")

addres = f"{kocha.capitalize()} ko'chasi, {mahalla.capitalize()} mahallasi, {tuman.capitalize()} tumani, {viloyat.capitalize()} viloyati"
print(addres)
