#функція, що генерує випадкову розв'язану головоломку та робить із неї нерозв'язану
#
#Використані імпортовані методи та константи:
from random import shuffle # перемішування рядків для отримання випадкової матриці чисел
from time import time # отримання часу задля того, щоб виходити з циклів, які займають забагато часу

class generate:
	"""Згенерувати нову головоломку"""
	#self : generate - сам об'єкт, 
	#size : int - розмір ігрового поля, 
	#difficulty : int - ріень складності головоломки
	def __init__(self, size, difficulty):
		
		#boardCells : int - розмір поля разом із підказками
		boardCells = size + 2
		#board : list[list[int]] - поле
		board = []
		#i : int - ітераційна, додавання випадкових рядків до матриці
		for i in range(size):
			#currentLine : list[int] - поточний рядок, перемішується, поки не відповідатиме правилам судоку
			currentLine = list(range(1, size + 1))
			shuffle(currentLine)
			while not self.plausible(board, currentLine):
				shuffle(currentLine)
			board.append(currentLine)
		#tboard : list[list[int]] - транспонована матриця
		tboard = self.trasposta(board) 
		#new_board : list[list[int]] - розширене ігрове поле з підказками
		new_board = [[0] + [self.countTops(line) for line in tboard] + [0]]
		#line : list[int] - рядок ігрового поля
		for line in board:
			new_board += [[self.countTops(line)] + line + [self.countTops(line, True)]]
		new_board += [[0] + [self.countTops(line, True) for line in tboard] + [0]]

		# Removing Values from the board
		#cap : int - максимальна кількість клітинок, які дозволяє прибрати складність головоломки
		cap = round(size ** 2 * (0.6 + 0.2 * difficulty)) # how many squares we can remove : easy - 60%, medium - 80%, hard - all
		#self.solvedState : list[list[int]] - розв'язаний стан ігрового поля
		self.solvedState = [l[:] for l in new_board]
		#removed : int - скільки прибрано комірок
		removed = 0
		#x : int - випадкова координата х, перевіряється чи буде єдиний розв'язок, якщо цю клітинку зробити нулем
		#y : int - випадкова координата у, 
		for x, y in self.randCells(boardCells):
			#tmp : int - тимчасово зберігає значення клітинки
			tmp = new_board[y][x]
			new_board[y][x] = 0
			removed += 1
			#startTime : float - час початку перевірки на кількість можливих розв'язків
			startTime = time()
			if self.solutionsCount(startTime, size, [l[:] for l in new_board]) != 1:
				new_board[y][x] = tmp
				removed -= 1
			if removed > cap:
				break

		#self.newBoard : list[list[int]] - головоломка, яка наприкінці ініціалізації є готовою до розв'язання
		self.newBoard = [l[:] for l in new_board]

	#line : list[int] - рядок ігрового поля, 
	#reverse : bool - чи треба зчитувати рядок навпаки
	def countTops(self, line, reverse = False): #self.countTops : int - порахувати, скільки видно хмарочосів у визначену сторону
		if reverse:
			line = list(reversed(line))
		#max : int - максимальний розмір хмарочоса
		max = -1
		#count : int - кількість хмарочосів, що видно
		count = 0
		#i : int - ітераційна, переглядає висоту всіх хмарочосів
		for i in line:
			if i > max:
				max = i
				count += 1
		return count

	#board : list[list[int]] - ігрове поле
	def trasposta(self, board): #self.trasposta : list[list[int]] - транспонувати матрицю
		#t : list[list[int]] - транспонована матриця
		t = [[] for i in range(len(board))]
		#line : list[int] - рядок матриці
		for line in board:
			#i : int - індекс у рядку звідки береться значення та індекс рядка, у який воно додається,
			#cell : int - значення комірки за цим індексом
			for i, cell in enumerate(line):
				t[i].append(cell)
		return t

	#board : list[list[int]] - матриця, 
	#line : list[int] - рядок, що перевіряється
	def plausible(self, board, line): #self.plausible : bool - перевірити чи підходить даний рядок чисел до даної матриці чисел за правилами судоку
		#i : int - індекс комірки в рядку, 
		#item : int - значення комірки
		for i, item in enumerate(line):
			#tLine : list[int] - стовпчик, який перевіряє чи допустиме значення комірки
			for tLine in board:
				if tLine[i] == item:
					return False
		return True

	#boardSize : int - розмір ігрового поля
	def randCells(self, boardSize): #self.randCells : tuple[int, int] повертає випадкові координати, кожного разу нові
		#randx : list[int] - рядок усіх можливих координат х, перемішаний
		randx = list(range(1, boardSize - 1))
		#randy : list[int] - рядок усіх можливих координат у, перемішаний
		randy = list(range(1, boardSize - 1))
		shuffle(randx)
		shuffle(randy)
		#x : int - ітераційна, усі значення координати х у рядку randx
		for x in randx:
			#y : int - ітераційна, усі значення координати y у рядку randy
			for y in randy:
				yield(x, y)

		# Picking side values that will be removed
		# sides : list[int] - індекси підказки в кожному направленні
		sides = list(range(1, boardSize - 1))
		#pairs : list[list[tuple[int, int]]] - координати підказок відносно початку рядка/стовпчика, по 1 на кожне направлення
		pairs = []
		#i : int - індекс підказки
		for i in sides:
			pairs += [(0, i), (boardSize - 1, i), (i, 0), (i, boardSize - 1)]
		shuffle(pairs)
	
		# pairs = pairs[:len(pairs)//3]

		#pair : list[tuple[int, int]] - елемент списку pairs, що має значення координати підказки, що перевіряється на можливість видалення
		for pair in pairs:
			yield pair

	#startTime : float - початок обчислень, 
	#size : int - розмір поля, board : list[list[int]] - ігрове поле, 
	#pos : tuple[int, int] - координата клітинки, що перевіряється на можливість видалення
	def solutionsCount(self, startTime, size, board, pos = (1, 1)): #self.solutionsCount : int - рекурсивно рахує кількість можливих розв'язків для даної матриці чисел. Якщо рахує довше 1 секунди, повертає 0
		if time() - startTime >= 1:
			return 0
		#nextPos : tuple[int, int] - наступна позиція, що перевіряється
		nextPos = self.nextPosition(pos, size)
		while board[pos[0]][pos[1]] != 0 and nextPos != (size + 1, 1):
			pos = nextPos
			nextPos = self.nextPosition(pos, size)
		if nextPos == (size + 1, 1):
			return 1
		#solutions : int - кількість можливих розв'язків
		solutions = 0

		#possibleVals : list[int] - можливі значення в комірці
		possibleVals = self.possibleValues(size, board, pos)
		#value : int - ітераційна, перебирає значення
		for value in possibleVals:
			board[pos[0]][pos[1]] = value
			if not self.checkCross(board, pos):
				continue
			solutions += self.solutionsCount(startTime, size, board, nextPos)
			if solutions > 1:
				return solutions
		board[pos[0]][pos[1]] = 0
		return solutions

	#size : int - розмір поля, 
	#board : list[list[int]] - поле,
	#pos : tuple[int, int] - координата комірки
	def possibleValues(self, size, board, pos): #self.possibleValues : list[int] визначає можливі значення для комірки з координатами pos
		#pvals : list[int] - можливі значення в комірці
		pvals = list(range(1, size + 1))
		#i : int - ітераційна, проходить індекси рядка/стовпчика
		for i in range(1, size + 1):
			#f : int - комірка у стовпчику, s : int - комірка в рядку
			f, s = board[i][pos[1]], board[pos[0]][i]
			if f in pvals:
				pvals.remove(f)
			if s in pvals:
				pvals.remove(s)
		return pvals

	#pos : tuple[int, int] - координата комірки,
	#size : int - розмір поля
	def nextPosition(self, pos, size): #self.nextPosition : tuple[int, int] - повертає наступні координати позиції, яку слід перевірити
		if pos[1] == size:
			return (pos[0] + 1, 1)
		else:
			return (pos[0], pos[1] + 1)

	#board : list[list[int]] - поле,
	#pos : tuple[int, int] - координата комірки
	def checkCross(self, board, pos): #self.checkCross : bool - Якщо значення у клітинці pos допустимо за правилами Хмарочосів, повертає True, в іншому випадку False
		lines = [board[pos[0]], [l[pos[1]] for l in board]]
		for line in lines:
			if 0 in line:
				return True
			if line[0] != 0 and self.countTops(line[1:-1]) != line[0]:
				return False
			if line[-1] != 0 and self.countTops(list(reversed(line[1:-1]))) != line[-1]:
				return False
		return True