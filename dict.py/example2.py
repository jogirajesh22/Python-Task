#Write a program set the new key & value into the dict and incase if the key does not exist. 
d= {"A":65,"B":66,"C":67,"D":68,"E":69}

if 'F ' not in d:
    d['F']=70
print(d)    

d.setdefault('F',70)
print(d)