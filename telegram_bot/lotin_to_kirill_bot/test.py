# chocolate = 2
# milk = 5
# coffee = 3
# prices = {
#     'milk':11500,
#     'chocolate':21000,
#     'coffee':3500
# }
# result = chocolate*prices['chocolate'] + milk*prices['milk'] + coffee*prices['coffee']
# print(result

## ISSUE - 2
""" first = 3
second = first + 4
third = second + first
print(f"First: {first} \nSecond: {second} \nThird: {third}")"""

## ISSUE - 3
"""side = 5
perimetr = side * 4
print(perimetr)"""

""" PROBLEMS """
#1
# length = 100
# print(f"{length} cm = {length/100} m")

#2
# kg = 50000
# print(f"{kg} kg = {kg/1000} t")

#3
# bytes = 32
# print(f"{bytes} byte = {bytes*8} bit")

#4
# numbers = [5,6,5,6,3,40]
# result = 0
# for i  in numbers:
#     result += i
# print(f"Sum: {result}")


#4

# import random
# numbers = []
# sum_negatives = 0
# for n in range(10):
#     numbers.append(random.randint(-100,100))
# for number in numbers:
#     if number < 0:
#         sum_negatives += number
# sorted_numbers = sorted(numbers)
# min_index = numbers.index(min(numbers))
# max_index = numbers.index(max(numbers))
# if min_index < max_index:
#     min_to_max = numbers[min_index:max_index]
# else:
#     min_to_max = numbers[max_index:min_index]
# print(f"Numbers: {numbers}")
# print(f"Sum of negatives: {sum_negatives}")
# print(f"Number of between minimum to maximum: {min_to_max}")
# print(f"Growth order: {sorted_numbers}")

#5

# a = 15
# b = 75
# square_side = 5
# new_a = int(a/square_side) * square_side
# new_b = int(b/square_side) * square_side
# numbers_square = (new_a * new_b)/ (square_side**2)
# print(numbers_square)
# my_list = [4, 5 , 6 ,7]
# my_list.remove(7)
# print(my_list)


""" 27.  Days of the week are numbered as follows. 0 Sunday, 1 Monday, 2 Tuesday, 3 
Wednesday, 4 Thursday, 5 Friday, 6 Saturday. Given an integer K, which means the day 
of the current year, the value is in the range 1-365. If it is clear that January 1st is a 
Thursday, determine which value of the number K corresponds  """

# day = int(input("Number of the day: "))
# mod_formula = day % 7
# if mod_formula == 1:
#     day_name = "Thursday"
# elif mod_formula == 2:
#     day_name = "Friday"
# elif mod_formula == 3:
#     day_name = "Saturday"
# elif mod_formula == 4:
#     day_name = "Sunday"
# elif mod_formula == 5:
#     day_name = "Monday"
# elif mod_formula == 6:
#     day_name = "Tuesday"
# else:
#     day_name = "Wednesday"
#
# print(f"Day name: {day_name}")
#

""" Ikkita son va ular orasidagi kvadratlarning yig'indisining o'rta arifmetigi"""

# a = int(input("a >>> "))
# b = int(input("b >>> "))
# mylist = []
# value = 0
# for i in range(a+1,b):
#     mylist.append(i*i)
# for number in mylist:
#     value += number
# result = value/len(mylist)
# print(result)

""" Berilgan sonning kasr qismi va butun qismini alohida ajratib hisoblash"""

import math

# float_list = [12.1,25.6,14.5]
# qoldiq = 0
# butun = 0
# for number in float_list:
#     i = 0
#     butun_qism = int(number)
#     butun += butun_qism
#     qoldiq += number - butun_qism
#     i += 1
# print(butun)
# print(round(qoldiq,2))
# print(float_list)

""" So'zni alifbo tartibida tartiblash"""
# word = input("Type word: ")
# sorted_word = sorted(word)
# print(sorted_word)

"""Eng kichigining indeksi"""
# list = [5,6,8,7,9,2,1.5,6]
# print(f"Index of minimum: {list.index(min(list))}")

"""Ro'yxat ichida element borligini tekshiruvchi dastur"""

mylist = [5,6,3,8,4,2,8,6,12,65,34,98,25,14,21]
number = input("Enter a number >>> ")
if number in mylist:
    result = "Element topilmadi :("
else:
    result = "Element topildi :)"
print(result)