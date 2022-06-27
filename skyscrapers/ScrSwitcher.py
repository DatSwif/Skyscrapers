#Клас, що перемикається між головним меню та ігровим полем
#
#Використані імпортовані методи та константи:
from Menu import Menu #створення головного меню
from InGame import InGame #створення ігрового меню

class ScrSwitcher:
    """Клас, що перемикає меню"""
    #self : ScrSwitcher - сам об'єкт, 
    #scr : Surface - екран, 
    #state : tuple[str, int, int, bool] - стан перемикача меню (коли [0] змінюється, треба змінити меню)
    def __init__(self, scr, state):
        #self.menu : Menu - головне меню
        self.menu = Menu(scr)
        #self.ingame : InGame - ігрове меню
        self.ingame = None

    #self : ScrSwitcher - сам об'єкт, 
    #scr : Surface - екран, 
    #keyboard : Keyboard - клавіатура, 
    #mouse : Mouse - дані про мишу, 
    #state : tuple[str, int, int, bool] - стан перемикача меню
    def update(self, scr, keyboard, mouse, state): # перехід між станами "Головне меню" та "У грі", оновлення цих меню

        if state[0] == "menu":
            if self.menu == None:
                self.menu = Menu(scr)
                self.ingame = None
            self.menu.update(scr, keyboard, mouse, state)

        elif state[0] == "ingame_normal" or state[0] == "ingame_pencilmarks" or state[0] == "autosolve" or state[0] == "ingame_coloring":
            if self.ingame == None:
                self.menu = None
                self.ingame = InGame(scr, state[1], state[2])
            self.ingame.update(scr, keyboard, mouse, state)