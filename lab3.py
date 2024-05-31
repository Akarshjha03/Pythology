#print the greatest number out of three numbers
n1=int(input("Enter the value of number 1:\n"))
n2=int(input("Enter the value of number 2:\n"))
n3=int(input("Enter the vaalue of number 3:\n"))
if n1>n2 and n1>n3:
    print("n1 is the greatest ie.",n1)
elif n2>n1 and n2>n3:
    print("n2 is the greatest ie.",n2)
else:
    print("n3 is the greatest ie.",n3)