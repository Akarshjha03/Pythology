#take 3 positive integers input and print the greatest of them
n1=int(input("Enter the number n1:\n"))
n2=int(input("Enter the number n2:\n"))
n3=int(input("Enter the number n3:\n"))

if n1>n2 and n1>n3:
    print("n1 is greater")
elif n2>n1 and n2>n3:
    print("n2 is greater")
elif n3>n1 and n3>n2:
    print("n3 is greater")
else:
    print("no result") 