'''
Selected functions from the random module

The most general function named random() (not to be confused with the module's name) produces a float number x coming from the range (0.0, 1.0) - 
in other words: (0.0 <= x < 1.0).



The seed() function is able to directly set the generator's seed. We'll show you two of its variants:

    seed() - sets the seed with the current time;
    seed(int_value) - sets the seed with the integer value int_value.

'''
from random import random, seed, randrange, randint, choice, sample

seed(0)

for i in range(5):
    print(random())

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(lst))
print(sample(lst, 5))
print(sample(lst, 10))