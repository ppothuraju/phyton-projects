'''
Created on 2 Mar 2021

@author: ppavan
'''
sodoku_sub_square1 = []
sodoku_sub_square2 = []
sodoku_sub_square3 = []
sodoku_sub_square4 = []
sodoku_sub_square5 = []
sodoku_sub_square6 = []
sodoku_sub_square7 = []
sodoku_sub_square8 = []
sodoku_sub_square9 = []
square = []

def sudoku_string(sstring):
    if (square1(sstring) == True) and\
    (square2(sstring) == True) and\
    (square3(sstring) == True) and\
    (square4(sstring) == True) and\
    (square5(sstring) == True) and\
    (square6(sstring) == True) and\
    (square7(sstring) == True) and\
    (square8(sstring) == True) and\
    (square9(sstring) == True):
        return "Valid Sudoku Data"
    else:
        return "Invalid Sudoku Data"
    
def square1(sstring):
    sodoku_sub_square1.extend(sstring[:3])
    sodoku_sub_square1.extend(sstring[9:12])
    sodoku_sub_square1.extend(sstring[18:21])
    print("sodoku-square1 = ", end="\n")
    print_in_martix(sodoku_sub_square1)
    duplicates = [x for n, x in enumerate(sodoku_sub_square1) if x in sodoku_sub_square1[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False

def square2(sstring):
    sodoku_sub_square2.extend(sstring[3:6])
    sodoku_sub_square2.extend(sstring[12:15])
    sodoku_sub_square2.extend(sstring[21:24])
    print("sodoku-square2 = ", end="\n")
    print_in_martix(sodoku_sub_square2)
    duplicates = [x for n, x in enumerate(sodoku_sub_square2) if x in sodoku_sub_square2[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False

def square3(sstring):
    sodoku_sub_square3.extend(sstring[6:9])
    sodoku_sub_square3.extend(sstring[15:18])
    sodoku_sub_square3.extend(sstring[24:27])
    print("sodoku-square3 = ", end="\n")
    print_in_martix(sodoku_sub_square3)
    duplicates = [x for n, x in enumerate(sodoku_sub_square3) if x in sodoku_sub_square3[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False

def square4(sstring):
    sodoku_sub_square4.extend(sstring[27:30])
    sodoku_sub_square4.extend(sstring[36:39])
    sodoku_sub_square4.extend(sstring[45:48])
    print("sodoku-square4 = ", end="\n")
    print_in_martix(sodoku_sub_square4)
    duplicates = [x for n, x in enumerate(sodoku_sub_square4) if x in sodoku_sub_square4[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False

def square5(sstring):
    sodoku_sub_square5.extend(sstring[30:33])
    sodoku_sub_square5.extend(sstring[39:42])
    sodoku_sub_square5.extend(sstring[48:51])
    print("sodoku-square5 = ", end="\n")
    print_in_martix(sodoku_sub_square5)
    duplicates = [x for n, x in enumerate(sodoku_sub_square5) if x in sodoku_sub_square5[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False
        
def square6(sstring):
    sodoku_sub_square6.extend(sstring[33:36])
    sodoku_sub_square6.extend(sstring[42:45])
    sodoku_sub_square6.extend(sstring[51:54])
    print("sodoku-square6 = ", end="\n")
    print_in_martix(sodoku_sub_square6)
    duplicates = [x for n, x in enumerate(sodoku_sub_square6) if x in sodoku_sub_square6[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False

def square7(sstring):
    sodoku_sub_square7.extend(sstring[54:57])
    sodoku_sub_square7.extend(sstring[63:66])
    sodoku_sub_square7.extend(sstring[72:75])
    print("sodoku-square7 = ", end="\n")
    print_in_martix(sodoku_sub_square7)
    duplicates = [x for n, x in enumerate(sodoku_sub_square7) if x in sodoku_sub_square7[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False

def square8(sstring):
    sodoku_sub_square8.extend(sstring[57:60])
    sodoku_sub_square8.extend(sstring[66:69])
    sodoku_sub_square8.extend(sstring[75:78])
    print("sodoku-square8 = ", end="\n")
    print_in_martix(sodoku_sub_square8)
    duplicates = [x for n, x in enumerate(sodoku_sub_square8) if x in sodoku_sub_square8[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False

def square9(sstring):
    sodoku_sub_square9.extend(sstring[60:63])
    sodoku_sub_square9.extend(sstring[69:72])
    sodoku_sub_square9.extend(sstring[78:])
    print("sodoku-square9 = ", end="\n")
    print_in_martix(sodoku_sub_square9)
    duplicates = [x for n, x in enumerate(sodoku_sub_square9) if x in sodoku_sub_square9[:n]]
    if len(duplicates) == 0:
        return True
    else:
        print(duplicates)
        return False

def print_in_martix(listtoprint):
    for index, item in enumerate(listtoprint, start=1):
        print(item, end=' ' if index % 3 else '\n')

print(sudoku_string("295743861431865927876192543387459216612387495549216738763524189928671354154938672")) # true
#print(sudoku_string("195743862431865927876192543387459216612387495549216738763524189928671354254938671")) # false first square do not match
#print(sudoku_string("295743861431865927876192543387459216612387495549216738763524189928671354154938678")) # false last square do not match
#print(sudoku_string("295743861431865927876192543387459286612387495549216738763524189928671354154938678")) # false middle square do not match

'''
inputs: 
True
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672

False
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
''' 
