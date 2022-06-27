#Клас комірок у середині ігрового поля
#
#Використані імпортовані методи та константи:
from Box import Box # для створення об'єкту через суперклас
from Mouse import Mouse # для зчитування параметрів миші
from COLORS import GREY200, GREY225, GREY127, GREY175, GREEN, BLUE # константи кольорів

class Cell(Box):
    """Комірка всередині ігрового поля"""
    #self : Cell - сам об'єкт, 
    #scr : Surface - екран, coords : tuple[int, int, int, int] - координати комірки, 
    #number : int - номер у комірці, 
    #textsize : int - розмір тексту, 
    #changeable : bool - чи можна змінити цифру в комірці
    def __init__(self, scr, coords, number, textsize, changeable = True):
        #self.number : int - номер у комірці
        self.number = number
        #self.changeable : bool - чи можна змінити цифру в комірці
        self.changeable = changeable
        if self.number != 0:    
            super().__init__(scr, coords, self.number, textsize, GREY200, GREY225)
        else:
            super().__init__(scr, coords, "", textsize, GREY200, GREY225)
        #self.isSelected : bool - чи виділена комірка
        self.isSelected = False
        #self.isHovered : bool - чи курсор миші над коміркою
        self.isHovered = False

    #self : Cell - сам об'єкт, 
    #mouse : Mouse - дані про мишу, 
    #number : int - номер у комірці, 
    #selected : bool - чи виділена комірка авторозв'язувачем
    def update(self, mouse, number = None, selected = False): #update : None - Перевірка чи занесено нове значення в комірку, оновлення даних і зображення
        if not self.changeable:
            super().update(None, None, GREY127, GREY175)
        else:
            if mouse.isDown:
                if mouse.intersects(self.coords):
                    self.isSelected = True
                elif (not mouse.intersects((13*50, 1*50, 16*50, 4*50))) and not (mouse.intersects((13*50, 9*50, 16*50, 12*50))):
                    self.isSelected = False
            elif mouse.intersects(self.coords):
                self.isHovered = True
            else:
                self.isHovered = False

            if self.isSelected or selected:
                if number != None:
                    self.number = number
                if self.number != 0:
                    super().update(self.number, self.textSize, GREEN)
                else:
                    super().update("", self.textSize, GREEN)
            elif self.isHovered:
                if self.number != 0:
                    super().update(self.number, self.textSize, BLUE)
                else:
                    super().update("", self.textSize, BLUE)
            elif self.number != 0:
                super().update(self.number, self.textSize, GREY200)
            else:
                super().update("", self.textSize, GREY200)