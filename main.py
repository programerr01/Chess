import pygame
from Piece import Piece
from pygame.locals import * 
from Rules import rules
from time import sleep
import sys
from minimax import minimax

from  math import inf
#GLOBALS 
W = 568
H = 560
w = W//8
h = H//8
win =None
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (120,120,0)
GRAY = (120,120,120)
turn = "w"
nm = None
textToShow = ""
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


def play_ai():
    print("AI IS PLAYING")
    global board, turn
    # score = 0
    best_score = -inf
    pos = None
    pos_to_play = None
    for i in range(8):
        for j in range(8):
            b = board[i][j]
            if(b != ""):
                if(b[0] != "w"):
                   score = minimax(board,i,j,2,True)
                #    print(score)
                   if(score[1] > best_score):
                       pos = [i,j]
                       pos_to_play = [score[0][0],score[0][1]]
                       
    if(pos):
        print(pos,pos_to_play)
        mv =board[pos[0]][pos[1]]
        print(mv)
        if(rules(mv,pos[0],pos[1],pos_to_play[0], pos_to_play[1],board)):
            board[pos[0]][pos[1]] = ''
            board[pos_to_play[0]][pos_to_play[1]] = mv
            initialize()
            turn = "b" if turn== "w" else "w"
    

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
    global clicked,nm,board,pos,turn,textToShow
    for event in pygame.event.get():
        if event.type  == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
           if event.key == K_ESCAPE:
               pygame.quit()
               sys.exit()
        if(turn == "b"):
            print("AI IS ABOUT TO PLAY")
            play_ai()
        elif event.type == MOUSEBUTTONDOWN:
            print("DSS")
            ms = pygame.mouse.get_pos()
            if(nm):
                # print(ms[0]//)
                print(nm,pos)
                (a,b) = (ms[1]//h,ms[0]//w)
                if((a,b) != (pos[0],pos[1])):
                    if(rules(nm,pos[0],pos[1], a,b,board) and turn =="w"):
                        print(pos,a,b)
                        if(board[a][b] != "" and board[a][b][-1] == "q"):
                            textToShow =  "white wins" if turn == "w" else "black wins"
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
    pygame.font.init() 
    win = pygame.display.set_mode((W,H))
    pygame.display.set_caption("CHESS")
    win.fill(RED)
    initialize()
    while True:
        draw_board()
        draws_pieces()
        check_for_quit()
        if(textToShow):
            win.fill(WHITE)
            myfont = pygame.font.SysFont('Comic Sans MS', 100)
            textsurface = myfont.render(textToShow, False, YELLOW)
            win.blit(textsurface,(2*w,3*h))
            

        pygame.display.update()

    print(mvs)
if __name__ == "__main__":
    main()

