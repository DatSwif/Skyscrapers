#клас внутрішньоігрового меню, що містить ігрове поле та додатковий інтерфейс
#
#Використані імпортовані методи та константи:
from Button import Button # створення кнопок ігрового меню
from Box import Box # створення текстових полів
from Timer import Timer # створення таймера
from pygame import draw # розміщення чорного квадрату на весь екран для його очищення
from GameBoard import GameBoard # створення ігрового поля
from COLORS import GREY127, GREEN, RED, BLACK # константи кольорів

class InGame(object):
    """Інтерфейс у процесі гри"""
    #self : InGame - сам об'єкт, 
    #scr : Surface - екран, 
    #size : int - розмір внутрішнього поля, 
    #difficulty : int - складність
    def __init__(self, scr, size, difficulty):
        #self.gameboard : GameBoard - ігрове поле
        self.gameboard = GameBoard(scr, size, difficulty)
        #self.numbers : list[Button] - кнопки для встановлення цифр на ігровому полі
        self.numbers = []
        #i : int - ітераційна, додавання кнопок цифр
        for i in range(1, 10):
            if i > size:
                self.numbers.append(Button(scr, ((13+((i-1)%3))*50+1, (1+((i-1)//3))*50+1, (14+((i-1)%3))*50-1, (2+((i-1)//3))*50-1), "X", 25, GREY127, GREY127, False))
            else:
                self.numbers.append(Button(scr, ((13+((i-1)%3))*50+1, (1+((i-1)//3))*50+1, (14+((i-1)%3))*50-1, (2+((i-1)//3))*50-1), str(i)))

        #self.title : Box - текстове поле, розмір та складність
        self.title = Box(scr, (13*50, 4*50, 16*50, 6*50), str(size) + " " + ["Easy", "Medium", "Hard"][difficulty], 50)
        #self.timer : Timer - таймер
        self.timer = Timer(scr)
        #self.indicator : Box - показує чи правильно розв'язано головоломку
        self.indicator = Box(scr, (13*50, 7*50, 16*50, 9*50))

        #self.deleteButton : Button - кнопка видалення цифри з комірки
        self.deleteButton = Button(scr, (13*50+1, 9*50+1, 14*50-1, 10*50-1), "del", 16)
        #self.checkButton : Button - кнопка перевірки на правильність
        self.checkButton = Button(scr, (14*50+1, 9*50+1, 15*50-1, 10*50-1), "check", 16)
        #self.restartButton : Button - кнопка перезапуску поточного рівня
        self.restartButton = Button(scr, (15*50+1, 9*50+1, 16*50-1, 10*50-1), "again", 16)
        ###self.undoButton = Button(scr, (13*50+1, 10*50+1, 14*50-1, 11*50-1), "<", 25, GREY127, GREY127, False)
        ###self.redoButton = Button(scr, (14*50+1, 10*50+1, 15*50-1, 11*50-1), ">", 25, GREY127, GREY127, False)
        #self.hintButton : Button - кнопка підказки (розмістити правильну цифру у випадкову комірку)
        self.hintButton = Button(scr, (15*50+1, 10*50+1, 16*50-1, 11*50-1), "hint", 16)
        ###self.pencilmarkButton = Button(scr, (13*50+1, 11*50+1, 14*50-1, 12*50-1), "marks", 16, GREY127, GREY127, False)
        ###self.colorButton = Button(scr, (14*50+1, 11*50+1, 15*50-1, 12*50-1), "color", 16, GREY127, GREY127, False)
        #self.autosolveButton : Button - авторозв'язання
        self.autosolveButton = Button(scr, (15*50+1, 11*50+1, 16*50-1, 12*50-1), "auto", 16)

    #self : InGame - сам об'єкт, 
    #scr : Surface - екран, 
    #keyboard : Keyboard - дані про клавіатуру, 
    #mouse : Mouse - дані про мишу, 
    #state : list[str, int, int, bool] - поточний стан перемикача меню
    def update(self, scr, keyboard, mouse, state): #update : None - оновлення всіх кнопок, текстових полів, таймера та ігрового поля
        
        draw.rect(scr, BLACK, (0, 0, 850, 650))
        self.title.update()
        self.indicator.update()
        
        if keyboard.escape == True:
            state[0] = "menu"

        #activating buttons with keyboard
        #i : int - ітераційна, перевірка всіх кнопок
        for i in range(9):
            if keyboard.num[i+1] == True:
                self.numbers[i].update(mouse, None, None, None, None, True)
            else:
                self.numbers[i].update(mouse)

        if keyboard.num[0] == True:
            self.deleteButton.update(mouse, None, None, None, None, True)
        else:
            self.deleteButton.update(mouse)

        if keyboard.check == True:
            self.checkButton.update(mouse, None, None, None, None, True)
        else:
            self.checkButton.update(mouse)

        if keyboard.restart == True:
            self.restartButton.update(mouse, None, None, None, None, True)
        else:
            self.restartButton.update(mouse)

        #self.undoButton.update(mouse)
        #self.redoButton.update(mouse)

        if (keyboard.solve == True) and (not keyboard.ctrl == True):
            self.hintButton.update(mouse, None, None, None, None, True)
        else:
            self.hintButton.update(mouse)

        #self.pencilmarkButton.update(mouse)
        #self.colorButton.update(mouse)

        if (keyboard.solve == True) and (keyboard.ctrl == True):
            self.autosolveButton.update(mouse, None, None, None, None, True)
        else:
            self.autosolveButton.update(mouse)
        
        # buttons' special abilities
        #i : int - ітераційна, перевірка кнопок з цифрами
        for i in range(9):
            if self.numbers[i].isPressed:
                keyboard.num[i+1] = True
        if self.deleteButton.isPressed:
            keyboard.num[0] = True

        if self.checkButton.isPressed:
            if self.gameboard.check() == True:
                self.timer.update(True)
                self.indicator.update("Correct!", None, None, GREEN)
            else:
                self.indicator.update("Incorrect!", None, None, RED)
        elif mouse.isDown or keyboard.isDown:
            self.indicator.update("")
        else:
            self.indicator.update()

        if self.restartButton.isPressed:
            self.gameboard.reset(mouse)
            self.timer.reset()
            self.timer.update(False)

        if self.autosolveButton.isPressed or state[0] == "autosolve":
            state[0] = "ingame_normal"
            self.gameboard.autosolve(mouse) # place all numbers
        elif self.hintButton.isPressed:
            self.gameboard.hint(mouse) # verify if all numbers already placed are correct, place a number      
        
        #finally, updating the gameboard
        self.gameboard.update(keyboard, mouse, state)
        self.timer.update()