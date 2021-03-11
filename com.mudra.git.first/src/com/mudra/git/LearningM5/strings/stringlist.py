'''
Operations on strings: the list() function

The list() function takes its argument (a string) and creates a new list containing all the string's characters, one per list element.

Note: it's not strictly a string function - list() is able to create a new list from many other entities (e.g., from tuples and dictionaries).

Take a look at the code example in the editor.

The example outputs:
['a', 'b', 'c', 'a', 'b', 'c']

'''
# Demonstrating the list() function
print(list("abcabc"))