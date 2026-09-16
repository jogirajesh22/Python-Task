student={"name":"rajesh","age":22,"course":["python","database","selenium"]}
print(student.values())
student['grade']="A"
print(student)
student["age"]=23
print(student)
for key ,value in student.items():
        print(key,value)

