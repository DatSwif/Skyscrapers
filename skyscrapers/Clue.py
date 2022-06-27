#Клас "підказок" - комірок з боків поля
#
#Використані імпортовані методи та константи:
from Box import Box #створення об'єкту через суперклас
from COLORS import BLACK, GREY175 # константи кольорів

class Clue(Box):
    """Цифри з боків ігрового поля"""
    #self : Clue - сам об'єкт, 
    #scr : Surface - екран, 
    #coords : tuple[int, int, int, int] - координати, 
    #number : int - номер у комірці, 
    #textsize : int - розмір тексту
    def __init__(self, scr, coords, number, textsize): 
        #self.number : int - номер у комірці
        self.number = number
        if self.number == 0:
            super().__init__(scr, coords, "", textsize)
        else:
            super().__init__(scr, coords, number, textsize, BLACK, GREY175)

    #self : Clue - сам об'єкт
    def update(self): #update : None - оновлення зображення
        super().update()
