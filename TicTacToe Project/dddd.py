import random

board1 = ['_', '_', '_', '_']
board2 = ['_', '_', '_', '_']
board3 = ['_', '_', '_', '_']
board4 = ['_', '_', '_', '_']
board = board1 + board2 + board3 + board4
mark = ''
player = ''

choice = ""
spot = ""


def drawboard():
    print("|---|---|---|---|")
    print(f'| {board[0]} | {board[1]} | {board[2]} | {board[3]} |')
    print('|___|___|___|___|')
    print(f'| {board[4]} | {board[5]} | {board[6]} | {board[7]} |')
    print('|___|___|___|___|')
    print(f'| {board[8]} | {board[9]} | {board[10]} | {board[11]} |')
    print('|___|___|___|___|')
    print(f'| {board[12]} | {board[13]} | {board[14]} | {board[15]} |')
    print('|___|___|___|___|')


def checkifleading(board):
    # rows
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[8] == mark and board[9] == mark and board[10] == mark:
        return True
    elif board[12] == mark and board[13] == mark and board[14] == mark:
        return True
    # columns
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[2] == mark and board[6] == mark and board[10] == mark:
        return True
    elif board[3] == mark and board[7] == mark and board[11] == mark:
        return True
    # diagonals
    elif board[0] == mark and board[5] == mark and board[10] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True

def checkifwon(board):
    # rows
    if board[0] == mark and board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark and board[7] == mark:
        return True
    elif board[8] == mark and board[9] == mark and board[10] == mark and board[11] == mark:
        return True
    elif board[12] == mark and board[13] == mark and board[14] == mark and board[15] == mark:
        return True
    # columns
    elif board[0] == mark and board[4] == mark and board[8] == mark and board[12] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark and board[13] == mark:
        return True
    elif board[2] == mark and board[6] == mark and board[10] == mark and board[14] == mark:
        return True
    elif board[3] == mark and board[7] == mark and board[11] == mark and board[15] == mark:
        return True
    # diagonals
    elif board[0] == mark and board[5] == mark and board[10] == mark and board[15] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark and board[12] == mark:
        return True


def draws():

    if board[1] != '_' and board[2] != '_' and board[3] != '_' and board[4] != '_' and board[5] != '_' and board[
        6] != '_' and board[7] != '_' and board[8] != '_' and board[9] != '_' and board[10] != '_' and board[
        11] != '_' and board[12] != '_' and board[13] != '_' and board[14] != '_' and board[15] != '_':
        return True


def checkiffull(board):
    if board[spot] != '_':
        return True


def checkiffullforai(board):
    if board[choice2] != '_':
        return


pplayer = input("Player 1 ,Machine or a human player . 'h' for human ,'m' for bot  :").lower()
while pplayer != 'h' and pplayer != 'm':
    print('incorrect output')
    pplayer = input("Player 1 ,Machine or a human player . 'h' for human ,'m' for bot  :").lower()

pplayer2 = input("Player 2 ,Machine or a human player . 'h' for human ,'m' for bot  :").lower()
while pplayer2 != 'h' and pplayer2 != 'm':
    print('incorrect output')
    pplayer2 = input(
        "Player 2 ,Machine or a human player . 'h' for human ,'m' for bot  :").lower()

if pplayer == 'm' and pplayer2 == 'h':
    pplayer = 'h'
    pplayer2 = 'm'

while player != 'X' and player != 'O':
    player = input("Who do you want to be 'X' or 'O' :").upper()
print("Hey player", player)
print('Welcome to a game of tic tac toe ')
player = mark
while True:
    if pplayer == 'h':
        if player == 'X':
            mark = 'O'
        else:
            mark = 'X'
        drawboard()
        choice = input('pick a row between 0-3 :')
        spot = input('pick a spot in the row between 0-3:')
        while True:
            if choice.isdigit() and spot.isdigit():
                break
            else:
                print('not a number')
                print('try again')
                choice = input('pick a row between 0-3 :')
                spot = input('pick a spot in the row between 0-3:')
        choice = int(choice)
        spot = int(spot)
        if choice == 1:
            spot = spot + 4
        elif choice == 2:
            spot = spot + 8
        elif choice == 3:
            spot = spot + 12
        else:
            spot = spot
        if checkiffull(board):
            print('The spot is occupied')
        board[spot] = mark
        if checkifleading(board):
            print('you are close to victory ')
        if checkifwon(board):
            print('you won player', mark)
            drawboard()
            break

        if draws():
            drawboard()
            print("it's a draw ")
            break
        if pplayer2 == 'h':
            if player == 'X':
                mark = 'X'
            else:
                mark = 'O'
            drawboard()
            choice = input('pick a row between 0-3 :')
            spot = input('pick a spot in the row between 0-3:')
            while True:
                if choice.isdigit() and spot.isdigit():
                    break
                else:  # this code makes sure the players follow the rules
                    print('not a number')
                    print('try again')
                    choice = input('pick a row between 0-3 :')
                    spot = input('pick a spot in the row between 0-3:')
            choice = int(choice)
            spot = int(spot)
            if choice == 1:
                spot = spot + 4
            elif choice == 2:
                spot = spot + 8
            elif choice == 3:
                spot = spot + 12
            else:
                spot = spot
            if checkiffull(board):
                print('The spot is occupied')
            board[spot] = mark
            if checkifleading(board):
                print('you are close to victory ')
            if checkifwon(board):
                drawboard()
                print('you won player', mark)
                break
        if draws():
            print("it's a draw ")

    if pplayer2 == 'm':
        if player == 'X':
            mark = 'X'
        else:
            mark = '0'
        c2 = random.randint(0, 15)
        choice2 = c2
        drawboard()
        if checkiffullforai(board):
            drawboard()
            print('The spot is occupied ')
        board[choice2] = mark
        if checkifleading(board):
            print('you are close to victory ')

        if checkifwon(board):
            drawboard()
            print('you won player', mark)
            break
        if draws():
            drawboard()
            print("it's a draw ")
            break
    if pplayer == 'm':
        if player == 'X':
            mark = 'O'
        else:
            mark = 'X'
        c2 = random.randint(0, 15)
        choice2 = c2
        drawboard()
        if checkiffullforai(board):
            drawboard()
            print('The spot is occupied ')
        board[choice2] = mark
        if checkifleading(board):
            print('you are close to victory ')
        if checkifwon(board):
            drawboard()
            print('you won player', mark)
            break
        if draws():
            drawboard()
            print("it's a draw ")
            break







