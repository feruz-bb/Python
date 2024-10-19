"""
Created Time: 17:18:18 01.09.2024
Muallif: Baqoyev Feruzbek Barakayevich
Content: Funksiya
"""

def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu aleykum")

## Qiymat qabul qiluvchi funksiya
def salom_ber_ism(ism):
    """Ismi bilan salom berish"""
    print(f"Assalomu aleykum, {ism.title()}")


## DOCSTRING - funksiya badaning ilk qatorida """ something """  kabi yoziladi.
## salom_ber_ism(ism)  ism -> parametr  'feruzbek' degan qiymat -> argument

def toliq_ism(name, surname):
    """To'liq ismni chiqarib beradi.
    Funksiya 2 ta parametrdan iborat. name va surname"""
    print(f"Foydalanuvchi ismi: {name.title()}\n"
          f"Foydalanuvchi familiyasi: {surname.title()}")
def hoay(name, year):
    """Fydalanuvchi yoshini hisoblaydigan dastur"""
    print(f"{name.title()} {2024-year} yoshda")