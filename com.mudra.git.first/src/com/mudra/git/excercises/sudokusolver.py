'''
https://www.youtube.com/watch?v=auK3PSZoidc

'''
backtracks = 0
s_matrix = []
rows, cols = (9,9)
#soduku_matrix = [[c+1 for c in range(rows)] for r in range(cols)]
#soduku_string = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"

#This procedure breaks the soduku string into two dimensional array [x][y]
def BuildTheMatrix(s_matrix,s_string):
        #s_matrix = list(map(''.join,zip(*[iter(s_string)]*9)))
        #s_matrix = map(int,str(s_matrix[0]))
        s_matrix.extend([int(x) for x in str(s_string)])
        s_matrix = [s_matrix[i:i + 9] for i in range(0,len(s_matrix),9)]
        # for i in range(0, len(s_matrix),9):
        #     s_matrix[i:i + 9]
        print(s_matrix)
        return s_matrix

#This procedure prints the soduku list in a matrix format
def DisplayTheMatrix(s_matrix):
    for i in range(rows):
        if(i==0):
            print("-"*37)
        if(i==3 or i==6):
            print("|","-"*9,"|","-"*9,"|","-"*9,"|")
        for j in range(cols): 
            print ("|",s_matrix[i][j], end=" ")
        print("|")
    print("-"*37)


#This procedure request the user to input unsolved puzzle in row format     
def UserInput():
    row_values = ""
    s_string = ""
    row_count = 1
    valid_input = True
    for i in range(9):
        valid_input = False
        while not valid_input:
            row_values = input("Enter unsolved row"+str(int(row_count +i))+" values:")
            if(len(row_values) == 9 and row_values.isdigit()):
                s_string += str(row_values)
                valid_input = True
            else:
                print("Invalid data, row must contain 9 digtis. Please try again!")
                valid_input = False
    return  s_string     

#This procedure confirms user input before calling solving procedures
def ConfirmUserEntry():
    choice = 'A'
    choice = input("Is the above Soduku you wish to resolve (Y/N):")
    while not choice in ('Y','y','N','n'):
        print("Invalid choice, please enter Y or N")
        choice = input("Is the above Soduku you wish to resolve (Y/N):")
    if (choice == 'Y' or choice == 'y'):
        return True
    #if (choice == 'N' or choice == 'n'):
       # RequestUnsolvedSodoku()

#This procedure finds the next empty cell to fill the Suodku grid
def findNextCellToFill(s_matrix):
    print("inside find next")
    #Look for an unfilled grid location
    for x in range(9):
        #print("find next x",x)
        for y in range(9):
            print("find next x,y",x,y)
            if s_matrix[x][y] == 0:
                print("inside find if",x,y)
                return x, y
    return -1, -1

#This procedure checks if setting the (i, j) square to e is valid
def isValid(s_matrix, i , j, e):
    #print("inside isvalid")
    rowOk = all([e != s_matrix[i][x] for x in range(9)]) # for x in range of 9 check the gird i of x value is not e
    if rowOk:
        columnOk = all([e != s_matrix[j][x] for x in range(9)])
        if columnOk:
            #finding the top left x,y co-ordinates of
            #the section or sub=grid containing the i,j cell
            secTopX, secTopY = 3 * (i // 3), 3*(j // 3)
            for x in range(secTopX, secTopX+3):
                for y in range(secTopY, secTopY+3):
                    if s_matrix[x][y] == e:
                        return False
            return True
    return False

#This procedure fills in the missing squares of Sudoku puzzle
#obeying the Sudoku rules thorugh brute-force guessing and checking
def solveSudoku(s_matrix, i=0, j=0):
    #print(s_matrix)

    global backtracks

    #find the next cell to fill
    i, j = findNextCellToFill(s_matrix)
    print("inside solve",i,j)
    if i == -1:
        return True

    for e in range(1, 10):
        #print("inside e in range:",e)
        #Try different values in i , j location
        if isValid(s_matrix, i, j, e):
            #print(e)
            s_matrix[i][j] = e
            if solveSudoku(s_matrix, i , j):
                return True

            #Undo the current cell for backtracking
            backtracks += 1
            s_matrix[i][j] = 0
    return False 

#This procedure have other sub procdures which starts with requesting the user input and ends with solving the puzzle
def RequestUnsolvedSodoku():
    global s_matrix
    print("Please enter each values, where values are unknown enter zero (e.g. 2050430060)")
    #s_string = UserInput()
    s_string = "810030027062050090070000000090600100100020004008005070000000080020010750380070042"
    s_matrix = BuildTheMatrix(s_matrix,s_string)
    #DisplayTheMatrix(s_matrix,s_string)
    #printsudoku(s_matrix)
    if ConfirmUserEntry():
        solveSudoku(s_matrix)
        printsudoku()
#This procedure prints the soduku list in a matrix format, a simpler version than DisplayTheMatrix
def printsudoku(): #just a different way of printing the sudoku
    global s_matrix
    print("\n\n")
    for i in range(rows):
        line = ""
        if i == 3 or i == 6:
            print("-"*21)
        for j in range(cols):
            if j == 3 or j == 6:
                line += "| "
            line += str(s_matrix[i][j]) + " "
        print(line)
    print("\n\n")

RequestUnsolvedSodoku()
