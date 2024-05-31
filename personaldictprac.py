#creating a dictionary
numbers= {
    "akarsh":1023,
    "nitish":2410,
    "medhi" :3357,
    "bhatia":4101
}
print(numbers["akarsh"]) #printing a value of dictionary/accessing the value
print(numbers.get("akarsh"))
print(numbers.keys()) #print only key values
print(numbers) #printing whole dictionary 

print(type(numbers)) #checking the type of dictionary
print(len(numbers)) #checking the length of dictionary

#update the value of dictionary:
numbers["akarsh"]=1083
print(numbers)

#to add new key value pairs in dictionary at last:
numbers["khanna"]=2610
print(numbers)

#to add other dictionary to previous dictionary:
car={
    "buggati":"xyz"
}
numbers.update(car)
print(numbers)

#remove key-values from dictionary:
numbers.pop("bhatia")
print(numbers)

#remove key-value from anywhere:
del numbers["medhi"]

#to remove last added item 
numbers.popitem()
print(numbers)

#to empty the dictionary:
'''numbers.clear()
print(numbers)'''

#to print all keys of dictionary: (using for loop)
for i in numbers:
    print(i)
    print(numbers[i]) #print values

#nested dictionary:
person = {
    "watch" : {
        "titan":1000,
        "sonata":2000
    },
    "shoes" : {
        "puma":3000,
        "fila":4000
    }
}

print(person["shoes"]["puma"]) #printing nested dictionaries.