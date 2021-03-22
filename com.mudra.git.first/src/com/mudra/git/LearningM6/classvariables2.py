class ExampleClass:
    varia = 1
    def __init__(self, val):
        ExampleClass.varia = val

print(ExampleClass.__dict__)
exampleObject = ExampleClass(2)

print(ExampleClass.__dict__)
print(exampleObject.__dict__)

'''
We told you before that class variables exist even when no class instance (object) had been created.

Now we're going to take the opportunity to show you the difference between these two __dict__ variables, the one from the class and the one from the object.

Look at the code in the editor. The proof is there.

Let's take a closer look at it:

    we define one class named ExampleClass;
    the class defines one class variable named varia;
    the class constructor sets the variable with the parameter's value;
    naming the variable is the most important aspect of the example because:
        changing the assignment to self.varia = val would create an instance variable of the same name as the class's one;
        changing the assignment to varia = val would operate on a method's local variable; (we strongly encourage you to test both of the above cases - this will make it easier for you to remember the difference)
    the first line of the off-class code prints the value of the ExampleClass.varia attribute; note - we use the value before the very first object of the class is instantiated.

Run the code in the editor and check its output.

As you can see, the class' __dict__ contains much more data than its object's counterpart. Most of them are useless now - the one we want you to check carefully shows the current varia value.

Note that the object's __dict__ is empty - the object has no instance variables.

'''

class ExampleClass1:
    varia = 1
    varia1 = 2
    varia2 = 3
    def __init__(self, val):
        ExampleClass1.varia = val
        self.varia1 = val
        varia2 = val

print(ExampleClass1.__dict__)
exampleObject1 = ExampleClass1(2)

print(ExampleClass1.__dict__)
print(exampleObject1.__dict__)

