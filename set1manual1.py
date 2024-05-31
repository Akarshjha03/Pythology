'''A program that converts temperatures from Fahrenheit to Celsius and vice versa.'''


#Celsius to Fahrenheit:
celsius = int(input("Enter the Temperature in Celsius :\n"))
Fahrenheit = (1.8 * celsius) + 32
print("Temperature in Fahrenheit :", Fahrenheit)

#Fahrenheit to Celsius:
Fahrenheit = float(input("Enter the Temperature in Fahrenheit :\n"))
Celsius = ((Fahrenheit-32)*5)/9
print("Temperature in Celsius :", Celsius)