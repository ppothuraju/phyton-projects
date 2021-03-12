'''
Your task is to write a program which:

    asks the user for one line of text to encrypt;
    asks the user for a shift value (an integer number from the range 1..25 - note: you should force the user to enter a valid shift value (don't give up and don't let bad data fool you!)
    prints out the encoded text. 

Test your code using the data we've provided.
Test data

Sample input:
abcxyzABCxyz 123
2

Sample output:
cdezabCDEzab 123

Sample input:
The die is cast
25

Sample output:
Sgd chd hr bzrs
'''
def CaesarCipher(text,shftvalue):
    cipher = ''
    code = 0
    for char in text:
        code = ord(char) + shftvalue
        #ignore space or other characters
        if not (char.isalnum() or char.isspace()):
            continue
        #print(char)
        # if the character is space or digit do not convert
        if (char.isspace()) or (char.isdigit()):
            code = ord(char)
        # if the character is upper/lower and its ord + shift digit value is greater that last letter of the set
        # then rotate with in the character set
        elif (char.isupper() and code > ord('Z')):
            #print("upper ->", char)
            code = ord('A') + (code - ord('Z') - 1)
        elif (char.islower() and code > ord('z')):
            code = ord('a') + (code - ord('z') - 1)
        else:
            code 
        #print(char," -> ",code," -> ",chr(code))
        cipher += chr(code)
    return cipher

def CaesarInput():
    text_to_encrypt = input("Please enter the string to encrypt:")
    try:
        shift_value = int(input("Please enter an integer for the shift value:"))
    except ValueError:
        print("You must enter an integer value.")
        shift_value = int(input("Please enter an integer for the shift value:"))
    return CaesarCipher(text_to_encrypt,shift_value)

print(CaesarInput())
# print(CaesarCipher('abcxyzABCxyz 123',2))
# print(CaesarCipher('The die is cast',25))

