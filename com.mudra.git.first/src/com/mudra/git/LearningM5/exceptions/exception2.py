'''
Don't forget that:

    the except branches are searched in the same order in which they appear in the code;
    you must not use more than one except branch with a certain exception name;
    the number of different except branches is arbitrary - the only condition is that if you use try, you must put at least one except (named or not) after it;
    the except keyword must not be used without a preceding try;
    if any of the except branches is executed, no other branches will be visited;
    if none of the specified except branches matches the raised exception, the exception remains unhandled (we'll discuss it soon)
    if an unnamed except branch exists (one without an exception name), it has to be specified as the last.

'''
try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")