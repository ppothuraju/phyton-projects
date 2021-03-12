# See http://ascii.cl/
#https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
upper = {ascii:chr(ascii) for ascii in range(65,91)}
lower = {ascii:chr(ascii) for ascii in range(97,123)}
digit = {ascii:chr(ascii) for ascii in range(48,58)}

s = "The die is cast"
k = 25
def ceasar(s, k):
    for c in s:
        o = ord(c)
        # Do not change symbols and digits
        if (o not in upper and o not in lower) or o in digit:
            yield o
        else:
            # If it's in the upper case and
            # that the rotation is within the uppercase
            if o in upper and o + k % 26 in upper:
                yield o + k % 26
            # If it's in the lower case and
            # that the rotation is within the lowercase
            elif o in lower and o + k % 26 in lower:
                yield o + k % 26
            # Otherwise move back 26 spaces after rotation.
            else: # alphabet.
                yield o + k % 26 -26

x = (''.join(map(chr, ceasar(s, k))))
print (x)