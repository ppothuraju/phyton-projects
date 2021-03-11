'''
Created on 21 Jul 2020

@author: ppavan
'''
print0 = ("###","# #","# #","# #","###")
print1 = ("  #","  #","  #","  #","  #")
print2 = ("###","  #","###","#  ","###")
print3 = ("###","  #","###","  #","###")
print4 = ("# #","# #","###","  #","  #")
print5 = ("###","#  ","###","  #","###")
print6 = ("###","#  ","###","# #","###")
print7 = ("###","  #","  #","  #","  #")
print8 = ("###","# #","###","# #","###")
print9 = ("###","# #","###","  #","###")
 
printList = [print0,print1,print2,print3,print4,print5,print6,print7,print8,print9]
# print(printList)
#
# print(printList[6][0])
# print(printList[6][1])
# print(printList[6][2])
# print(printList[6][3])
# print(printList[6][4])

 
inputVal = input("Enter an integer :")
#inputStr = str(inputVal)
inputDigits = [int(x) for x in inputVal]
#inputDigits = list(inputVal)
print(inputDigits)

for j in range(5):
    result =""
    for i in inputDigits:
        result += printList[i][j]+" "
    print (result, sep="\n")
'''
inputs
123
9081726354
'''  
