def rules(piece, x1,y1,x2,y2,board):
    """
    Rules for the game of the chess 
    """
#KING

    if(piece[1] == "k"):
        obstacles = {(ob[0],ob[1]) for ob in board}
        mvs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        for m in mvs:
            cr, cc = x1,y1
            while (cr + m[0] >= 0 and cr + m[0] <= 7) and (cc + m[1] >= 0 and cc + m[1] <= 7):
                cr += m[0]
                cc += m[1]
                if(cr == x2 and cc == y2):
                    if(board[x2][y2]):
                        if(board[x2][y2][0] != piece[0]):
                           return True
                        else:
                            return False
                    return True
                if(board[cr][cc] != ''):
                    break
                # if (cr, cc) in obstacles:break
                if(board[cr][cc] != ''):
                    break
        return False
    #PAWN


    elif(piece[1] == "p"):
        obstacles = {(ob[0],ob[1]) for ob in board}
        if(piece[0] == "w"):
            mvs = [(-1,0)]
        else:
            mvs = [(1,0)]
        for m in mvs:
            if((x1+m[0] == x2 and y1+m[0] == y2) or (x1+ m[0] == x2 and y1 - m[0] == y2)):
                if((board[x1+m[0]][y1+m[0]] != '') or (board[x1+m[0]][y1-m[0]] !='')):
                    return True

            # elif(board[x1+ m[0]][y1+ m[0]] != '' or board[x1-m[0]][y1+m[0]] != ''):
            #     if(y1+ m[0] == y2 or y1 - m[0] == y2):
            #         return True
            cr = x1 + m[0]
            cc = y1 + m[1]
            # if(cr == x2 and cc == y2):
            #     if(board[x2][y2]):
            #         if(board[x2][y2][0] != piece[0]):
            #             return True
            #         else:
            #             pass
            #     return True
            if(x1+m[0] * 2 == x2 and ((x1 == 6 and m[0] == -1)or (x1 == 1 and m[0] == 1))):
                if(board[x1+ m[0]][y1] !=""):
                    return False
                return True
            if(board[cr][cc] != ''):
                return False
            if(cr == x2 and cc == y2):
                print(x1,y1)
                return True
        return False



    elif(piece[1] == "b"):
        # if(piece[0] == "w"):
        #     mvs = [(-1,-1),(-1,1),(1,-1)]
        # else:
        #     mvs = [(1,1),(1,-1),(1,1)]
        mvs = [(1,1),(-1,-1),(-1,1),(1,-1)]
        for m in mvs:
            cr, cc = x1,y1
            while (cr + m[0] >= 0 and cr + m[0] <= 7) and (cc + m[1] >= 0 and cc + m[1] <= 7):
                cr +=m[0]
                cc +=m[1]
                if(cr == x2 and cc == y2):
                    if(board[x2][y2]):
                        if(board[x2][y2][0] != piece[0]):
                           return True
                        else:
                            return False
                    return True
                if(board[cr][cc] != ''):
                    break
                if(cr == x2 and cc == y2):
                    return True
        return False
    #ROOK
    elif(piece[1] == "r"):
        mvs =[(-1,0),(0,-1),(1,0),(0,1)]
        for m in mvs:
            cr ,cc = x1,y1
            while((cr + m[0] >= 0 and cr + m[0] <= 7)and (cc+ m[1] >= 0 and cc+ m[1] <= 7)):
                cr += m[0]
                cc += m[1]
                if(cr == x2 and cc == y2):
                    if(board[x2][y2]):
                        if(board[x2][y2][0] != piece[0]):
                           return True
                        else:
                            return False
                    return True
                if(board[cr][cc] != ""):
                    break
                if(cr == x2 and cc == y2):
                    return True
        return False
    #KNIGHT
    elif(piece[1] == "h"):
        print("KNIGHT")
        mvs = [(-2,1),(2,1),(-2,-1),(2,-1) ,(1,-2),(1,2),(-1,-2),(-1,2)]
        for m in mvs:
            cr ,cc = x1,y1
            while((cr + m[0] >= 0 and cr + m[0] <= 7)and (cc+ m[1] >= 0 and cc+ m[1] <= 7)):
                cr += m[0]
                cc += m[1]
                if(cr == x2 and cc == y2):
                    if(board[x2][y2]):
                        if(board[x2][y2][0] != piece[0]):
                           return True
                        else:
                            return False
                    return True
                if(board[cr][cc] != ""):
                    break
                if(cr == x2 and cc == y2):
                    return True
        return False
    #KING 
    elif(piece[1] == "q"):
        mvs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
        for m in  mvs:
            cr ,cc = x1,y1
            while((cr +m[0] >= 0 and cr + m[0] <= 7) and (cc + m[1] >= 0 and cc + m[1] <= 7)):
                cr += m[0]
                cc += m[1]
                if(cr == x2 and cc == y2):
                    if(board[x2][y2]):
                        if(board[x2][y2][0] != piece[0]):
                            return True
                        else:
                            return False
                    return True
                if(board[cr][cc] != ""):
                    break
                if(cr == x2 and cc == y2):
                    return True
                break
        return False
    else:
        return True