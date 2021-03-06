'''
Location:

BaseException ← Exception ← MemoryError

Description:

a concrete exception raised when an operation cannot be completed due to a lack of free memory
'''
# this code causes the MemoryError exception
# warning: executing this code may be crucial
# for your OS
# don't run it in production environments!

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')

