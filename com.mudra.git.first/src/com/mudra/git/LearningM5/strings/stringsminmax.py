'''
Operations on strings: min()
The function finds the minimum element of the sequence passed as an argument. 
There is one condition - the sequence (string, list, it doesn't matter) cannot be empty, or else you'll get a ValueError exception.

Operations on strings: max()

Similarly, a function named max() finds the maximum element of the sequence.
'''
# Demonstrating min() - Example 1
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']') #used the square brackets to prevent the space from being overlooked on your screen.

t = [0, 1, 2]
print(min(t))   

# Demonstrating max() - Example 1
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))