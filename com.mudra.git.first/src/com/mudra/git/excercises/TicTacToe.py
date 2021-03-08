'''
Created on 2 Jul 2020

@author: ppavan
'''
from random import randrange
board = []
rows, cols = (3,3)
turnCount = 0
turn = 0

board = [[c+1 for c in range(rows)] for r in range(cols)]

def BuildTheBoard(board):
    board[0][0] = 1
    board[0][1] = 2
    board[0][2] = 3
    board[1][0] = 4
    board[1][1] = 'X'
    board[1][2] = 6
    board[2][0] = 7
    board[2][1] = 8
    board[2][2] = 9
    return board

def PlayTicTacToe():
    choice = input("Do you wish to Play Tic Tac Toe: (Y/N)")
    if choice == 'Y' or choice == 'y':
        BuildTheBoard(board)
        DisplayBoard(board)
        EnterMove(board)
    elif choice == 'N' or choice == 'n':
        print("Good Bye...")

def EndTheGame(ended):
    DisplayBoard(board)
    print("\nGame Over.\n")
    if ended == 'T':
        print("*** Game Ended in Tie ****")
        PlayTicTacToe()
    else:
        print(" **** " + ended + " won. ****")
        PlayTicTacToe()

def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#   
    global turnCount
    for row in range(rows):
        print("+" + 7 * "-" + "+",end="")
        print(7 * "-" + "+",end="")
        print(7 * "-" + "+")
        print(("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|\n") * 1, end="")
        for col in range(cols):
            print(("|" + " " * 2) , board[row][col],(" " * 2), end="")
        print("|")
        print(("|" + " " * 7 + "|" + " " * 7 + "|" + " " * 7 + "|\n") * 1, end="")
    print("+" + 7 * "-" + "+",end="")
    print(7 * "-" + "+",end="")
    print(7 * "-" + "+")

def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    umove = True
    if not (isBoardFull(board)):
        while (umove):
            userNum = int(input("Enter your move: "))
            if userNum > 0 and userNum < 10:
                if userNum == 5:
                    print("That move not available")
                else:
                    if(isMoveValid(board,userNum,'O')):
                        umove = False
                    else:
                        print(userNum)
                        print("That move not available")
            else:
                print("Invalid move number")
        VictoryFor(board, 'O')
    else:
        VictoryFor(board, 'T')

def VictoryFor(board, sign):
#
# the function verifies the board status in order to check if 
# the player using 'O's or 'X's has won the game
#   
    if sign == 'T':
        EndTheGame(sign)
    elif board[0][0] == board[0][1]== board[0][2] == sign or\
    board[1][0] == board[1][1]== board[1][2] == sign or\
    board[2][0] == board[2][1]== board[2][2] == sign or\
    board[0][0] == board[1][0]== board[2][0] == sign or\
    board[0][1] == board[1][1]== board[2][1] == sign or\
    board[0][2] == board[1][2]== board[2][2] == sign or\
    board[0][0] == board[1][1]== board[2][2] == sign or\
    board[0][2] == board[1][1]== board[2][0] == sign:
        EndTheGame(sign)
    else:
            DisplayBoard(board)
            if sign == 'O':
                 DrawMove(board)
            if sign == 'X':
                EnterMove(board)

def isBoardFull(board):  
#
#   the function check if board is full or any moves left
#
    movecount = 0
    for r in range(rows):
        for c in range(cols):
            if (board[r][c] == 'X'):
                movecount = movecount + 1
    if movecount >=5:
        return True

def isMoveValid(board,move,sign):
#
# the function checks that move is available
#
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == move:
                board[r][c] = sign
                return True

def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    cmove = True
    if not (isBoardFull(board)):
        while (cmove):
            compNum = randrange(10)
            if compNum == 0 or compNum == 5:
                cmove = True
            else:
                if(isMoveValid(board,compNum,'X')):
                    print("Computer Move:",compNum)
                    cmove = False
        VictoryFor(board, 'X')
    else:
        VictoryFor(board, 'T')

#print(EnterMove(board))
#DisplayBoard(board)
PlayTicTacToe()

