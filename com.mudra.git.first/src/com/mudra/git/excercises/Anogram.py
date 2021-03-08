'''
Scenario

An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

    asks the user for two separate texts;
    checks whether, the entered texts are anagrams and prints the result.

Note:

    assume that two empty strings are not anagrams;
    treat upper- and lower-case letters as equal;
    spaces are not taken into account during the check - treat them as non-existent

'''
str3 = []
def isanagram(st1, st2):
    st1 = st1.replace(" ","")
    st1 = st1.upper()
    st2 = st2.replace(" ","")
    st2 = st2.upper()
    #print(sorted(list(st1)))
    #print(sorted(list(st2)))
    '''
    st3 = list(st1) #list.sort sorts the list in place, i.e. it doesn't return a new list. hence st3 = list(st1).sort() results in none
    st3.sort()
    print(st3)
    '''

    if sorted(list(st1)) == sorted(list(st2)):
        return "Anagrams"
    else:
        return "Not anagrams"

print(isanagram("rail safety","fairy tales"))
print(isanagram("modern","norman"))
print(isanagram("Listen","Silent"))