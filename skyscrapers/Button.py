#Клас кнопок у меню та у грі, що мають спецальні функції
#
#Використані імпортовані методи та константи:
from Box import Box # для ініціалізації об'єкта з допомогою суперкласу
from Mouse import Mouse # для зчитування параметрів миші
from COLORS import WHITE, GREY127, GREEN, BLUE # константи кольорів

class Button(Box):
    """Поле з текстом, яке реагує, коли на нього натискають"""
    #self : Button - сам об'єкт, 
    #scr : Surface - екран, 
    #coords : tuple[int, int, int, int] - координати кнопки, 
    #text : str - текст кнопки, 
    #textSize : int - розмір тексту, 
    #frameColor : tuple[int, int, int] - колір рамки, 
    #textColor : tuple[int, int, int] - колір тексту, 
    #isPressable : bool - чи можна натиснути кнопку
    def __init__(self, scr, coords, text = "", textSize = 25, frameColor = WHITE, textColor = WHITE, isPressable = True):
        super().__init__(scr, coords, text, textSize, frameColor, textColor)
        #self.isHovered : bool - чи курсор знаходиться над кнопкою
        self.isHovered = False
        #self.isPressable : bool - чи можна натиснути кнопку
        self.isPressable = isPressable
        #self.isPressed : bool - чи натиснута кнопка
        self.isPressed = False

    #self : Button - сам об'єкт, 
    #mouse : Mouse - дані про мишу, 
    #isPressable : bool - чи можна натиснути кнопку, 
    #text : str - текст кнопки, 
    #textSize : int - розмір тексту, 
    #frameColor : tuple[int, int, int] - колір рамки, 
    #pressed : bool - спеціальний параметр, що означає натиснення кнопки через клавіатуру
    def update(self, mouse, isPressable = None, text = None, textSize = None, frameColor = None, pressed = False): #update : None - Перевірка чи натиснута кнопка і чи знаходиться курсор над нею, оновлення даних і зображення

        if isPressable != None:
            self.isPressable = isPressable
        if text != None:
            self.text = text
        if textSize != None:
            self.textSize = textSize
        if frameColor != None:
            self.frameColor = frameColor
        else:
            self.frameColor = self.defaultFrameColor

        if self.isPressable:
            if pressed: #if a button is pressed in some way other than the mouse
                self.isPressed = True
                self.isHovered == False
            elif mouse.isDown:
                if mouse.intersects(self.coords):
                    self.isPressed = True
                    self.isHovered == False
                else:
                    self.isPressed = False
                    self.isHovered = False
            elif mouse.intersects(self.coords):
                self.isPressed = False
                self.isHovered = True
            else:
                self.isPressed = False
                self.isHovered = False
        
        if not self.isPressable:
            super().update(self.text, self.textSize, GREY127, GREY127)
        elif self.isPressed:
            super().update(self.text, self.textSize, GREEN)
        elif self.isHovered:
            super().update(self.text, self.textSize, BLUE)
        else:
            super().update(self.text, self.textSize, (self.frameColor[0], self.frameColor[1], self.frameColor[2]))