'''
Arithmetic operators:
exponentiation
A "**" (double asterisk) sign is an exponentiation(power)operator. Its left argumnet is the base, its right the exponent.
2 to the power of 3 is written as 2**3
'''
print(2**3)
print(2 ** 3)
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.)

#multiplication - An "*"(single asterisk) is a multiplication operator
print(2*3)
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3.)

#division - A "/"(slash) is divisional operator. The value in front of the slash is a dividend and behind the slash a divisor
#The result produced by the division operator is always a float
print(6/3)
print(6 / 3)
print(6 / 3.)
print(6 / 3)
print(6. / 3.)

#integer division - A "//"(double slash) sign is an integer divisional operator.
#its results lacks the fractional part, this means that the results are always rounded
print(6 // 3)
print(6 // 3.)
print(6 // 3)
print(6. // 3.) #integer by integer gives integer results, all other cases produce float

print(6//4)
print(6/4)
print(6.//4)#1.0 instead of 1.5
print(6./4)

#remainder (modulo) - The "%"(percent) sign is the remainder operator in python. The result of the operator is a remainder left after the integer division.
print(14%4)
print(12%4.5)

 