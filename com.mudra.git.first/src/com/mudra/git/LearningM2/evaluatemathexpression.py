'''
evaluate the following expression:
1/x+1/x+1/x+1/x
'''
x = float(input("Enter the value for x:"))

y = 1/(x+(1/(x+(1/(x+(1/x))))))

print("y =",y)