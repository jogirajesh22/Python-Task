#WAP to find the largest of three numbers.
a=int(input("enter a num:"))
b=int(input("entra b num:"))
c=int(input("enter c num:"))
if a>=b and a>=c:
    print("a is a largest num")
elif b>=a and b>=c:
    print("b is a largest num")
else:
    print("c is a largest num")