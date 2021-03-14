soduku_matrix = []
rows, cols = (9,9)
soduku_matrix = [[c+1 for c in range(rows)] for r in range(cols)]
#soduku_string = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"

def BuildTheMatrix(s_matrix,s_string):
        s_matrix = list(map(''.join,zip(*[iter(s_string)]*9)))
        #print(s_matrix)
        return s_matrix

def DisplayTheMatrix(s_matrix,s_string):
    s_matrix = BuildTheMatrix(s_matrix,s_string)
    for i in range(rows):
        if(i==0):
            print("-"*37)
        if(i==3 or i==6):
            print("|","-"*9,"|","-"*9,"|","-"*9,"|")
        for j in range(cols): 
            print ("|",s_matrix[i][j], end=" ")
        print("|")
    print("-"*37)

def RequestUnsolvedSodoku():
    print("Please enter each values, where values are unknown enter zero (e.g. 2050430060)")
    s_string = UserInput()
    s_matrix = soduku_matrix
    #s_unsolved_sodku = DisplayTheMatrix(s_matrix,s_string)
    DisplayTheMatrix(s_matrix,s_string)
    ConfirmUserEntry()
        
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

def ConfirmUserEntry():
    #print(show_matrix)
    choice = 'A'
    choice = input("Is the above Soduku you wish to resolve (Y/N):")
    while not choice in ('Y','y','N','n'):
        print("Invalid choice, please Y or N")
        choice = input("Is the above Soduku you wish to resolve (Y/N):")
    if (choice == 'Y' or choice == 'y'):
        pass
    if (choice == 'N' or choice == 'n'):
        RequestUnsolvedSodoku()


RequestUnsolvedSodoku()
