import pygame
import math
class Piece:
    def __init__(self, x,y,pc):
        self.x = x
        self.y = y
        self.pc = pc
        self.win = 0
        self.selected = False

    def draw(self, win):
        # print(self.pc)
        self.win = win
        img = pygame.image.load("imgs/"+self.pc+".png")
        win.blit(img,(self.x,self.y))
    
    def dist(self,x,y,x1,y1):
        return math.sqrt((x-x1)**2 + (y-y1)**2)
    def move(self):
        # print(self.x,self.y)
        ms = pygame.mouse.get_pos()
        # print(ms)
        if(pygame.mouse.get_pressed()[0]):
            if(self.dist(self.x+30,self.y+30 , ms[0],ms[1]) < 40):
               return True
              
        