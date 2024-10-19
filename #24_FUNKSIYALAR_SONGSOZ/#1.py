"""
Created time: 24:59:00 13.09.2024
Muallif: Baqoyev Feruzbek Barakayevich
Content: Funksiyalar(lambda, map(), filter())
"""
import math

# uzunlik = lambda pi, r: 2*pi*r
# print(uzunlik(math.pi, 10))

# product = lambda x, y: x**y
# print(product(3,2))

# def degree(x):
#     return lambda n:n**x
# kvadrat = degree(2)
# kub = degree(3)
# print(f"3 - kvadrati {kvadrat(3)}, kubi {kub(3)}")

# from math import sqrt
#
# sonlar = list(range(11))
# degrees = list(map(sqrt, sonlar))
# print(degrees)


sonlar = list(range(10))
#
# def degree2(x):
#     return x**2
# print(list(map(degree2, sonlar)))


# kvadratlar = list(map(lambda x:x**2, sonlar))
# print(kvadratlar)

# kvadratlar = []
# for son in sonlar:
#     kvadratlar.append(son*son)
# print(kvadratlar)

# a = [5,8,9,12]
# b = [4,2,3]
# a_plus_b = list(map(lambda x, y: x+y, a, b))
# print(a_plus_b)


# ismlar = ['hasan', 'husan', 'ali']
# print(list(map(lambda matn:matn.upper(), ismlar)))

# import random as r
# sonlar = r.sample(range(100), 10)
# def juftmi(x):
#     """x juft bo'lsa TRUE, aks holda False qaytaruvchi funksiya"""
#     return x%2 == 0
# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)

# mevalar = ['olma', 'anor', 'anjir']
# mevalar_b = list(filter(lambda matn:matn.startswith('a'), mevalar))
# print(mevalar_b)
# mevalar2 = list(filter(lambda meva:len(meva)<=4, mevalar))
# print(mevalar2)
