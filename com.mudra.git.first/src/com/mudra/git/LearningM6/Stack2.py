class Stack:
    def __init__(self):
        self.__stackList = []

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

'''
you have to point to the object (the class's instance) which has to be initialized by the constructor - 
this is why you have to specify the argument and use the self variable here; 
note: invoking any method (including constructors) from outside the class never requires you to put the self argument at the argument's list - 
invoking a method from within the class demands explicit usage of the self argument, and it has to be put first on the list.

Note: it's generally a recommended practice to invoke the superclass's constructor before any other initializations you want to perform inside the subclass.
'''   
class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self) # pyton forces to explicitly invoke a super class's contructor. Omitting will have harmful effects
        self.__sum = 0 #created property names __sum which is private

    def getSum(self):
        return self.__sum
    
    def push(self, val): #push method has been overridden, the same name function in superclass now reprent different functionality
        self.__sum += val
        Stack.push(self, val) # superclass name is necessary to avoid confusing it with any ohter function of the same name

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val

stackObject = AddingStack()

for i in range(5):
    stackObject.push(i)
print(stackObject.getSum())

for i in range(5):
    print(stackObject.pop())