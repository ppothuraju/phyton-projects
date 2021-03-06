'''
Location:

BaseException ← Exception ← StandardError ← ImportError

Description:

a concrete exception raised when an import operation fails
'''

# one of this imports will fail - which one?

try:
    import math
    import time
    import abracadabra

except:
    print('One of your imports has failed.')

