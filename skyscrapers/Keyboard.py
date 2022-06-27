#Клас для запису натиснутих клавіш
#
#Використані імпортовані методи та константи:
import pygame
#імпортовано ідентифікатори деяких клавіш та зчитувач клавіш

class Keyboard(object):
    """Записує натискання або затискання усіх потрібних клавіш на клавіатурі"""
    #self : Keyboard - сам об'єкт
    def __init__(self):
        #тут є деякі кнопки, які зчитуються, але нічого не роблять. Коментарі до них позначені через "###".
        self.isDown = False # is True if at least 1 (any) button is pressed
        self.left = False ### left arrow or a
        self.right = False ### right arrow or d
        self.up = False ### up arrow or w
        self.down = False ### down arrow or s
        self.shift = False ### left or right shift -- to redo, multi-select (holding mouse)
        self.ctrl = False # left or right ctrl -- to undo, redo, multi-select (different clicks)
        self.enter = False # left or right enter to select (alternative to mouse)
        # delete or backspace or 0 -- acts as number 0, deletes number from cell
        self.escape = False # esc -- to exit the level
        self.check = False # f -- to check is puzzle was solved right
        self.z = False ### z -- to undo ctrl+z, redo ctrl+shift+z
        self.restart = False # r -- to restart the current puzzle
        self.solve = False # q -- to hint, ctrl+q to autosolve all
        self.toggleColor = False ### c -- to toggle color mode
        self.togglePencilmark = False ### e -- to toggle pencilmark mode
        self.num = [False, False, False, False, False, False, False, False, False, False] # numbers 0-9: number row or numeric keypad

    #self : Keyboard - сам об'єкт
    def update(self): #update : None - оновлення даних про натиснуті клавіші
        #pressed : list[bool] - список усіх натиснутих та не натиснутих клавіш
        pressed = pygame.key.get_pressed()
        
        self.isDown = False
        #key : bool - ітераційна, перевірка всіх клавіш
        for key in pressed:
            if key:
                self.isDown = True

        if pressed[pygame.K_LEFT] or pressed[pygame.K_a]: ### left
            if self.left == False:
                self.left = True
            elif self.left:
                self.left = None
        else:
            self.left = False

        if pressed[pygame.K_RIGHT] or pressed[pygame.K_d]: ### right
            if self.right == False:
                self.right = True
            elif self.right:
                self.right = None
        else:
            self.right = False

        if pressed[pygame.K_UP] or pressed[pygame.K_w]: ### up
            if self.up == False:
                self.up = True
            elif self.up:
                self.up = None
        else:
            self.up = False

        if pressed[pygame.K_DOWN] or pressed[pygame.K_s]: ### down
            if self.down == False:
                self.down = True
            elif self.down:
                self.down = None
        else:
            self.down = False

        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]: ### shift
            if self.shift == False:
                self.shift = True
            elif self.shift:
                self.shift = None
        else:
            self.shift = False

        if pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]: # ctrl
            self.ctrl = True
        else:
            self.ctrl = False

        if pressed[pygame.K_RETURN]: # enter
            if self.enter == False:
                self.enter = True
            elif self.enter:
                self.enter = None
        else:
            self.enter = False

        if pressed[pygame.K_DELETE] or pressed[pygame.K_BACKSPACE] or pressed[pygame.K_0] or pressed[pygame.K_KP0]: # delete
            if self.num[0] == False:
                self.num[0] = True
            elif self.num[0]:
                self.num[0] = None
        else:
            self.num[0] = False

        if pressed[pygame.K_ESCAPE]: # escape
            if self.escape == False:
                self.escape = True
            elif self.escape:
                self.escape = None
        else:
            self.escape = False

        if pressed[pygame.K_f]: # check
            if self.check == False:
                self.check = True
            elif self.check:
                self.check = None
        else:
            self.check = False

        if pressed[pygame.K_r]: # restart
            if self.restart == False:
                self.restart = True
            elif self.restart:
                self.restart = None
        else:
            self.restart = False

        if pressed[pygame.K_c]: ### c - color
            if self.toggleColor == False:
                self.toggleColor = True
            elif self.toggleColor:
                self.toggleColor = None
        else:
            self.toggleColor = False

        if pressed[pygame.K_z]: ### z 
            if self.z == False:
                self.z = True
            elif self.z:
                self.z = None
        else:
            self.z = False

        if pressed[pygame.K_q]: # solve
            if self.solve == False:
                self.solve = True
            elif self.solve:
                self.solve = None
        else:
            self.solve = False

        if pressed[pygame.K_e]: ### e - toggle pencilmark mode
            if self.togglePencilmark == False:
                self.togglePencilmark = True
            elif self.togglePencilmark:
                self.togglePencilmark = None
        else:
            self.togglePencilmark = False
            
        if pressed[pygame.K_1] or pressed[pygame.K_KP1]: # 1
            if self.num[1] == False:
                self.num[1] = True
            elif self.num[1]:
                self.num[1] = None
        else:
            self.num[1] = False

        if pressed[pygame.K_2] or pressed[pygame.K_KP2]: # 2
            if self.num[2] == False:
                self.num[2] = True
            elif self.num[2]:
                self.num[2] = None
        else:
            self.num[2] = False

        if pressed[pygame.K_3] or pressed[pygame.K_KP3]: # 3
            if self.num[3] == False:
                self.num[3] = True
            elif self.num[3]:
                self.num[3] = None
        else:
            self.num[3] = False

        if pressed[pygame.K_4] or pressed[pygame.K_KP4]: # 4
            if self.num[4] == False:
                self.num[4] = True
            elif self.num[4]:
                self.num[4] = None
        else:
            self.num[4] = False

        if pressed[pygame.K_5] or pressed[pygame.K_KP5]: # 5
            if self.num[5] == False:
                self.num[5] = True
            elif self.num[5]:
                self.num[5] = None
        else:
            self.num[5] = False

        if pressed[pygame.K_6] or pressed[pygame.K_KP6]: # 6
            if self.num[6] == False:
                self.num[6] = True
            elif self.num[6]:
                self.num[6] = None
        else:
            self.num[6] = False

        if pressed[pygame.K_7] or pressed[pygame.K_KP7]: # 7
            if self.num[7] == False:
                self.num[7] = True
            elif self.num[7]:
                self.num[7] = None
        else:
            self.num[7] = False

        if pressed[pygame.K_8] or pressed[pygame.K_KP8]: # 8
            if self.num[8] == False:
                self.num[8] = True
            elif self.num[8]:
                self.num[8] = None
        else:
            self.num[8] = False

        if pressed[pygame.K_9] or pressed[pygame.K_KP9]: # 9
            if self.num[9] == False:
                self.num[9] = True
            elif self.num[9]:
                self.num[9] = None
        else:
            self.num[9] = False

