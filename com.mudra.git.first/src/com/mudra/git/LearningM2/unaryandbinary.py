'''
operators - addition (+) and subtraction(-)
unary and binary
print(-4-4) - the - sign before 4 is unary and - sign between is binary
print(+2-2) - the + sing before 2 is unary and - sing between is binary (e.g. -2+3)
'''
print(-4-4)
print(4.-8)
print(-1.1)
print(+2)
# Operators and their priorities - multiplications precede additions
print(2+3*5)

#*** Operators and their bindings
'''
The binding of the operator determines the order of computations performed by some operators with equal priority, put side by side in one expression
Most the Python's operators have "**left-sided**" binding, which menas that the calcuation of the expression is conducted from left to right
One important exception to this rule is exponentiation which is "**right-sided**" binding.
'''
print(9 % 6 % 2) # from left to right 9%6 gives 3 and then 3%2 gives 1
print(2 ** 2 **3) #2**3 -> 8; 2**8 ->256
'''
======== ======== ========
Priority Operator 
1        +, -     unary
2        **
3        *,/,%
4        +,-     binary

Operators and parentheses
In accordance with the arithmetic rules, subexpressions in parentheses are always calcuated first.
'''
print((5 * ((25 % 13) + 100) / (2*13)) // 2)

print((2 ** 4), (2 * 4.), (2 * 4))
print((-2 / 4),(2 / 4), (2 // 4), (-2 // 4))
print((2 % -4),(2 % 4),(2 ** 3 **2))

