'''
Created on 12 Mar 2021

@author: ppavan
'''
rows, cols = (9,9)
sudoku = [[c+1 for c in range(rows)] for r in range(cols)]
sudoku =    [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0]]
sudoku2 =  '295743861431865927876192543387459216612387495549216738763524189928671354154938672'
slist = []

slist.append(sudoku2[0:9])
slist.append(sudoku2[9:18])
slist.append(sudoku2[18:27])
slist.append(sudoku2[27:36])
slist.append(sudoku2[36:45])
slist.append(sudoku2[45:54])
slist.append(sudoku2[54:63])
slist.append(sudoku2[63:72])
slist.append(sudoku2[72:81])


print(slist)

def printsudoku():
    #print("\n\n\n\n\n")
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("---------------------")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)
print(printsudoku())


def print_in_martix(listtoprint):
    print('-'*37)
    for index, item in enumerate(listtoprint, start=1):
        print('|', item, end=' ' if index % 9 else ' |\n')
    print('-'*37)
    return None
#print(print_in_martix(sudoku))


def DisplayBoard(sudoku):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#   
    global turnCount
    for row in range(rows):
        print("+" + 3 * "-" + "+",end="")
        print(3 * "-" + "+",end="")
        print(3 * "-" + "+",end="")
        print(3 * "-" + "+",end="")
        print(3 * "-" + "+",end="")
        print(3 * "-" + "+",end="")
        print(3 * "-" + "+",end="")
        print(3 * "-" + "+",end="")
        print(3 * "-" + "+")
        for col in range(cols):
            print(("|"), sudoku[row][col], end=" ")
        print("|")
    print("+" + 3 * "-" + "+",end="")
    print(3 * "-" + "+",end="")
    print(3 * "-" + "+",end="")
    print(3 * "-" + "+",end="")
    print(3 * "-" + "+",end="")
    print(3 * "-" + "+",end="")
    print(3 * "-" + "+",end="")
    print(3 * "-" + "+",end="")
    print(3 * "-" + "+")

#print(DisplayBoard(sudoku))


