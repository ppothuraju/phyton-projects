s_rows = []
i_rows = []
s_cols = []
i_cols = []
subsqs = []

#s_string = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"

def breakIntoRowAndCols(s_string):
    #creating rows
    row = []
    col = []
    n=0
    for i in range(len(s_string)):
        row.extend(s_string[i])
        n += 1
        if(n==9):
            s_rows.append(row)
            i_rows.append([int(i) for i in row])
            #print(srows,end="\n")
            row = []
            n = 0
    #columns from rows
    for j in range(9):
        for i in range(len(s_rows)):
            col.extend(s_rows[i][j])
        s_cols.append(col)
        i_cols.append([int(i) for i in col])
        col = []
    return s_rows,i_rows,s_cols,i_cols

def breakIntoSubSquares(s_rows):
    subsq1 = []
    subsq2 = []
    subsq3 = []
    subsq4 = []
    subsq5 = []
    subsq6 = []
    subsq7 = []
    subsq8 = []
    subsq9 = []
    
    for i in range(len(s_rows)):
        if(i==0 or i==1 or i==2):
            subsq1.extend(s_rows[i][:3])
            subsq2.extend(s_rows[i][3:6])
            subsq3.extend(s_rows[i][6:9])
        if(i==3 or i==4 or i==5):
            subsq4.extend(s_rows[i][:3])
            subsq5.extend(s_rows[i][3:6])
            subsq6.extend(s_rows[i][6:9])
        if(i==6 or i==7 or i==8):
            subsq7.extend(s_rows[i][:3])
            subsq8.extend(s_rows[i][3:6])
            subsq9.extend(s_rows[i][6:9])
    subsqs.append(subsq1)    
    subsqs.append(subsq2)
    subsqs.append(subsq3)
    subsqs.append(subsq4)
    subsqs.append(subsq5)
    subsqs.append(subsq6)
    subsqs.append(subsq7)
    subsqs.append(subsq8)
    subsqs.append(subsq9)   
    return subsqs

def checkDuplicatesInRowsColsAndSquares(rows,cols,squares):
    #find any duplicates in the rows
    for i in rows:
        dups_in_rows = [x for n, x in enumerate(i) if x in i[:n]]
        if len(dups_in_rows) > 0:
            return False
        else:
            dups_in_rows = []
    
    #find any duplicates in the cols
    for i in cols:
        dups_in_cols = [x for n, x in enumerate(i) if x in i[:n]]
        if len(dups_in_cols) > 0:
            return False
        else:
            dups_in_cols = []
    
    #find any duplicates in the sub squares
    for i in squares:
        dups_in_squares = [x for n, x in enumerate(i) if x in i[:n]]
        if len(dups_in_squares) > 0:
            return False
        else:
            dups_in_squares = []
        
    #print(len(dups_in_rows))
    #print(len(dups_in_cols))
    return True

def checkDuplicatesInSubSquares(s_rows):
    return False   

def validateSodukuString(s_string):
    
    s_string = s_string.replace("\n","")
    
    s_rows,i_rows,s_cols,i_cols = breakIntoRowAndCols(s_string)
    subsqs = breakIntoSubSquares(s_rows)
    #print(s_rows)  
      
    if(checkDuplicatesInRowsColsAndSquares(s_rows,s_cols,subsqs)):
        print("Valid Sodku")
    else:
        print("Invalid Soduku - Some rows or cols or subsquares have duplicates")
    print_in_martix(s_rows)
       
    
    

def print_in_martix(listtoprint):
    for index, item in enumerate(listtoprint, start=1):
        print(item, end=' ' if index % 1 else '\n')    

#validateSodukuString("295743861431865927876192543387459216612387495549216738763524189928671354154938672") # true
#validateSodukuString("195743862431865927876192543387459216612387495549216738763524189928671354254938671") # false first square do not match
#validateSodukuString("295743861431865927876192543387459216612387495549216738763524189928671354154938678") # false last square do not match
#validateSodukuString("295743861431865927876192543387459286612387495549216738763524189928671354154938678") # false middle square do not match


# validateSodukuString('''295743861
# 431865927
# 876192543
# 387459216
# 612387495
# 549216738
# 763524189
# 928671354
# 154938672''')

validateSodukuString('''195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671''')




# rows = [int(i) for i in rows] #converting to integers
# cols = [int(i) for i in cols] 
# print(rows)
# print(cols)



# breaking string at nth character
'''
Use a for-loop and range(start, stop, step) to iterate over a range from start to stop where stop is the len(string) 
and step is every number of characters where the string will be split. 
Use string slicing syntax string[index : index + step] to acquire a string with step characters. 
Use list.append() to add that previously described string to a list. 
'''
# n = 9
# for index in range(0, len(s_string), n):
#
    # row.append(int(s_string[index : index + n]))
    #
# print(rows)

'''
Use list comprehension for a more compact implementation.

#breaking string into rows
n=9
rows = [int(s_string[index : index + n]) for index in range(0, len(s_string), n)] #int covert to integer
print(rows)
'''

