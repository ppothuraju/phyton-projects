'''
Task is to prepare a simple code to evaluate the end time of a period of time, given as a number of minutes (it could be
arbitrarily large). The start time is given as a pair of hours (0..23) and minutes(0..59). The result has to be printed to the console.
For example, if an event starts at 12:17 and last 59minutes it will end at 13:16
'''
# hour = int(input("Starting time (hours): "))
# mins = int(input("Starting time (minutes): "))
# dura = int(input("Event duration (minutes): "))
#
# print("End time is: ",((hour+(mins+dura)//60)%24),":",(mins+dura)%60)
'''
(mins+dura)%60 = mins in remainder)
(mins+dura)//60 = number of hours
+hours = total number of hours
%24 hours in remainder
'''

x=11
y=4
x= x%y
x=x%y
y=y%x
print(4%2)