#	Write a program count each character frequency from the given starting.
str1="rajesh jogi"
dcount ={}
for cha in str1:
    if cha not in dcount:
         dcount[cha]=1
    else:
         dcount[cha]=dcount[cha]+1
print(dcount)         