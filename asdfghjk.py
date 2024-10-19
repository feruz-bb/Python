import math as m

def factorial(x):
    x = int(x)
    natija = 1
    for i in range(1,x+1):
        natija *= i
    return natija

print(factorial(11))
print(factorial(3))