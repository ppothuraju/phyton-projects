class Classy0:
    def __init__(self, value):
        self.var = value

obj1 = Classy0("object")

print(obj1.var)

class Classy1:
    def __init__(self, value = None):
        self.var = value

obj1 = Classy1("object")
obj2 = Classy1()

print(obj1.var)
print(obj2.var)

class Classy:
    def visible(self):
        print("visible")
    
    def __hidden(self):
        print("hidden")

obj = Classy()
obj.visible()

try:
    obj.__hidden() ##
except:
    print("failed")

obj._Classy__hidden() ##