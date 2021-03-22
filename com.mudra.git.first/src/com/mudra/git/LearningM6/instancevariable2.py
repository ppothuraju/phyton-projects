class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def setSecond(self, val = 2):
        self.__second = val


exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)

exampleObject2.setSecond(3)

exampleObject3 = ExampleClass(4)
exampleObject3.__third = 5


print(exampleObject1.__dict__)
print(exampleObject2.__dict__)
print(exampleObject3.__dict__)

'''
When Python sees that you want to add an instance variable to an object and you're going to do it inside any of the object's methods, it mangles the operation in the following way:

    it puts a class name before your name;
    it puts an additional underscore at the beginning.

This is why the __first becomes _ExampleClass__first.

The name is now fully accessible from outside the class. You can run a code like this:
print(exampleObject1._ExampleClass__first)

and you'll get a valid result with no errors or exceptions.

As you can see, making a property private is limited.

The mangling won't work if you add an instance variable outside the class code. In this case, it'll behave like any other ordinary property.

'''