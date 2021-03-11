'''
The startswith() method

The startswith() method is a mirror reflection of endswith() - it checks if a given string starts with the specified substring.
'''
# Demonstrating the startswith() method
print("omega".startswith("meg"))
print("omega".startswith("om"))

print()

'''
The strip() method

The strip() method combines the effects caused by rstrip() and lstrip() - it makes a new string lacking all the leading and trailing whitespaces.
'''

# Demonstrating the strip() method
print("[" + "   aleph   ".strip() + "]")

'''
The swapcase() method

The swapcase() method makes a new string by swapping the case of all letters within the source string: lower-case characters become upper-case, and vice versa.

The title() method

The title() method performs a somewhat similar function - it changes every word's first letter to upper-case, turning all other ones to lower-case.

The upper() method

Last but not least, the upper() method makes a copy of the source string, replaces all lower-case letters with their upper-case counterparts, and returns the string as the result.
'''


# Demonstrating the swapcase() method
print("I know that I know nothing.".swapcase())

print()

# Demonstrating the title() method
print("I know that I know nothing. Part 1.".title())

print()

# Demonstrating the upper() method
print("I know that I know nothing. Part 2.".upper())