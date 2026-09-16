#WAP to check whether a character is an alphabet, digit or special character.
ch=input("enter the charcter:")
if ch.isalpha():
    print("Alphabet")
elif ch.isdigit():
    print("Digit")
else:
    print("special character")
    