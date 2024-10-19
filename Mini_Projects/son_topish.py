import random as r
print("Keling o'ylagan sonni topish o'yinini o'ynaymiz !!! :)")
person_guest = 1
pc_guest = 1
while True:
    pc_number = r.randint(1,10)
    print("1 dan 10 gacha son o'yladim. Topa olasizmi ?")
    while True:
        son = int(input(">>> "))
        if pc_number > son:
            print("Men o'ylagan son bundan kattaroq. ")
            person_guest += 1
            continue
        elif pc_number < son:
            print("Men o'ylagan son bundan kichikroq. ")
            person_guest += 1
            continue
        else:
            print(f"TOPDINGIZ !!! :-) {pc_number} sonini o'ylagan edim. ", end='')
            print(f"{person_guest} ta taxmin bilan topdingiz. Tabriklayman !")
            break
    print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
    input("Son o'ylagan bolsangiz 'enter' tugmasini bosing")
    while True:
        a, b = 1, 10
        person_number = r.randint(a,b)
        ask = str(input(f"Siz {person_number} sonini o'yladingiz. to'g'ri (T), men o'ylagan bundan kattaroq (+)"
                        f", men o'ylagan bundan kichikroq (-) ? >>> ").lower())
        if ask == '+':
            a = person_number + 1
            pc_guest += 1
            continue
        elif ask == '-':
            b = person_number - 1
            pc_guest += 1
            continue
        else:
            print(f"Soningizni {pc_guest} ta taxmin bilan topdim !")
            break
    if person_guest == pc_guest:
        print(f"DURRANG ! Ikkalamiz ham {person_guest} ta taxmin bilan topdik. ")
    elif person_guest > pc_guest:
        print(f"Men {pc_guest} ta taxmin bilan g'olib bo'ldim.")
    else:
        print(f"Siz {person_guest} ta taxmin bilan g'olib bo'ldingiz !")
    ask_continue = input("Yana o'ynaymizmi ? ha(1), yo'q(0)")
    if ask_continue == 1:
        person_guest = 1
        pc_guest = 1
        continue
    else:
        print("O'yin qiziqarli bo'ldi XAYR ! :)")
        break

