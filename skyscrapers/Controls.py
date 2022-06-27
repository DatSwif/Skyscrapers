#Клас меню-пам'ятки для гравця
#
#Використані імпортовані методи та константи:
from Button import Button # створення кнопки в меню
from Box import Box # створення текстових полів у меню
from COLORS import GREY200 # константа кольору

class Controls(object):
    """Пам'ятка, що показує, які клавіші на клавіатурі мають функції у грі"""
    #self : Controls - сам об'єкт, 
    #scr : Surface - екран
    def __init__(self, scr):
        #self.scr : Surface - екран
        self.scr = scr
        #self.background : Box - рамка меню
        self.background = Box(scr, (3*50, 25, 14*50, 25+12*50), "", 25, GREY200)
        #self.title : Box - назва меню
        self.title = Box(scr, (25+8*50-1, 2*50-1, 25+8*50+1, 2*50+1), "Controls:", 50)
        #self.textRows : List[Box] - пояснювальний текст у меню
        self.textRows = []

        self.textRows.append(Box(scr, (25+8*50-1, 25+3*50-1, 25+8*50+1, 25+3*50+1), "Left mouse click to select cells", 25))
        self.textRows.append(Box(scr, (25+8*50-1, 25+4*50-1, 25+8*50+1, 25+4*50+1), "Numbers on the keyboard/screen to place numbers in cells", 18))
        self.textRows.append(Box(scr, (25+8*50-1, 25+5*50-1, 25+8*50+1, 25+5*50+1), "ESC to go to main menu, Enter/PlayButton to start playing", 18))
        self.textRows.append(Box(scr, (25+8*50-1, 25+6*50-1, 25+8*50+1, 25+6*50+1), "R/RestartButton to restart this puzzle from beginning", 18))
        self.textRows.append(Box(scr, (25+8*50-1, 25+7*50-1, 25+8*50+1, 25+7*50+1), "Del/Backspace/0/DelButton to clear selected cell", 20))
        self.textRows.append(Box(scr, (25+8*50-1, 25+8*50-1, 25+8*50+1, 25+8*50+1), "Q/HintButton for a hint (correct or place a cell)", 20))
        self.textRows.append(Box(scr, (25+8*50-1, 25+9*50-1, 25+8*50+1, 25+9*50+1), "Ctrl+Q/AutoButton to autosolve the puzzle", 20))
        self.textRows.append(Box(scr, (25+8*50-1, 25+10*50-1, 25+8*50+1, 25+10*50+1), "F/CheckButton to check solution correctness", 20))
        #self.acceptButton : Button - кнопка виходу з меню
        self.acceptButton = Button(scr, (25+12*50, 11*50, 25+13*50, 12*50), "OK", 25)

    #self : Controls - сам об'єкт, 
    #keyboard : Keyboard - дані про клавіатуру,
    #mouse : Mouse - дані про мишу
    def update(self, keyboard, mouse): #update : None - Перевірка чи вийшов гравець із меню, оновлення даних зображення
        
        self.background.update()
        self.title.update()
        for i in range(len(self.textRows)):
            self.textRows[i].update()

        if ((mouse.isDown and mouse.intersects(self.acceptButton.coords)) or keyboard.enter or keyboard.escape):
            return False
        else:
            self.acceptButton.update(mouse)