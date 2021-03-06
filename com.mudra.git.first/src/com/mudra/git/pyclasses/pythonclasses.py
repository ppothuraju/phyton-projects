class Employee:
    def __init__(self,first,last,pay):
        '''
        Constructor
        '''
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
emp1 = Employee('Pavan','Pothuraju','10000')
emp2 = Employee('Sam','Dam','9000')

print(emp1)
print(emp2)

print(emp1.email)

print('{}{}'.format(emp2.first,emp2.last))