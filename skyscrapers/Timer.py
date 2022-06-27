#Об'єкт таймера, що записує час із початку розв'язання головоломки
#
#Використані імпортовані методи та константи:
from time import time
from Box import *

class Timer(Box):
    """Таймер, що записує час із початку розв'язання головоломки"""
    #self : Timer - сам об'єкт, 
    #scr : Surface - екран
    def __init__(self, scr): 
        #self.begin : int - момент початку розв'язання
        self.begin = int(time())
        #self.solved : bool - чи розв'язана головоломка
        self.solved = False
        #self.text : str - відформатований текст таймера
        self.text = "00:00"
        #self.sec : int - секунди
        self.sec : int
        #self.min : int - хвилини
        self.min : int
        #self.hrs : int - години
        self.hrs : int
        #self.strSec : str - секунди у форматі рядка
        self.strSec : str
        #self.strMin : str - хвилини у форматі рядка
        self.strMin : str
        #self.strMin : str - години у форматі рядка
        self.strHrs : str
        super().__init__(scr, (13*50, 6*50, 16*50, 7*50), self.text, 25)

    #self : Timer - сам об'єкт, 
    #solved : bool - чи чи розв'язана головоломка
    def update(self, solved = None): #update : None - оновлення таймера. Таймер зупиняється у разі успішної перевірки розв'язання задачі
        if solved != None:
            self.solved = solved
        if not self.solved:
            #sec : int - кількість секунд від початку розв'язання
            sec = int(time()) - self.begin
            self.sec = sec % 60
            self.min = (sec // 60) % 60
            self.hrs = sec // 3600
            if self.sec < 10:
                self.strSec = "0" + str(self.sec)
            else:
                self.strSec = str(self.sec)
            if self.min < 10:
                self.strMin = "0" + str(self.min)
            else:
                self.strMin = str(self.min)
            self.strHrs = str(self.hrs)
            if self.hrs == 0:
                self.text = self.strMin + ":" + self.strSec
            else:
                self.text = self.strHrs + ":" + self.strMin + ":" + self.strSec
        super().update(self.text)

    #self : Timer - сам об'єкт
    def reset(self): #reset : None - перезапуск таймера, якщо гравець почав розв'язувати головоломку спочатку
        self.begin = int(time())