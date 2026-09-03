#WAP to accept the height of a person in centimeters and categorize the person according to their height. If the height is less than 150 display output as “DWARF” and if the height is greater than equal to 150 and less than 165 display output as “AVERAGE HEIGHT” and if the height is greater than 165 display output as “TALL”
x=int(input("entra a  centimeterst:"))
if x<150:
    print("DWARF")
elif x>=150 and x<165:
    print("AVERAGE HEGIHT")
elif x>165:
    print("TALL")
else:
    print(" ")