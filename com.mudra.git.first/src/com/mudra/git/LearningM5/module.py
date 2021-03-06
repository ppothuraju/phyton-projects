#print("I like to be a module")
''' 
    when you run a file directly, its __name__ variable is set to __main__;
    when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)
'''
#print(__name__)

'''
**** To inform user that a variable is a private variable the variable's name with _ (one underscore) or __ (two underscores), 
but remember, it's only a convention. Your module's users may obey it or they may not. There is no way in python to protect private variables
'''
'''
if __name__ == "__main__":
    print("I prefer to be a module")
else:
    print("I like to be module")
'''
# module.py

#!/usr/bin/env python3 

""" module.py - an example of Python module """

__counter = 0

def suml(lst):
    global __counter
    __counter += 1
    vsum = 0
    for el in lst:
        vsum += el
    return vsum

def prodl(lst):
    global __counter    
    __counter += 1
    prod = 1
    for el in lst:
        prod *= el
    return prod

if __name__ == "__main__":
    print("I prefer to be a module, but I can do some tests for you")
    l = [i+1 for i in range(5)]
    print(suml(l) == 15)
    print(prodl(l) == 120)