'''
Operations on strings: the count() method

The count() method counts all occurrences of the element inside the sequence. The absence of such elements doesn't cause any problems.

Look at the second example in the editor. Can you guess its output?

It is:
2
0

Moreover, Python strings have a significant number of methods intended exclusively for processing characters. Don't expect them to work with any other collections. 
The complete list of is presented here: https://docs.python.org/3.4/library/stdtypes.html#string-methods.
'''

# Demonstrating the count() method
print("abcabc".count("b"))
print('abcabc'.count("d"))