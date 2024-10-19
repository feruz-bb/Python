"""
Created time: 18.09.2024 11:21:05
Author: Baqoyev Feruzbek Barkayevich
Content: So'z topish o'yinini tayyorlash
"""
import random
from uzwords import words

def get_word():
    word  = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)
    return word.upper()
def display(type_word, uzword):
    list_word = list(type_word)
    list_uzword = list(uzword)
    new_word = []
    for harf in list_uzword:
        if harf in list_word:
            new_word.append(harf)
        else:
            new_word.append('-')

    for m in new_word:
        print(m.upper(),end='')

def son_top():
    pc_word = get_word().upper()
    word_length = len(pc_word)
    print(f"Мен {word_length} хонали сон ўйладим. Топа оласизми ?")
    print(word_length*'-')
    promp_words = []
    while True:
        ask_word = input("\nҲарф киритинг: ").upper()
        promp_words.append(ask_word)
        if ask_word in list(pc_word):
            print(f"{ask_word} ҳарфи тўғри.")
            display(ask_word,pc_word)
            promp_words.append(ask_word)
        else:
            print(f"Бундай ҳарф йўқ")
            display(promp_words, pc_word)
        re_word = display(promp_words, pc_word)
        if re_word == pc_word:
           print(f"Табриклайман. {pc_word} сўзини {len(promp_words)} та уринишда топдингиз.")
           break
        else:
            continue
son_top()
