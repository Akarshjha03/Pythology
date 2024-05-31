#1st if-else statements
rain=input("Enter True or False for is it raining?\n")
if rain=="True":
    print("Take umbrella!")
else:
   print("Dont take umbrell")

#OR

rain=bool(input("Enter True or False for is it raining?\n"))#(1=true,0=false)
if rain==1:
    print("Take umbrella!")
else:
    print("Dont take umbrella!")