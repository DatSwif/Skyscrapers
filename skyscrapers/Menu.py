#Клас для позначення інтерфейсу в головному меню гри
#
#Використані імпортовані методи та константи:
from Button import Button #створення кнопок у меню
from Box import Box #створення текстових полів у меню
from Controls import Controls #створення меню з інформацією про значення деяких кнопок на клавіатурі
from Mouse import Mouse # дані про мишу
from Keyboard import Keyboard #дані про клавіатуру
from pygame import draw # розміщення чорного квадрату на весь екран для його очищення
from COLORS import GREEN, BLACK #константи кольорів

class Menu(object):
    """Інтерфейс у головному меню гри"""
    #self : Menu - сам об'єкт, 
    #scr : Surface - екран
    def __init__(self, scr):        
        #self.scr : Surface - екран
        self.scr = scr
        #self.title : Box - назва гри
        self.title = Box(scr, (4*50, 1*50, 13*50, 3*50), "Skyscrapers", 50)
        #self.boardSizeText : Box - текстове поле
        self.boardSizeText = Box(scr, (3*50, 1*50, 4*50, 6*50), "Board size", 25)
        #self.boardSizeButtons : list[Button] - кнопки для вибору розміру ігрового поля
        self.boardSizeButtons = []
        #i : int - ітераційна, створення кнопок вибору розміру
        for i in range(3):
            self.boardSizeButtons.append(Button(scr, (1*50, 3*50*i+4*50, 3*50, 3*50*i+6*50), str(4+i)+"x"+str(4+i), 50))
        for i in range(3):
            self.boardSizeButtons.append(Button(scr, (4*50, 3*50*i+4*50, 6*50, 3*50*i+6*50), str(7+i)+"x"+str(7+i), 50))
        #self.playButton : Button - кнопка що запускає гру
        self.playButton = Button(scr, (7*50, 4*50, 10*50, 7*50), "Play", 50)
        #self.viewControlsText : Box - текстове поле
        self.viewControlsText = Box(scr, (25+7*50, 10*50, 25+9*50, 11*50), "View controls", 25)
        #self.viewControlsButton : Button - кнопка створення меню з інформацією про значення деяких кнопок на клавіатурі
        self.viewControlsButton = Button(scr, (25+7*50, 8*50, 25+9*50, 10*50), "?", 50)
        #self.viewControls : bool - чи ввімкнене меню з інформацією про значення деяких кнопок на клавіатурі
        self.viewControls = False
        #self.controlsScreen : Controls - меню з інформацією про значення деяких кнопок на клавіатурі
        self.controlsScreen = None
        #self.difficultyText : Box - текстове поле
        self.difficultyText = Box(scr, (11*50, 3*50, 13*50, 4*50), "Difficulty", 20)
        #self.difficultyButtons : list[Button] - кнопки для вибору складності
        self.difficultyButtons = []
        #i : int - ітераційна, створення кнопок вибору складності
        for i in range(3):
            self.difficultyButtons.append(Button(scr, (11*50, (4+3*i)*50, 13*50, (6+3*i)*50), ["Easy", "Medium", "Hard"][i], 25))
        #self.sutosolveText : Box - текстове поле
        self.autosolveText = Box(scr, (14*50, 3*50, 16*50, 4*50), "Autosolve", 20)
        #self.autosolveButtons : list[Button] - кнопки вибору автоскладання
        self.autosolveButtons = []
        #i : int - ітераційна, створення кнопок автоскладання
        for i in range(2):
            self.autosolveButtons.append(Button(scr, (14*50, (4+3*i)*50, 16*50, (6+3*i)*50), ["Disable", "Enable"][i], 25))
        #self.boardSize : int - обраний розмір ігрового поля
        self.boardSize = 4 # from 4 up to 9
        #self.difficulty : int - обрана складність
        self.difficulty = 0 # easy = 0, medium = 1, hard = 2
        #self.autosolve : bool - чи обрано автоскладання
        self.autosolve = False

    #self : Menu - сам об'єкт, 
    #scr : Surface - екран, 
    #keyboard : Keyboard - дані про клавіатуру, 
    #mouse : Mouse - дані про мишу, 
    #state : State - стан перемикача екранів
    def update(self, scr, keyboard, mouse, state): #update : None - оновлення головного меню та його кнопок

        draw.rect(scr, BLACK, (0, 0, 850, 650))

        self.title.update()
        self.boardSizeText.update()
        #i : int - ітераційна, оновлення кнопок вибору розміру
        for i in range(6):
            if self.boardSize - 4 == i:
                self.boardSizeButtons[i].update(mouse, None, None, None, GREEN)
            else:
                self.boardSizeButtons[i].update(mouse)
        self.playButton.update(mouse)
        self.viewControlsText.update()
        self.viewControlsButton.update(mouse)
        self.difficultyText.update()
        #i : int - ітераційна, оновлення кнопок вибору складності
        for i in range(3):
            if self.difficulty == i:
                self.difficultyButtons[i].update(mouse, None, None, None, GREEN)
            else:
                self.difficultyButtons[i].update(mouse)

        self.autosolveText.update()
        #i : int - ітераційна, оновлення кнопок вибору автоскладання
        for i in range(2):
            if self.autosolve == i:
                self.autosolveButtons[i].update(mouse, None, None, None, GREEN)
            else:
                self.autosolveButtons[i].update(mouse)

        if self.viewControls == True:
            draw.rect(scr, BLACK, (0, 0, 850, 650))
            if self.controlsScreen == None:
                self.controlsScreen = Controls(scr)
            #result : bool - чи треба закрити меню з інформацією про значення деяких кнопок на клавіатурі
            result = self.controlsScreen.update(keyboard, mouse) 
            if result == False:
                self.viewControls = False
                self.controlsScreen = None

        else: # activate buttons' special abilities
            #i : int - ітераційна, оновлення кнопок вибору розміру
            for i in range(len(self.boardSizeButtons)):
                if self.boardSizeButtons[i].isPressed:
                    self.boardSize = i + 4

            if (self.playButton.isPressed) or (keyboard.enter == True):
                state[1] = self.boardSize
                state[2] = self.difficulty
                state[3] = self.autosolve
                state[0] = ["ingame_normal", "autosolve"][state[3] == True]

            if self.viewControlsButton.isPressed:
                self.viewControls = True
            #i : int - ітераційна, оновлення кнопок вибору складності
            for i in range(len(self.difficultyButtons)):
                if self.difficultyButtons[i].isPressed:
                    self.difficulty = i
            #i : int - ітераційна, оновлення кнопок вибору автоскладання
            for i in range(len(self.autosolveButtons)):
                if self.autosolveButtons[i].isPressed:
                    self.autosolve = (i == 1)
