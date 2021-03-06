print("My name is","Python.")
print("Monty Python")

'''
the print() function has two keyword agruments. The first of them is named "end" and second is named "sep"(like separator).
'''
print("My name is","Python.",end=" ")
print("Monty Python")

print("My", "name", "is","Python.",sep="-")

print("My","name","is",sep="_",end="*")
print("Monty","Python.",sep="*",end="*\n")
print("I am on new line")

print("    *") #print(*) error: SyntaxError: Invalid syntax
print("   * *") #print (" * ) error: SyntaxError: EOL while scanning string literal
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****") #Print("***") error: NameError: name 'Print' is not defined

print("    *"*2) 
print("   * *"*2)
print("  *   *"*2)
print(" *     *"*2)
print("***   ***"*2)
print("  *   *"*2)
print("  *   *"*2)
print("  *****"*2) 
