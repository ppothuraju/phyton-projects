'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
Extras:

    Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
    Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)

'''
import datetime
name = input("What is your name: ")
age = int(input("How old are you: "))
printtimes = int(input("How many time do you wish to print this message:"))
year = str((datetime.datetime.now().year - age)+100)
pmessage = name + " will be 100 years old in the year " + year
print((pmessage + '\n')* printtimes)

