'''
Scenario

Some say that the Digit of Life is a digit evaluated using somebody's birthday. It's simple - you just need to sum all the digits of the date. If the result contains more than one digit, you have to repeat the addition until you get exactly one digit. For example:

    1 January 2017 = 2017 01 01
    2 + 0 + 1 + 7 + 0 + 1 + 0 + 1 = 12
    1 + 2 = 3

3 is the digit we searched for and found.
'''
dob = "20000101" #input("Please enter your dob: ")
dg1 = 0
dg2 = 0

for i in dob:
    dg1 = dg1 + int(i)
    #print(dg1)
if dg1 > 9:
    dg1 = str(dg1)
    for i in dg1:
        dg2 = dg2 + int(i)
    dg1 = dg2
print(dg1)