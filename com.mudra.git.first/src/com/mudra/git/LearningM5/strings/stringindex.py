'''
Operations on strings: the index() method

The index() method (it's a method, not a function) searches the sequence from the beginning, in order to find the first element of the value specified in its argument.

Note: the element searched for must occur in the sequence - its absence will cause a ValueError exception.

The method returns the index of the first occurrence of the argument (which means that the lowest possible result is 0, while the highest is the length of argument decremented by 1). 
'''
# Demonstrating the index() method
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))