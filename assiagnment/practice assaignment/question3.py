#type of weather entry
temperature= float(input("enter temeperature"))
if temperature >30:
    print("hot")
elif temperature >=20 and temperature <=30:
    print("warm") 
elif temperature < 20:
    print("cool")       