class Person(): #declaring a class
 def __init__(self,a,b): #constuctor: this fn is compulsary in class
    #self is parameter , you can give parameter any name
    #connstuctor is a special type of function used to create an object
    self.a=a #
    self.b=b

student=Person("akarsh",20)
print(student.a)  #accessing the attribute of object using dot operator (.)
print(student.b)
    

