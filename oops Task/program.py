"""
The given string contains both lowercase and uppercase letters in random order and combines all lowercase letters and displays in output.
Example:  #input :   AmaZOn
	    #output: man
 """
text="AmaZOn"
output=""
for i in text:
    if i>='a' and i<='z':
        output=output+i
print(output)
