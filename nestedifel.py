#find the greatest number
n1=int(input("Enter the number n1:\n"))
n2=int(input("Enter the number n2:\n"))
n3=int(input("Enter the number n3:\n"))

if n1>n2:
    if n1>n3:
        print("n1 is greatest")
    else:
        print("n3 is greatest")
else:
    if n2>n3:
        print("n2 ia greatest")
    else:
        print("n3 is greatest")