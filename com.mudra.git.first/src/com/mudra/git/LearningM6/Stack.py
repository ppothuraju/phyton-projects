class Stack:
    def __init__(self):
        self.sampleStackList = [] #public variable
        self.__stackList = [] #name starting with two underscores(__), it becomes private - this mean that it can be accessed only from within the class. This is how python implement encapsulation

    def push(self, val):
        self.__stackList.append(val)

    def pop(self):
        val = self.__stackList[-1]
        del self.__stackList[-1]
        return val

stackObject = Stack()

# stackObject.push(3)
# stackObject.push(2)
# stackObject.push(1)

# print(stackObject.pop())
# print(stackObject.pop())
# print(stackObject.pop())

stackObject2 = Stack()

stackObject.push(3)
stackObject2.push(stackObject.pop())

print(stackObject2.pop())

