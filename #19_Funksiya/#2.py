"""Created time: 18:52:11 01.09.2024
Muallif: Baqoyev Feruzbek Barakayevich
Maqsad: Funksiya (Amaliyot)
"""

## TASK 1
def wiyb():
    name = input("Ismingiz kim ? >>>> ")
    age = int(input("Yoshingiz nechada >>>"))
    print(f"{name.title()} {2024 - age} yilda tug'ilgan.")

## TASK 2
def kvkub(number):
    print(f"Kvadrati: {pow(number,2)}")
    print(f"Kubi: {pow(number,3)}")

## TASK 3
def jufttoq(number):
    if number %2 == 0:
        print(f"{number} -> juft son")
    else:
        print(f"{number} -> toq son")
## TASK 4
def kattasi(number1, number2):
    if number1 < number2:
        print(f"Kattasi: {number2}")
    elif number1 == number2:
        print(f"Sonlar teng. ")

def daraja_oshir(number, degree):
    print(f"{number} ning {degree} - darajasi {pow(number,degree)} ga teng.")

def kv_oshir(number):
    print(f"{number} ning kvadrati {number**2} ga teng.")
def bolinishga_tekshir(number):
    bolinadi = []
    for i in range(2,11):
        if number %i == 0:
            bolinadi.append(i)
    print(f"{number} ushbu sonlarga qoldiqsiz bo'linadi >>> ", end="")
    for n in bolinadi:
        print(f"{n}",end=" ")