'''
import math
local variables can be same imported ones
import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14 // we defined our own pi and sin

print(sin(pi/2)) - prints 0.99999999
print(math.sin(math.pi/2)) - prints 1.0 since this use values from math namespace

from math import sin,pi -- selective import only sin and pi is imported from the match namespace
from math import.* --  import all entities from math module
import math as alias
import math as m
print(m.sin(m.pi/2))

from math import pi as PI, sin as sine

print(sine(PI/2))
'''

import math
dir(math) #dir is used to list all the entites of a module in alphabetic order 
