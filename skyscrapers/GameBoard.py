#клас ігрового поля, яке містить комірки
#
#Використані імпортовані методи та константи:
from generate import generate # створення матриці з числами для нової головоломки
from copy import deepcopy # створення копії списку без прив'язки до оригіналу
from random import choice # вибір випадкового елемента для створення випадково згенерованої матриці
from Cell import Cell # створення комірок усередині поля
from Clue import Clue # створення підказок з боків поля

class GameBoard(object):
    """Ігрове поле з комірками та підказками з боків"""
    #self : GameBoard - сам об'єкт, 
    #scr : Surface - екран, 
    #size : int - розмір поля, difficulty : int - складність головоломки
    def __init__(self, scr, size, difficulty): 
        #self.size : int - розмір поля
        self.size = size
        #buffer : list[list[list[int]], list[list[int]]] - зберігає розв'язаний стан та початковий
        buffer = generate(size, difficulty)
        #self.startingState : list[list[int]] - зберігає початковий стан для повернення у разі перезапуску головоломки
        self.startingState = deepcopy(buffer.newBoard)
        #self.currentState : list[list[int]] - поточний стан головоломки
        self.currentState = deepcopy(self.startingState)
        #self.solvedState : list[list[int]] - зберігає розв'язаний стан для авторозв'язання та часткового розв'язання
        self.solvedState = deepcopy(buffer.solvedState)
        #self.board : list[list[Cell, Clue]] - ігрове поле, складається з комірок та підказок
        self.board = []
        #y : int - ітераційна для заповнення ігрового поля об'єктами, координата y
        for y in range(size + 2):
            self.board.append([])
            #x : int - ітераційна для заповнення ігрового поля об'єктами, координата х
            for x in range(size + 2):
                if ((y == 0) or (y == size + 1)) and ((x == 0) or (x == size + 1)):
                    self.board[y].append(None)
                else:
                    #dimensions : list[int, int, int, int, int] - координати об'єкта комірки
                    dimensions = [0, 0, 0, 0, 0] # x1, y1, x2, y2, textsize
                    dimensions[0] = round(50 + 11*50 / (size + 2) * x + 1)
                    dimensions[1] = round(50 + 11*50 / (size + 2) * y + 1)
                    dimensions[2] = round(50 + 11*50 / (size + 2) * (x + 1) - 1)
                    dimensions[3] = round(50 + 11*50 / (size + 2) * (y + 1) - 1)
                    dimensions[4] = round(11*50 / (size + 2) / 2)
                    if ((y == 0) or (y == size + 1)) ^ ((x == 0) or (x == size + 1)):
                        self.board[y].append(Clue(scr, (dimensions[0], dimensions[1], dimensions[2], dimensions[3]), self.currentState[y][x], dimensions[4]))
                    else:
                        self.board[y].append(Cell(scr, (dimensions[0], dimensions[1], dimensions[2], dimensions[3]), self.currentState[y][x], dimensions[4], self.currentState[y][x] == 0))
    
    #self : GameBoard - сам об'єкт, 
    #keyboard : Keyboard - дані про клавіатуру, 
    #mouse : Mouse - дані про мишу, 
    #state : list[str, int, int, bool] - стан програми: яке меню треба ввімкнути
    def update(self, keyboard, mouse, state): #update : None - оновлення всіх комірок та підказок
        #y : int - ітераційна змінна, перевірка всіх комірок на зміни даних, координата у
        for y in range(self.size + 2):
            #х : int - ітераційна змінна, перевірка всіх комірок на зміни даних, координата х
            for x in range(self.size + 2):
                if isinstance(self.board[y][x], Cell):
                    #checkForInput : bool - чи введено номер у комірку
                    checkForInput = False
                    #i : int - перевірка кожної цифри, чи не введена вона
                    for i in range(self.size + 1):
                        if keyboard.num[i] == True:
                            checkForInput = True
                            self.board[y][x].update(mouse, i)
                            if self.board[y][x].isSelected:
                                self.currentState[y][x] = i
                    if not checkForInput:
                        self.board[y][x].update(mouse)
                elif isinstance(self.board[y][x], Clue):
                    self.board[y][x].update()
        
    #self : GameBoard - сам об'єкт, 
    #mouse : Mouse - дані про мишу
    def reset(self, mouse): #reset : None - повернення ігрового поля до початкового стану
        self.currentState = deepcopy(self.startingState)
        #y : int - ітераційна, повернення до початкового стану всіх комірок, координата у
        for y in range(self.size + 2):
            #x : int - ітераційна, повернення до початкового стану всіх комірок, координата х
            for x in range(self.size + 2):
                if isinstance(self.board[y][x], Cell):
                    if self.board[y][x].changeable:
                        self.board[y][x].update(mouse, 0, True)
    
    #self : GameBoard - сам об'єкт
    #board : list[list[int]] - матриця з числами (ігрове поле розв'язаної головоломки),
    #filename : str - ім'я файлу
    def saveToFile(self, board, filename = "solution.txt"): #saveToFile : None - занесення розв'язку в файл при виклику функції autosolve
        #size : int - розмір ігрового поля
        size = len(board)
        #file : fileobj - потік, у який записується результат
        file = open(filename, 'w')
        #y : int - рядок, що записується
        for y in range(size):
            #line : str - рядок
            line = ""
            #x : int - номер стовпчика
            for x in range(size):
                if board[y][x] == 0:
                    line += "  "
                else:
                    line += str(board[y][x]) + " "
            file.write(line + "\n")
        file.close()

    #self : GameBoard - сам об'єкт, 
    #mouse : Mouse - дані про мишу
    def autosolve(self, mouse): #autosolve : None - автоматичне розв'язання

        self.currentState = deepcopy(self.solvedState)
        #y : int - ітераційна, перехід до розв'язаного стану всіх комірок, координата у
        for y in range(1, self.size + 1):
            #х : int - ітераційна, перехід до розв'язаного стану всіх комірок, координата х
            for x in range(1, self.size + 1):
                self.board[y][x].update(mouse, self.currentState[y][x], True)

        self.saveToFile(self.currentState)

    #self : GameBoard - сам об'єкт, 
    #mouse : Mouse - дані про мишу
    def hint(self, mouse): #hint : None - якщо якась комірка заповнена гравцем неправильно, виправити її. Якщо ні, заповнити нову
        #priorityOneCoords : list[tuple[int, int]] - координати комірок, заповнених гравцем неправильно, їм надається перший пріоритет для підказок
        priorityOneCoords = []
        #priorityTwoCoords : list[tuple[int, int]] - координати пустих комірок, їм надається другий пріоритет
        priorityTwoCoords = []
        #x : int - ітераційна, пошук координат комірок першого та другого пріоритету, координата х
        for x in range(1, self.size + 1):
            #у : int - ітераційна, пошук координат комірок першого та другого пріоритету, координата у
            for y in range(1, self.size + 1):
                if (self.currentState[y][x] != self.solvedState[y][x]) and (self.currentState[y][x] != 0):
                    priorityOneCoords.append([y, x])
                elif self.currentState[y][x] != self.solvedState[y][x]:
                    priorityTwoCoords.append([y, x])

        if priorityOneCoords != []:
            coordsToChange = choice(priorityOneCoords)
            self.currentState[coordsToChange[0]][coordsToChange[1]] = deepcopy(self.solvedState[coordsToChange[0]][coordsToChange[1]])
            self.board[coordsToChange[0]][coordsToChange[1]].update(mouse, self.currentState[coordsToChange[0]][coordsToChange[1]], True)

        elif priorityTwoCoords != []:
            coordsToChange = choice(priorityTwoCoords)
            self.currentState[coordsToChange[0]][coordsToChange[1]] = deepcopy(self.solvedState[coordsToChange[0]][coordsToChange[1]])
            self.board[coordsToChange[0]][coordsToChange[1]].update(mouse, self.currentState[coordsToChange[0]][coordsToChange[1]], True)

    #self : GameBoard - сам об'єкт
    def check(self): #check : bool - перевірити чи правильно розв'язано головоломку

        #verifying Skyscrapers
        #x : int - ітераційна, перевірка всіх підказок над ігровим полем (1)
        for x in range(1, self.size + 1): #top line from left to right
            if self.currentState[0][x] != 0:
                #reqWatchable : int - скільки повинно бути видно хмарочосів з цієї підказки
                reqWatchable = self.currentState[0][x]
                #currHighest : int - поточно найвищий хмарочос
                currHighest = 0
                #realWatchable : int - скільки справді видно хмарочосів з цієї підказки
                realWatchable = 0
                for y in range(1, self.size + 1):
                    if self.currentState[y][x] == 0:
                        return False
                    elif self.currentState[y][x] > currHighest:
                        realWatchable += 1
                        currHighest = self.currentState[y][x]
                if not (reqWatchable == realWatchable):
                    return False

        #у : int - ітераційна, перевірка всіх підказок справа від ігрового поля (2) ідентично до (1), але з іншими напрямками
        for y in range(1, self.size + 1): #right line from up to down
            if self.currentState[y][self.size + 1] != 0:
                reqWatchable = self.currentState[y][self.size + 1]
                currHighest = 0
                realWatchable = 0
                for x in range(self.size, 0, -1):
                    if self.currentState[y][x] > currHighest:
                        realWatchable += 1
                        currHighest = self.currentState[y][x]
                if not (reqWatchable == realWatchable):
                    return False

        #х : int - ітераційна, перевірка всіх підказок знизу від ігрового поля (3) ідентично до (1), але з іншими напрямками
        for x in range(1, self.size + 1): #bottom line from left to right
            if self.currentState[self.size + 1][x] != 0:
                reqWatchable = self.currentState[self.size + 1][x]
                currHighest = 0
                realWatchable = 0
                for y in range(self.size, 0, -1):
                    if self.currentState[y][x] > currHighest:
                        realWatchable += 1
                        currHighest = self.currentState[y][x]
                if not (reqWatchable == realWatchable):
                    return False

        #у : int - ітераційна, перевірка всіх підказок зліва від ігрового поля (4) ідентично до (1), але з іншими напрямками
        for y in range(1, self.size + 1): #left line from up to down
            if self.currentState[y][0] != 0:
                reqWatchable = self.currentState[y][0]
                currHighest = 0
                realWatchable = 0
                for x in range(1, self.size + 1):
                    if self.currentState[y][x] > currHighest:
                        realWatchable += 1
                        currHighest = self.currentState[y][x]
                if not (reqWatchable == realWatchable):
                    return False
        
        #verifying Sudoku
        #foundNumber : list[bool] - які номери вже було знайдено в рядку чи стовпчику
        foundNumber = []
        #i : int - ітераційна, ініціалізація foundNumber
        for i in range(self.size):
            foundNumber.append(False)
        #y : int - ітераційна, перебір усіх рядків, координата у
        for y in range(1, self.size + 1):
            #i : int - ітераційна, скидання значень foundNumber
            for i in range(self.size):
                foundNumber[i] = False
            #y : int - ітераційна, перебір усіх рядків, координата х
            for x in range(1, self.size + 1):
                if foundNumber[self.currentState[y][x]-1] == True:
                    return False
                else:
                    foundNumber[self.currentState[y][x]-1] = True

        #х : int - ітераційна, перебір усіх стовпчиків, координата х
        for x in range(1, self.size + 1):
            #i : int - ітераційна, скидання значень foundNumber
            for i in range(self.size):
                foundNumber[i] = False
            #y : int - ітераційна, перебір усіх стовпчиків, координата у
            for y in range(1, self.size + 1):
                if foundNumber[self.currentState[y][x]-1] == True:
                    return False
                else:
                    foundNumber[self.currentState[y][x]-1] = True

        return True # if found 0 mistakes