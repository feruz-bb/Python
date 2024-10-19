"""
Created time: 17:50:58
Muallif: Baqoyev Feruzbek Barakayevich
Maqsad: Amaliyot
"""

## TASK 1
# buyurtmalar = []
# print("Buyurtmalaringizni nomini kiriting. ")
# print("(dasturni to'xtatish uchun 'stop' buyrug'idan foydalaning) ")
# while True:
#     meal = input(">>> ")
#     if meal != 'stop':
#         buyurtmalar.append(meal)
#     else:
#         print("Buyurtmalaringiz uchun raxmat!!!")
#         break
# print("Sizning buyurtmalaringiz >>> ", end='')
# while buyurtmalar:
#     print(buyurtmalar.pop().upper(), end=' ')


## TASK 2
# prices = {}
# print("Elektron bozorga ma'lumotlar kiritish. ")
# print(" ( ma'lumotlar kiritishni to'xtatish uchun 'stop' buyrug'ini yozing) ")
# print("Mahsulotni kiriting ")
# while True:
#     print(">>> ", end='')
#     object = input()
#     if object != 'stop':
#         price = int(input(f"{object} - narxini yozing >>> "))
#         prices[object] = price
#     else:
#         print("Ma'lumotlar uchun raxmat !!!")
#         break
#
# for object, price in prices.items():
#     print(f"{object.upper()} -> {price} so'm")

## TASK 3
# prices = {
#     'non':5000,
#     'osh':22500,
#     'olma':9000,
#     'grenki':4200,
#     'norin':35000,
#     'salat':8000,
#     'manti':7000
# }
# no_buyurtma = []
# buyurtmalar = []
# print("Xush kelibsiz !!!")
# print("Nimalar buyurtma qilmoqchisiz ?")
# print(" (buyurtmani yakunlagandan so'ng 'stop' buyrug'ini bering) ")
# total = 0
# ask = ''
# while True:
#     ask = input(">>> ")
#     if ask != 'stop':
#        buyurtmalar.append(ask)
#     else:
#         print("Tashrifingiz uchun raxmat !!!")
#         break
# print("\n    Sizning buyurtmalaringiz >>> ")
# for buyurtma in buyurtmalar:
#     if buyurtma in prices.keys():
#         print(f"{buyurtma}", end=" ")
#         total += prices[buyurtma]
#     else:
#         no_buyurtma.append(buyurtma)
# print("\n     Quyidagilar bizda yo'q >>> ")
# for no in no_buyurtma:
#     print(f"{no}", end=" ")
# print(f"\nJami: {total}")



