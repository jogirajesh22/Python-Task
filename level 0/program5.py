#WAP to read the age of a candidate and determine whether it is eligible for casting his/her own vote.
x=int(input("entra a age:"))
if x>18:
    print("eligible for vote")
elif x<18:
    print("not eligible for vote")
elif x>=18:
    print("her eligible for vote")
else:
    print("not eligible")