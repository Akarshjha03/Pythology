#take positive integer input and check wheather it is a four digit number or not
digit=int(input("Enter the digit\n"))
if digit>=1000 and digit<=9999:
    print("It is of 4 digit")
else:
    print("It is not of 4 digit")  