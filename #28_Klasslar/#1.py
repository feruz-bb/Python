"""
Create rime: 8:11:45 29.09.2024
Author: Baqoyev Feruzbek Barakayevich
Content: Classes
"""

class Talaba:
    """Talaba nomli klass"""
    def __init__(self, name, surname, birth_year):
        """Talaba xususiyatlari"""
        self.name = name
        self.surname = surname
        self.birth_year = birth_year

    def introduce(self):
        print(f"Ismim {self.name}, familiyam {self.surname}. {self.birth_year}-yilda tug'ilganman.")
talaba1 = Talaba("Feruzbek", "Baqoyev", 2005)
talaba1.introduce()