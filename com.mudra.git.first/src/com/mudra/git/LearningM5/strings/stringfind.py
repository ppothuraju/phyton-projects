'''


The find() method

The find() method is similar to index(), which you already know - it looks for a substring and returns the index of first occurrence of this substring, but:
-- it's safer - it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
-- it works with strings only - don't try to apply it to any other sequence.



'''
# Demonstrating the find() method
print("Eta".find("ta"))
print("Eta".find("mma"))

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

'''
If you want to perform the find, not from the string's beginning, but from any position, you can use a two-parameter variant of the find() method. Look at the example:
'''
print('kappa'.find('a', 2)) #The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).

txt = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = txt.find('the')
while fnd != -1:
    print(fnd)
    fnd = txt.find('the', fnd + 1)
    

'''
There is also a three-parameter mutation of the find() method - the third argument points to the first index which won't be taken into consideration during the search (it's actually the upper limit of the search).

The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).

Therefore, the modified example outputs:
1
-1 (a cannot be found within the given search boundaries in the second print().
'''

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))


