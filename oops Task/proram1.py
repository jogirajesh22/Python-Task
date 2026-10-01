"""
Your program should take an even length string as input which length was greater than or equals to 6.
  Display the output by combining the last character from the first half and first character from the second half of the string.  In case of string is not even length and the number of characters  less than 6 , you can display  output as “INVALID INPUT STRING”

     Example: #input:   MOTHER   
                    #output:   TH
"""                    
input=input("enter the input:")
output=""
if len(input)>=6 and len(input)%2==0:
    first =input[len(input)//2-1]
    last=input[len(input)//2]

    output=first+last
    print(output)
else:
    print("INVALID INPUT STRING")    