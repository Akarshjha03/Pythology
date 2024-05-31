#creation of tuple
color=("purple","orange","blue","yellow") #packing a tuple
print(color) #printing a tuple
#creating a tuple with single item:
color1=("orange",) #if comma is not given then it is considered as string
'''OR'''
color2=tuple(("purple"))

#checking the type:
print(type(color))
#check the length of tuple:
print(len(color))

#printing a item from the tuple using indexing 
print(color[1])
#negative indexing:
print(color[-1])
#printing using indexing range
print(color[0:4])
#printing using negative indexing range:
print(color[-5:-1])

#checking if a item exist in a tuple or not:
if "red" not in color: #using membership operator
    print("red is not in tuple")

#concate 2 tuples:(can be done with more)
color1=("blue","yellow")
color2=("purple","gold")
new_color=color1+color2
print(new_color)

#unpacking the tuple:
#ulta likha kyuki seedha likhna allowed nhi hai aaisa 
color3 , color4 ,color5 ,color6 = color
print(color3,color4,color5,color6)


