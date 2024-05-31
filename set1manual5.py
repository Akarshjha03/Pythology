'''A program that checks if a given year is a leap year.'''


year=int(input("Enter a year"))
if(year%4==0 and year%100!=0 or year%400==0):
 print("This year is a leap")
else:
 print("This year is not a leap")