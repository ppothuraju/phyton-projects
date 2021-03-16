from random import randrange
data = [['1', '0', '5', '0', '4', '3', '0', '0', '2'], 
        ['4', '3', '1', '0', '6', '5', '9', '2', '7'], 
        ['8', '7', '6', '0', '9', '2', '5', '0', '3'], 
        ['0', '8', '7', '0', '5', '0', '2', '1', '6'], 
        ['6', '1', '2', '3', '0', '7', '4', '9', '5'], 
        ['5', '4', '0', '2', '1', '6', '0', '3', '8'], 
        ['7', '6', '3', '5', '0', '4', '1', '0', '9'], 
        ['9', '2', '8', '6', '0', '1', '3', '5', '0'], 
        ['0', '0', '0', '0', '0', '0', '0', '0', '0']]
dataint = [1, 9, 5, 7, 4, 3, 8, 6, 2]
[4, 3, 1, 8, 6, 5, 9, 2, 7]
[8, 7, 6, 1, 9, 2, 5, 4, 3]
[3, 8, 7, 4, 5, 9, 2, 1, 6]
[6, 1, 2, 3, 8, 7, 4, 9, 5]
[5, 4, 9, 2, 1, 6, 7, 3, 8]
[7, 6, 3, 5, 2, 4, 1, 8, 9]
[9, 2, 8, 6, 7, 1, 3, 5, 4]
[2, 5, 4, 9, 3, 8, 6, 7, 1]


chunks = [data[x:x+3] for x in range(0, len(data), 3)]
digit = randrange(1, 10)
#print(digit)
n = 0 
for i in range(len(data)):
    for j in range(9):
        n = 1
        #print(data[i])
        #print(data[i][j])
        if data[i][j] == "0":
            for n in range(10):
                if str(n) not in data[i]:
                    data[i][j] = str(n)
 
#print(data)
def print_in_martix(listtoprint):
    for index, item in enumerate(listtoprint, start=1):
        print(item, end=' ' if index % 1 else '\n') 
print_in_martix(data) 
#print(chunks)

# s_rows = []
# i_rows = []
# s_cols = []
# i_cols = []
#
# s_string = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"
# subsq1 = []
# subsq2 = []
# subsq3 = []
# subsq4 = []
# subsq5 = []
# subsq6 = []
# subsq7 = []
# subsq8 = []
# subsq9 = []
# subsqs = []
# for i in range(len(data)):
    # if(i==0 or i==1 or i==2):
        # subsq1.extend(data[i][:3])
        # subsq2.extend(data[i][3:6])
        # subsq3.extend(data[i][6:9])
    # if(i==3 or i==4 or i==5):
        # subsq4.extend(data[i][:3])
        # subsq5.extend(data[i][3:6])
        # subsq6.extend(data[i][6:9])
    # if(i==6 or i==7 or i==8):
        # subsq7.extend(data[i][:3])
        # subsq8.extend(data[i][3:6])
        # subsq9.extend(data[i][6:9])
# subsqs.append(subsq1)    
# subsqs.append(subsq2)
# subsqs.append(subsq3)
# subsqs.append(subsq4)
# subsqs.append(subsq5)
# subsqs.append(subsq6)
# subsqs.append(subsq7)
# subsqs.append(subsq8)
# subsqs.append(subsq9)   
# # print(subsq1)
# # print(subsq2)
# # print(subsq3)
# # print(subsq4)
# # print(subsq5)
# # print(subsq6)
# # print(subsq7)
# # print(subsq8)
# # print(subsq9)
    # #
# print(subsqs)





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

    