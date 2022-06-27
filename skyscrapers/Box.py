#Суперклас - база для створення кнопок, комірок тощо. Використовується як текстове поле.
#
#Використані імпортовані методи та константи:
from pygame import draw # для створення рамки навколо тексту
from pygame import font # робота з шрифтами для створення тексту
from COLORS import BLACK, WHITE # константи кольорів

class Box(object):
    """Поле з текстом"""
    #self : Box - сам об'єкт, 
    #scr : Surface - екран, 
    #coords : tuple[int, int, int, int] - координати, на яких встановлюється об'єкт, 
    #text : string - текст у полі, 
    #textSize : int - розмір тексту, 
    #frameColor : tuple[int, int, int] - колір рамки, 
    #textColor : tuple[int, int, int] - колір тексту
    def __init__(self, scr, coords, text = "", textSize = 25, frameColor = BLACK, textColor = WHITE): 
        #self.surface : Surface - екран
        self.surface = scr
        #self.coords : tuple[int, int, int, int] - координати, на яких встановлюється об'єкт
        self.coords = coords # [x1, y1, x2, y2]
        #self.text : str - текст об'єкта
        self.text = text
        #self.textSize : int - розмір тексту
        self.textSize = textSize
        #self.textColor : tuple[int, int, int] - колір тексту
        self.textColor = textColor
        #self.textObj : list[str, Rect] - текст та координати для його розміщення
        self.textObj = self.makeText(text, (self.coords[0] + self.coords[2]) // 2, (self.coords[1] + self.coords[3]) // 2, textSize, textColor)
        #self.defaultFrameColor : tuple[int, int, int] - колір рамки за замовчуванням
        self.defaultFrameColor = frameColor
        #self.frameColor : tuple[int, int, int] - поточний колір рамки
        self.frameColor = frameColor

    #self : Box - сам об'єкт, 
    #text : str - текст, 
    #textSize : int - розмір тексту, 
    #frameColor : tuple - поточний колір рамки, 
    #textColor : tuple - колір тексту
    def update(self, text = None, textSize = None, frameColor = None, textColor = None): #update : None - оновлення даних та зображення текстового поля
        if text != None:
            self.text = text
        if textSize != None:
            self.textSize = textSize
        if frameColor != None:
            self.frameColor = frameColor
        else:
            self.frameColor = self.defaultFrameColor
        if textColor != None:
            self.textColor = textColor

        draw.rect(self.surface, BLACK, (self.coords[0], self.coords[1], self.coords[2]-self.coords[0], self.coords[3]-self.coords[1]))
        draw.rect(self.surface, self.frameColor, (self.coords[0], self.coords[1], self.coords[2]-self.coords[0], self.coords[3]-self.coords[1]), 1)
        self.textObj = self.makeText(self.text, (self.coords[0] + self.coords[2]) // 2, (self.coords[1] + self.coords[3]) // 2, self.textSize, self.textColor)
        self.surface.blit(self.textObj[0], self.textObj[1])

    #input : str - рядок, що треба перетворити на текст,
    #x : int - координата х тексту, y : int - координата у,
    #size : int - розмір шрифту,
    #color : tuple[int, int, int] - колір тексту
    @staticmethod
    def makeText(input, x, y, size, color = WHITE): #makeText : List[str, Rect] - створення тексту
        #myFont : Font - шрифт
        myFont = font.SysFont("Bahnschrift", size)
        #text : str - якщо введено цифру, переводить її у тип рядка
        text = str(input)
        #text : Surface - поверхня, на якій генерується текст
        text = myFont.render(text, True, color)
        #textRect : Rect - прямокутник із текстом, його розміри та координати
        textRect = text.get_rect()
        #textRect.center : tuple[int, int] - координати центру текстового зображення
        textRect.center = (x, y)
        return [text, textRect]