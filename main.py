import pygame
from Piece import Piece
from pygame.locals import * 
from Rules import rules
import sys
#GLOBALS 
W = 568
H = 560
w = W//8
h = H//8
win =None
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GRAY = (120,120,120)
turn = "w"
nm = None
pos  = [0,0]
board = [
    ['br','bh','bb','bk','bq','bb','bh','br'],
    ['bp','bp','bp','bp','bp','bp','bp','bp'],
    ['' ,  '' , '' , '' , '' , '' , '' , '',],
    [ '' , '' , '' , '' , '' , '' , '' , '',],
    [ '' , '' , '' , '' , '' , '' , '' , '',],
    [ '' , '' , '' , '' , '' , '' , '' , '',],
    ['wp','wp','wp','wp','wp','wp','wp','wp'],
    ['wr','wh','wb','wk','wq','wb','wh','wr'],
    ]
mvs =[[0 for i in range(8)] for j in range(8)]

def draws_pieces():
    global nm , board,clicked
    for each in mvs:
        for pc in each:
            # if(pygame.mouse.get_pressed()[0]):
                # if(clicked and nm):

                #     mp = pygame.mouse.get_pos()
                #     i  = mp[0]//w
                #     j = mp[1]//h
                #     board[i][j] = nm.pc
                #     # print(board)
                #     clicked = False
                #     nm = None
            if(pc):
                pc.draw(win)
                # if(pc.move()):
                #     if(not clicked):
                #         clicked = True
                #         nm = pc 
                #         print(nm)
                #     else:
                #         mp = pygame.mouse.get_pos()
                #         i  = mp[0]//w
                #         j = mp[1]//h
                #         # board[i][j] = nm.pc
                #         # print(board)
                #         clicked = False
                #         nm = None


def initialize():
    global mvs
    mvs =[[0 for i in range(8)] for j in range(8)]
    for i in range(8):
        for j in range(8):
            pc = board[i][j]
            # print(i*w,j*h)
            if pc != "":
                mvs[i][j] = Piece(j*w,i*h,pc)
                # print(mvs[i][j])
    print("INIT")
def draw_board():
    black = False
    for i in range(0,W,w):
        for j in range(0,H,h):
            if(black):
                pygame.draw.rect(win,GRAY,(i,j,i+w,j+w))
                black = False
            else:
                pygame.draw.rect(win,WHITE,(i,j,i+w,j+w))
                black = True
        black = not black
    

def check_for_quit():
    global clicked,nm,board,pos,turn
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
           if event.key == K_ESCAPE:
               pygame.quit()
               sys.exit()
            
        elif event.type == MOUSEBUTTONDOWN:
            print("DSS")
            ms = pygame.mouse.get_pos()
            if(nm):
                # print(ms[0]//)
                print(nm,pos)
                (a,b) = (ms[1]//h,ms[0]//w)
                if(rules(nm,pos[0],pos[1], a,b,board) and turn == nm[0]):
                    board[pos[0]][pos[1]] = ''
                    board[a][b] = nm
                    # nm= None
                    initialize()
                    turn = "b" if turn== "w" else "w"
                    pygame.display.set_caption(turn)
                # print(board)
                else:
                    nm = board[ms[1]//h][ms[0]//w]
                    # print(nm,"from here")
                    pos = [ms[1]//h, ms[0]//w]
                # nm= ''
                # pos = [0,0]
            else:
                if(not nm):
                    nm = board[ms[1]//h][ms[0]//w]
                    # print(nm,"from here")
                    pos = [ms[1]//h, ms[0]//w]

def main():
    global win
    pygame.init()
    win = pygame.display.set_mode((W,H))
    pygame.display.set_caption("CHESS")
    win.fill(RED)
    initialize()
    while True:
        draw_board()
        draws_pieces()
        # img = pygame.image.load("imgs/bb.png")
        # win.blit(img,(0,0))
        check_for_quit()
        pygame.display.update()

    print(mvs)
if __name__ == "__main__":
    main()

