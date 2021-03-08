listA=['a','b','c','d','e','f','g','h','i','j']

row = ""

for item in listA:
    row = row + item
    if len(row) == 3:
        print(row,end='\n')
        row = ""
print(row)
