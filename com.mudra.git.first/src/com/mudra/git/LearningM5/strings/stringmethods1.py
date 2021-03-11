'''
The capitalize() method
The capitalize() method does exactly what it says - it creates a new string filled with characters taken from the source string, but it tries to modify them in the following way:

The center() method
The one-parameter variant of the center() method makes a copy of the original string, trying to center it inside a field of a specified width.

The centering is actually done by adding some spaces before and after the string.

The endswith() method

The endswith() method checks if the given string ends with the specified argument and returns True or False, depending on the check result.

'''
# Demonstrating the capitalize() method
print('aBcD'.capitalize())

# Demonstrating the center() method
print('[' + 'alpha'.center(10) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

# Demonstrating the endswith() method
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")
    
t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))