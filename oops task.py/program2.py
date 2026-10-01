class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def show(self) :
        print("name:",self.name)
        print("salary:",self.salary)

s=Employee("Rajesh",30000)
s2=Employee("Raju",25000)

s.show()
s2.show()
"""
s1=Employee(s.name,s.salary)

s1.name="raja"
s1.salary=24000
print(f"s1 deatils:{s1.name},{s1.salary}")  
"""      