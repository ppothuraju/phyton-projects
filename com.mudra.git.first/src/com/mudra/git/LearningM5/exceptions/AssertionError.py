'''
ArithmeticError

Location:

BaseException ← Exception ← ArithmeticError

Description:

an abstract exception including all exceptions caused by arithmetic operations like zero division or an argument's invalid domain
AssertionError

Location:

BaseException ← Exception ← AssertionError

Description:

a concrete exception raised by the assert instruction when its argument evaluates to False, None, 0, or an empty string

'''
from math import tan, radians
angle = int(input('Enter integral angle in degrees: '))

# we must be sure that angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))


