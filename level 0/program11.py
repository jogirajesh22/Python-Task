 #WAP to read temperature in centigrade and display a suitable message according to temperature state below 
Temp=int(input("enter a value:"))
if Temp<0:
    print(" frezing weather")
elif Temp <10:
    print(" very cold weather")
elif Temp <20:
    print(" cold weather")
elif Temp <30:
    print(" noraml in temp")
elif Temp <40:
    print(" its hot")
elif Temp>=40:
    print("its very hot")