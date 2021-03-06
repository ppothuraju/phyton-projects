'''
less than 85,528 the tax is 18% minus 556.2
greater than 85,528 the tax is 14,839.2 + 32% of the surplus over 85,528
'''
income = float(input("Enter the annual income: "))

if (income > 85528):
    tax = 14829.2 + (0.32*(income-85528))
else:
    tax = (0.18*income)-556.2

if (tax <= 0):
    tax = 0.0
    
tax = round(tax, 0)
print("The tax is:", tax, "dollars")