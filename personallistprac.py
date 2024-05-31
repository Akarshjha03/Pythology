fruits= ["guava","pineapple","banana"] #creation of a list
car=["Bugatti","lamborghini","farraari","ford"]
car[3]="mclaren" #updating a list
print(car)
print(fruits) #printing a list
print(type(fruits)) #checking the type of list
print(len(fruits)) #checking the type of list

#using membership datatype: in , not in
# identity data type: is , is not
if "banana" in fruits:
    print("banana is a part of list")

if "AUDI" not in car:
    print("AUDI is not a supercar")

#accessing items of a list:
    
#using indexing:
print(car[0])
#using negative indexing:
print(car[-3])
#using indexing range:
print(car[0:4])
#using negative indexing:
print(car[-4:-1])

#adding element to a list:
car.append("jaguar") #using append() to add items ina list from last
print(car)

car.insert(2,"Dugatti") #using insert() to add element inside a list at any particular index
print(car)

watch=["Titan","Sonata","Rolex"]
car.extend(watch) #using extend() to add a another list of any datatype to the previous list from last
print(car)        #its like concating 2 lists

#To remove elements from a list:
car.remove("Dugatti") #to remove a specific item from list
print(car)

car.pop(4) #to remove a item from specific index in list
print(car)
car.pop() #to remove a item form list at last
print(car)

#to change a item inside a list:
fruits[1]="mango" #to change a value at a specific index
print(fruits)

fruits[1:2]=["muskmelon","papaya"] #to change value at range  of indexes
print(fruits)

#sorting of list i.e ascending & decending
num=[10,20,40,50,30]
num.sort() #for sorting in acsending order which is by default
print(num)

num.sort(reverse=True) #for sorting in decending order
print(num)

'''we can also reverse the list'''
num.reverse()

#list comprehension
new_num= [i for i in num if i>25] #creating new list using items of existing list
print(new_num)

#copy a list
copied_num=num.copy()
print(copied_num)

#concate 2 lists: other ways then extending
new=fruits+car
print(new)

#nested list
list=[10,20,[100,200],40,50]
print(list[2][0])