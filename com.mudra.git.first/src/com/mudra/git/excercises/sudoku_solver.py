data = [['1', '0', '5', '0', '4', '3', '0', '0', '2'], 
        ['4', '3', '1', '0', '6', '5', '9', '2', '7'], 
        ['8', '7', '6', '0', '9', '2', '5', '0', '3'], 
        ['0', '8', '7', '0', '5', '0', '2', '1', '6'], 
        ['6', '1', '2', '3', '0', '7', '4', '9', '5'], 
        ['5', '4', '0', '2', '1', '6', '0', '3', '8'], 
        ['7', '6', '3', '5', '0', '4', '1', '0', '9'], 
        ['9', '2', '8', '6', '0', '1', '3', '5', '0'], 
        ['0', '0', '0', '0', '0', '0', '0', '0', '0']]
s_rows = []
i_rows = []
s_cols = []
d_cols = []
i_cols = []
#This procedure will replace all zeros from the incoming list with missing numbers
def fillTheRows(data):
    s_rows = data
    n = 0 
    for i in range(len(s_rows)):
        for j in range(9):
            n = 1
            if s_rows[i][j] == "0":
                for n in range(10):
                    if str(n) not in s_rows[i]:
                        s_rows[i][j] = str(n)
 
    return s_rows

def buildTheColsFromRows(data):
    col = []
    cols_non_zero = []
    print_in_martix(data)
    for j in range(9):
        for i in range(len(rows)):
            col.extend(rows[i][j])
        s_cols.append(col)
        i_cols.append([int(i) for i in col])
        col = []
    print("after making cols")
    print_in_martix(s_cols)
    
    
    for i in range(len(s_cols)):
        col = s_cols[i]
        col[:] = ["0" if col.count(x)>1 else x for x in col]# replace the duplicates with zero
        d_cols.append(col)

    print("after replacing duplicates with zeros")
    print_in_martix(d_cols)
    cols_non_zero = fillTheRows(d_cols) #call the row function to remove zeros
    print("after removing duplicates from cols")
    print_in_martix(cols_non_zero)
    return cols_non_zero
    
def print_in_martix(listtoprint):
    for index, item in enumerate(listtoprint, start=1):
        print(item, end=' ' if index % 1 else '\n') 

def buildTheRowsFromCols(data):
    col = []
    print_in_martix(data)
    for j in range(9):
        for i in range(len(rows)):
            col.extend(rows[i][j])
        s_cols.append(col)
        i_cols.append([int(i) for i in col])
        col = []
    print("after making rows from cols")
    print_in_martix(s_cols)

def solveTheSoduku(data):
    rows = []
    cols = []
    rows = fillTheRows(data)
    cols = buildTheColsFromRows(rows)
    rows = buildTheRowsFromCols(cols)
    
print_in_martix(solveTheSoduku(data))





