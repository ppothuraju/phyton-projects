'''
The rfind() method

The one-, two-, and three-parameter methods named rfind() do nearly the same things as their counterparts (the ones devoid of the r prefix), 
but start their searches from the end of the string, not the beginning (hence the prefix r, for right).
'''
# Demonstrating the rfind() method
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

'''
The rstrip() method

Two variants of the rstrip() method do nearly the same as lstrips, but affect the opposite side of the string.
'''
# Demonstrating the rstrip() method
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))