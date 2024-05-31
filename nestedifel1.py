#take positive integer input and tell if it is divisible by 5 or 3 but not divisible by 15
number=int(input("Enter the number:\n"))

if number%15==0:
    print("the number is divisible by 15")
else:
    if number%3==0 or number%5==0:
        print("the number is divisible by 3 or 5,But not by 15")
    else:
        print("the number is not divisible by 3 or 5") 