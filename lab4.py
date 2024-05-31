#check if a year is leap year or not
year=int(input("Enter the year:\n"))
if year%400==0:
    print("The year is Leap Year")
elif year%4==0 and year%100!=0:
    print("The year is Leap Year")
else:
    print("The year is not Leap Year")