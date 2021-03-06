'''
check that an year is leap or not
the code should output one of the two possible messages, which are Leap year or Common Year depending on the value entered
if the entered year falls outside the gregorian era [<1582] print a warning "Not within the Gregorian calender period"

'''

year = int(input("Enter a year: "))

if (year < 1582 ):
    print("Not within the Gregorian calender period")
elif (year % 4 != 0 ):
    print(year, " is a common year")
elif (year % 100 == 0):
    print(year, " is a leap year")
elif (year % 400 == 0):
    print(year, " is a common year")
else:
    print(year, " is a leap year")