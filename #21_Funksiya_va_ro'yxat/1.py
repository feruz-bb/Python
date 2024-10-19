"""
Created time: 17:12:00 05.09.2024
Muallif: Baqoyev Feruzbek Barakayevich
Content: Funksiya va ro'yxat ishlashini o'rganish
"""

def bahola(ismlar):
        baholar = {}
        while ismlar:
            ism = ismlar.pop()
            baho = input(f"{ism.title()}ning bahosini kiriting: ")
            baholar[ism] = baho
        return baholar
# talabalar = ['ali','feruzbek','nurmat', 'bobir']
# baholar = bahola(talabalar[:])
# print(talabalar)
#

def upper_sentence(dictionary):

    sentences = []
    while dictionary:
        sentence = dictionary.pop()
        sentences.append(sentence.title())
    return sentences

# sentences = ['I have got a phone', 'I live in dormitory', 'I wanna go to gym']
# print(upper_sentence(sentences))

