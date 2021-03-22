class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1

exampleObject1 = ExampleClass()
exampleObject2 = ExampleClass(2)
exampleObject3 = ExampleClass(4)

print(exampleObject1.__dict__, exampleObject1.counter)
print(exampleObject2.__dict__, exampleObject2.counter)
print(exampleObject3.__dict__, exampleObject3.counter) 

'''
Two important conclusions come from the example:

    class variables aren't shown in an object's __dict__ (this is natural as class variables aren't parts of an object) but you can always try to look into the variable of the same name, but at the class level - we'll show you this very soon;
    a class variable always presents the same value in all class instances (objects)

'''
'''
Mangling a class variable's name has the same effects as those you're already familiar with.
'''
class ExampleClass2:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass2.__counter += 1

exampleObject11 = ExampleClass2()
exampleObject22 = ExampleClass2(2)
exampleObject33 = ExampleClass2(4)

print(exampleObject11.__dict__, exampleObject11._ExampleClass2__counter)
print(exampleObject22.__dict__, exampleObject22._ExampleClass2__counter)
print(exampleObject33.__dict__, exampleObject33._ExampleClass2__counter)


