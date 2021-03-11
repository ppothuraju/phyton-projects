'''
Created on 10 Mar 2021

@author: ppavan
'''
def prntList(x,y):
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
    return printList[x][y]
 
def ledDisplay():
    try:
        inputVal = input("Enter an integer :")
        inputDigits = [int(x) for x in inputVal]
        for j in range(5):
            result =""
            for i in inputDigits:
                result += prntList(i,j)+" "
            print (result, sep="\n")
    except ValueError:
        print("Invalid Integer, try again")
        ledDisplay()

ledDisplay()

