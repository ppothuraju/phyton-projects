'''
The first is implemented as a function named sorted().

The function takes one argument (a list) and returns a new list, filled with the sorted argument's elements. 

The second method affects the list itself - no new list is created. Ordering is performed in situ by the method named sort().
'''
# Demonstrating the sorted() function
firstGreek = ['omega', 'alpha', 'pi', 'gamma']
firstGreek2 = sorted(firstGreek)

print(firstGreek)
print(firstGreek2)

print()

# Demonstrating the sort() method
secondGreek = ['omega', 'alpha', 'pi', 'gamma']
print(secondGreek)

secondGreek.sort()
print(secondGreek)