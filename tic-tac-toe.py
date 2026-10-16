import numpy as np

def check_rows(board):
    n=len(board)
    for i in range(n):
        ok=True
        for j in range(1,n):
            if board[i][0]!=board[i][j]:
                ok=False
                break
            else: pass
        if ok:
            return i
    return False

def check_columns(board):
    n=len(board)
    for j in range(n):
        ok=True
        for i in range(1,n):
            if board[0][j]!=board[i][j]:
                ok=False
                break
            else: pass
        if ok:
            return j
    return False 
            
def check_diagonales(board):
    n=len(board)
    ok1=True
    for i in range(1,n):
        if board[0][0]!=board[i][i]:
            ok1=False
            break
    ok2=True
    for i in range(1,n):
        if board[0][n-1]!=board[i][n-i-1]:
            ok2=False
            break
    if ok1:
        return 1
    elif ok2:
        return 2
    else: return ok1 and ok2

def validate(board):
    n=len(board)
    a=check_columns(board)
    if a is not False:
        return board[0][a]
    a=check_rows(board)
    if a is not False:
        return board[a][0]
    a=check_diagonales(board)
    if a==1:
        return board[0][0]
    elif a==2:
        return board[0][n-1]
            
while True:        
    board =[['1','2','3'],
            ['4','5','6'],
            ['7','8','9']]
    k=0
    for i in range(len(board)):
        print(board[i])
    while True:
        k+=1
        a=input('Choose a spot to place ur symbol by typing the associated number to it ')
        while True:
            if int(a)<1 or int(a)>9:
                a=input("Please insert a valid input ")
            else:
                gasit=any(a in rand for rand in board)
                if gasit:
                    break
                else:
                    a=input("Please insert a valid spot that was not taken before ")
        n=len(board)
        j=None
        for i, rand in enumerate(board):
            if a in rand:
                j=rand.index(a)
                break
        if(k%2!=0):
            board[i][j]='X'
            if validate(board)=='X':
                print('Player 1 won! Congrats!')
                for i in range(len(board)):
                    print(board[i])
                ans=input("Do you want to play again? Y/N ")
                if ans in ['Yes','YES','Y','y','yes']:
                    break
                else:
                    exit()
        else:
            board[i][j]='O'
            if validate(board)=='O':
                print('Player 2 won! Congrats!')
                for i in range(len(board)):
                    print(board[i])
                ans=input("Do you want to play again? Y/N ")
                if ans in ['Yes','YES','Y','y','yes']:
                    break
                else:
                    exit()
        if set().union(*board).issubset({'X', 'O'}) and validate(board)!='O' and validate(board)!='X' :
            print('It s a draw!')
            for i in range(len(board)):
                print(board[i])
            ans=input("Do you want to play again? Y/N ")
            if ans in ['Yes','YES','Y','y','yes']:
                break
            else:
                exit()
        for i in range(len(board)):
            print(board[i])
        