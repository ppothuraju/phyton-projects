'''
BaseException

Description:

the most general (abstract) of all Python exceptions - all other exceptions are included in this one; it can be said that the following two except branches are equivalent: except: and except BaseException:.
IndexError

Location:

BaseException ← Exception ← LookupError ← IndexError

Description:

a concrete exception raised when you try to access a non-existent sequence's element (e.g., a list's element)
'''

# the code shows an extravagant way
# of leaving the loop
lst = [1, 2, 3, 4, 5]
ix = 0
doit = True

while doit:
    try:
        print(lst[ix])
        ix += 1
    except IndexError:
        doit = False

print('Done')