"""
Task: Employee Salary System
Create a Python program using inheritance.
Requirements:
Create a parent class Employee with:
name
employee_id
Method display_details()
Create a child class Developer that inherits from Employee.
Add programming_language
Add method display_developer_details()
Create another child class Tester that inherits from Employee.
Add testing_tool
Add method display_tester_details()
Create objects for both Developer and Tester and display all their details.
"""
class Employee():
    def employee(self,name,employee_id):
        self.name=name
        self.employee_id=employee_id
    def display_details(self):
        print("name:",self.name)
        print("empoyee_id:",self.employee_id)
class Develpoer(Employee):
    def developer(self,programming_language):
        self.programming_language=programming_language
    def display_developer_details(self):
        print("program language:",self.programming_language) 
class Tester(Employee):
    def tester(self,testing_tool):
        self.testing_tool=testing_tool
    def display_tester_details(self):
        print("testing tools:",self.testing_tool)
d=Develpoer()
d.employee("rajesh",1122) 
d.display_details()      
d.developer("python") 
d.display_developer_details()
t=Tester() 
t.employee("raju",2233)
t.display_details()
t.tester("selenium") 
t.display_tester_details()         


