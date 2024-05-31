#creating a string
name1="akarsh"
name2="gullu"
name3="nitish"
print(name1,name2,name3)
print(type(name1))

#indexing in string:
college="parul university"
print(college[0])
print(college[4])
print(college[-7]) #negative indexing

#traversing through string:
for i in college: #by for loop
    print(i)

#by list comprehension:
list=(char for char in college)
for i in list:
    print(i)

#find the length of string:
print(len(college))

#sliceing:
print(college[:5])
print(college[5:])
print(college[6:9])  #from index 6 to before index 9 (not including 9)
print(college[:-3:-1]) #negative indexing
print(college[-3:])
print(college[-3:-1])
print(college[:-1])

#modifying string:
country="bharat"
str5=country.upper()
print(str5) #prints string in uppercase
str6=country.lower()
print(str6) #prints string in lowercase
str7=country.title()
print(str7) #capitalize first letter of each word
str8=country.capitalize()
print(str8) #capatilize only the first letter of the string
str9="   hello   "
print(str9.strip()) #removes leading and trailing spaces
s='''i am akarsh 
akarsh is 20 years old'''
print("akarsh","gullu",2)
b="guava pineapple banana"
print(b.split()) #splits at white space by default

#concatinating the string:
n1="AKARSH"
n2="JHA"
n3= n1+n2
print(n3)

#formating a string:
name="akarsh"
age=20
print(f"my name is {name} and i am {age}")
#or
str17="my name is {} and i am {}".format(name,age)
#or
str23="my name is {n} and i am {a}".format(n=name,a=age)