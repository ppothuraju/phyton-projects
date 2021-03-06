'''
Scenario

You already know how split() works. Now we want you to prove it.

Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

    it should accept exactly one argument - a string;
    it should return a list of words created from the string, divided in the places where the string contains whitespaces;
    if the string is empty, the function should return an empty list;
    its name should be mysplit()

'''
def mysplit(strng):
#
    nstrng = ""
    slist = []
    for i in strng:
        if i != " ":
            nstrng = nstrng + i
        else:
            #print(len(nstrng))
            if len(nstrng) == 0:
                slist = []
            else:
                slist.append(nstrng)
                nstrng = ""
    if len(nstrng) > 0:
        slist.append(nstrng)
    return slist
#   

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))