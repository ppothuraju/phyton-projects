data = [['1', '9', '5', '7', '4', '3', '8', '6', '2'], 
        ['4', '3', '1', '8', '6', '5', '9', '2', '7'], 
        ['8', '7', '6', '1', '9', '2', '5', '4', '3'], 
        ['3', '8', '7', '4', '5', '9', '2', '1', '6'], 
        ['6', '1', '2', '3', '8', '7', '4', '9', '5'], 
        ['5', '4', '9', '2', '1', '6', '7', '3', '8'], 
        ['7', '6', '3', '5', '2', '4', '1', '8', '9'], 
        ['9', '2', '8', '6', '7', '1', '3', '5', '4'], 
        ['2', '5', '4', '9', '3', '8', '6', '7', '1']]

chunks = [data[x:x+3] for x in range(0, len(data), 3)]

#print(chunks)

s_rows = []
i_rows = []
s_cols = []
i_cols = []

s_string = "295743861431865927876192543387459216612387495549216738763524189928671354154938672"
subsq1 = []
subsq2 = []
subsq3 = []
subsq4 = []
subsq5 = []
subsq6 = []
subsq7 = []
subsq8 = []
subsq9 = []
subsqs = []
for i in range(len(data)):
    if(i==0 or i==1 or i==2):
        subsq1.extend(data[i][:3])
        subsq2.extend(data[i][3:6])
        subsq3.extend(data[i][6:9])
    if(i==3 or i==4 or i==5):
        subsq4.extend(data[i][:3])
        subsq5.extend(data[i][3:6])
        subsq6.extend(data[i][6:9])
    if(i==6 or i==7 or i==8):
        subsq7.extend(data[i][:3])
        subsq8.extend(data[i][3:6])
        subsq9.extend(data[i][6:9])
subsqs.append(subsq1)    
subsqs.append(subsq2)
subsqs.append(subsq3)
subsqs.append(subsq4)
subsqs.append(subsq5)
subsqs.append(subsq6)
subsqs.append(subsq7)
subsqs.append(subsq8)
subsqs.append(subsq9)   
# print(subsq1)
# print(subsq2)
# print(subsq3)
# print(subsq4)
# print(subsq5)
# print(subsq6)
# print(subsq7)
# print(subsq8)
# print(subsq9)
    #
print(subsqs)

    