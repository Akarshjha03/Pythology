#using lamda function:
cube = lambda x: x**3
print(cube(5))

add = lambda x,y: x+y
print(add(2,3))
print(add(7,9))
print(add(6,1))


#inbulit map function:
squared_numbers = map(lambda x: x**2, [1, 2, 3, 4, 5])
print(list(squared_numbers)) #or list can also be removed
#or 
for i in squared_numbers:
    print(i)

#inbuild max function:
maximum = max(10, 20, 30)
print(maximum)

#inbuild min function:
minimum = min(10, 20, 30)
print(minimum)

