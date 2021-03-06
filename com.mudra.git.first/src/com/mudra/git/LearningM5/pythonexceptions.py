'''
To learn more about exceptions on your own, you look into Standard Python Library at https://docs.python.org/3.6/library/exceptions.html.

Python 3 defines 63 built-in exceptions, and all of them form a tree-shaped hierarchy, although the tree is a bit weird as its root is located on top.

BaseException -> SystemExit
BaseException -> KeyboardInterrupt
BaseException -> Exception -> ValueError
BaseException -> Exception -> LookupError -> IndexError
BaseException -> Exception -> LookupError -> KeyError
BaseException -> Exception -> ArithmeticError -> ZeroDivisionError
'''
try:
    y = 1 / 0
except ZeroDivisionError:
    print("Zero Division!")
except ArithmeticError:
    print("Arithmetic problem!")

print("THE END.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Arithmetic problem!")
except ZeroDivisionError:
    print("Zero Division!")

print("THE END.")