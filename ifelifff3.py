#multiple conditions using 'and' & 'or'
'''for A grade: both marks should be above 80
   for B grade: any one marks should be above 80
   for C grade: both marks should be below 80'''

marks1=int(input("Enter the marks of english\n"))
marks2=int(input("Enter the marks of maths\n"))

if marks1>80 and marks2>80:
    print("AKARSH got A grade")
elif marks1>80 or marks2>80:
    print("AKARSH got B grade")
else:
    print("AKARSH got C grade")