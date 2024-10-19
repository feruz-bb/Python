"""
Create time: 13:11:18 31.08.2024
Muallif Baqoyev Feruzbek Barakayevich
Maqsad: While tsikli (amaliyot)
"""

# TASK 1
# mf_books = []
# print("Yoqtirgan kitoblaringiz nomini kiriting. ")
# print("Dasturni to'xtatish uchun 'stop' soz'ini yozing. ")
# ask = ''
# while ask != 'stop':
#     ask = input(">>> ")
#     if ask != 'stop':
#         mf_books.append(ask)
# print(f"Siz yoqtirgan kitoblar : ")
# for book in mf_books:
#     print(f"{book.upper()}", end=" ")

# TASK 2
# ask = ''
# narxlar = {
#     '0-7':2000,
#     '7-18':3000,
#     '18-65':10000,
#     '65-':'bepul'
# }
# print("Chipta narxini bilish uchun yoshingizni kiriting. ")
# print("(Dasturni to'xtatish uchun 'stop' buyrug'idan foydalaning.)")
# while True:
#     ask = input(">>> ")
#     if ask != 'stop':
#         if ask.isnumeric():
#             ask = int(ask)
#             if ask < 7:
#                 print(f"{ask} yosh uchun chipta narxi {narxlar['0-7']} so'm")
#             elif  7 <= ask < 18:
#                 print(f"{ask} yosh uchun chipta narxi {narxlar['7-18']} so'm")
#             elif 18 <= ask < 65:
#                 print(f"{ask} yosh uchun chipta narxi {narxlar['18-65']} so'm")
#             elif ask >= 65 :
#                 print(f"{ask} yosh uchun chipta {narxlar['65-']} ")
#         else:
#             print("Javobingiz faqat raqam shaklida bo'lishi lozim !!!")
#             continue
#     else:
#         print("Sayohatga kelganingiz uchun raxmat !!!")
#         break

