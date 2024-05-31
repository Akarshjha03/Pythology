'''take input  percentage of a student and print the grade according to marks
a.81-100:verygood, b. 61-80:good, c.41-60:average, <=40:fail'''

percentage=int(input("Enter the percentage of student:\n"))
if percentage>=81 and percentage<=100:
    print("Grade:very good")
elif percentage>=61 and percentage<=80:
    print("Grade:good")
elif percentage>=41 and percentage<=60:
    print("Grade:average")
else:
    print("Grade:fail")