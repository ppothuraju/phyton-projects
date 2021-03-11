'''
The isalnum() method

The parameterless method named isalnum() checks if the string contains only digits or alphabetical characters (letters), and returns True or False according to the result.
'''
# Demonstrating the isalnum() method
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())
t = 'Six lambdas'
print(t.isalnum())

t = 'ΑβΓδ'
print(t.isalnum())

t = '20E1'
print(t.isalnum())

'''
The isalpha() method

The isalpha() method is more specialized - it's interested in letters only.
'''
# Example 1: Demonstrating the isapha() method
print("Moooo".isalpha())
print('Mu40'.isalpha())

'''
The isdigit() method

In turn, the isdigit() method looks at digits only - anything else produces False as the result.
'''

# Example 2: Demonstrating the isdigit() method
print('2018'.isdigit())
print("Year2019".isdigit())


'''
The islower() method
The islower() method is a fussy variant of isalpha() - it accepts lower-case letters only.

The isspace() method
The isspace() method identifies whitespaces only - it disregards any other character (the result is False then).

The isupper() method
The isupper() method is the upper-case version of islower() - it concentrates on upper-case letters only.
'''
# Example 1: Demonstrating the islower() method
print("Moooo".islower())
print('moooo'.islower())

# Example 2: Demonstrating the isspace() method
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())

# Example 3: Demonstrating the isupper() method
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())