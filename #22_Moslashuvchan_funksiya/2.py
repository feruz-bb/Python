"""
Created time: 12:42:20 07.09.2024
Muallif: Baqoyev Feruzbek Barakayevich
Content: Moslashuvchan_ Funksiya (amaliyot)
"""

## TASK 1
def kopaytma(*sonlar):
    natija =1
    for son in sonlar:
        natija *= son
    return natija
# print(kopaytma(4,5,6,4,5))

## TASK 2
def student_info(ism, familiya, **talaba):
    talaba['ism'] = ism
    talaba['familiya'] = familiya
    return talaba
# print(student_info('feruznek', 'baqoyev', kurs = 1, universitet = 'TUIT'))
