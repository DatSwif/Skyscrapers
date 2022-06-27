#Головний файл програми
#
#Використані імпортовані методи та константи:
from pygame import font # ініціалізація шрифтів
from pygame import init as pgInit # ініціалізація модуля pygame
from pygame import event # перевірка поточних подій на вихід із гри
from pygame import display # створення вікна з грою
from pygame import time # створення годинника для періодичного оновлення екрану
from pygame import QUIT # подія виходу з гри
from pygame import quit as pgQuit # функція виходу з pygame
from Mouse import Mouse # створення об'єкту для запису даних з миші
from Menu import Menu # створення головного меню
from Keyboard import Keyboard # створення об'єкту для запису даних з клавіатури
from ScrSwitcher import ScrSwitcher # перемикач екранів

#preparing
pgInit()
font.init()
# scr : Surface - екран
scr = display.set_mode((850, 650))
display.set_caption("Skyscrapers")
#clock : Clock - годинник для періодичного оновлення екрану
clock = time.Clock()
#run : bool - чи треба продовжувати головний цикл
run = True
#FPS : int - кадри на секунду
FPS = 20
#state : tuple[str, int, int, bool] - стан перемикача екранів

state = ["menu", 4, 0, False]
# [0]: "menu", "ingame_normal", "ingame_pencilmarks", "autosolve"
# [1]: game size
# [2]: game difficulty
# [3]: autosolve

#mouse : Mouse - ініціалізація об'єкта миші
mouse = Mouse()
#keyboard : Keyboard - ініціалізація об'єкта клавіатури
keyboard = Keyboard()
#scrSwitcher : ScrSwitcher - ініціалізація перемикача екранів
scrSwitcher = ScrSwitcher(scr, state)
#menu : Menu - ініціалізація головного меню
menu = Menu(scr)

#main loop
while run:
    
    #inputs:
    keyboard.update()
    mouse.update()

    #updating variables
    scrSwitcher.update(scr, keyboard, mouse, state)
    
    #screen update
    display.update()        
    clock.tick(FPS)

    #myEvent - ітераційна змінна: поточна подія
    for myEvent in event.get():
        #myEvent.type - тип поточної події
        if myEvent.type == QUIT:
            pgQuit()
            run = False

    #test code