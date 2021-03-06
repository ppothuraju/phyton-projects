'''
Integers: 
Integers
In Python the number can be written either like -11111111 or -11_111_111

Float
4 - integer, 4.0 - floating-point number. the point is what makes a float.
Letter "e" also make a float
example the speed of light expressed in meter per second written directly 300000000 can also be written as 3 X 10 to the power of 8
or in python 3E8
The letter E (or e) comes from the word exponent
** the exponent(the value after the E) has to be an integer
** the base (the value front of E) may be an integer 

octal and hexadecimal numbers

If an integer number is preceded by an "0o" or "0O" prefix(zero-o) it will be treated as an octal value.
This means that the number must contain digits taken from the [0..7] range only
0o123 is an octal number with a decimal value equal to 3

The second convention allows us to use hexadecimal numbers such number should be preceded by the prefix "0x" or "0X"(zero-x)
0x123 is a hexadecimal number with a decimal value equal to 291.
'''
print(0o123)
print(0x123)
print(0.0000000000000000000001) #1e-22

#Boolean Values - two value True, False
print(True > False)
print(True < False)
print(True)
#print(true) udefined variable as it must be True