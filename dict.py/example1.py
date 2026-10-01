#Write a program to update all values into the given dictionary  from decimal to binary equivalen
d= {"A":65,"B":66,"C":67,"D":68,"E":69}

for key,value in d.items():
    d[key] =bin(value)
print(d)    
