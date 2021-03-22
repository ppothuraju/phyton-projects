class ExampleClass:
    def __init__(self, val = 1):
        self.first = val

    def setSecond(self, val):
        self.second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.third = 5


print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)

'''
Python objects, when created, are gifted with a small set of predefined properties and methods. 
Each object has got them, whether you want them or not. One of them is a variable named __dict__ (it's a dictionary).
The variable contains the names and values of all the properties (variables) the object is currently carrying. Make use of it to safely present an object's contents.

the class named ExampleClass has a constructor, 
which unconditionally creates an instance variable named first, and sets it with the value passed through the first argument (from the class user's perspective) or 
the second argument (from the constructor's perspective); note the default value of the parameter - 
any trick you can do with a regular function parameter can be applied to methods, too;

the class also has a method which creates another instance variable, named second;

we've created three objects of the class ExampleClass, but all these instances differ:

    exampleObject1 only has the property named first;

    exampleObject2 has two properties: first and second;

    exampleObject3 has been enriched with a property named third just on the fly, outside the class's code - this is possible and fully permissible.
'''