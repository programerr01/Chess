import math
from Rules import rules 
def minimax(board,i,j,depth,isMax):
    
    if depth == 0: 
        return None , evaluate(board)
    if(isMax):
        best_move = None
        moves = getMoves(board[i][j])
        max_score = -math.inf
        for move in moves:
            val = board[i][j]
            if(rules(val, i,j,move[0],move[1],board)):
                board[i][j] = ''
                val1  = board[move[0]][move[1]]
                current_eval = minimax(board,i,j,depth-1, False)[1]
                board[i][j] = val
                board[move[0]][move[1]] = val1
                if(current_eval > max_score):
                        best_move = move
                        max_score = current_eval
        return best_move,max_score
    else:
        best_move = None
        moves  = getMoves(board[i][j])
        min_score = math.inf
        for move in moves:
            val = board[i][j]
            if(rules(val,i,j,move[0],move[1],board)):
                board[i][j] = ''
                val1  = board[move[0]][move[1]]
                current_eval = minimax(board,i,j,depth-1, True)[1]
                board[i][j] = val
                board[move[0]][move[1]] = val1
                if(current_eval < min_score):
                        best_move = move
                        min_score = current_eval
        return best_move,min_score
            
def evaluate(board):
    scores = {
        "wp":-1,
        "bp":1,
        "wr":-5,
        "br":5,
        "bh":3,
        "wh":-3,
        "wb":-3,
        "bb":3,
        "bk":9,
        "bq": 90,
        "wq":-90,
        "wk":-9
    }
    score = 0
    for i in range(8):
        for j in range(8):
            score += scores[board[i][j]]
    return score
        

def getMoves(piece):
    if(piece == ""):
        return [(0,0)]
    if(piece[1] == "k"):
        return [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
    
    elif(piece[1] =="p"):
        return [(-1,0),(1,0),(-2,0),(2,0)]
    
    elif(piece[1] == "q"):
        return [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]

    elif(piece[1] == "h"):
        return [(-2,1),(2,1),(-2,-1),(2,-1) ,(1,-2),(1,2),(-1,-2),(-1,2)]

    elif(piece[1] == "r"):
        return [(-1,0),(0,-1),(1,0),(0,1)]
    
    elif(piece[1] == "b"):
        return [(1,1),(-1,-1),(-1,1),(1,-1)]

