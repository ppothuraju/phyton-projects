'''
The lstrip() method

The parameterless lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.
'''
# Demonstrating the lstrip() method
print("[" + " tau ".lstrip() + "]")
'''
The one-parameter lstrip() method does the same as its parameterless version, 
but removes all characters enlisted in its argument (a string), not just whitespaces:
'''
print("pythoninstitute.org".lstrip(".org")) #outputs pythoninstitute.org as .org are not leading characters

'''
The lower() method

The lower() method makes a copy of a source string, replaces all upper-case letters with their lower-case counterparts, 
and returns the string as the result. Again, the source string remains untouched.
'''
# Demonstrating the lower() method
print("SiGmA=60".lower())

'''
The replace() method

The two-parameter replace() method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.
'''
# Demonstrating the replace() method
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

'''
The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.
'''
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

