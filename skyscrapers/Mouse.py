#Клас, що зберігає дані про мишу в реальному часі
#
#Використані імпортовані методи та константи:
from pygame import mouse
#для зчитування даних про мишу

class Mouse():
    """Записує позицію курсору та натискання ЛКМ"""
    #self : Mouse - сам об'єкт
    def __init__(self):
        #self.x : int - координата курсора х
        self.x : int
        #self.y : int - координата курсора у
        self.y : int
        #self.isDown : bool - чи натиснута ЛКМ
        self.isDown = False

    #self : Mouse - сам об'єкт
    def update(self): #update : None - оновлення даних про мишу
        self.x = mouse.get_pos()[0]
        self.y = mouse.get_pos()[1]
        if mouse.get_pressed()[0]:
            if self.isDown == False:
                self.isDown = True
            elif self.isDown:
                self.isDown = None
        else:
            self.isDown = False

    #self : Mouse - сам об'єкт, 
    #coords : tuple[int, int, int, int] - координати, що перевіряються
    def intersects(self, coords): #intersects : bool - визначає, чи знаходиться курсор миші в заданих координатах
        if (self.x >= coords[0]) and (self.x <= coords[2]) and (self.y >= coords[1]) and (self.y <= coords[3]):
            return True
        else:
            return False