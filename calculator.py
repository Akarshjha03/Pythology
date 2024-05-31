num1=int(input("Enter num1:"))
num2=int(input("Enter num2:"))

operator=input("enter operator:")

match operator:
    case "+":
        print("the sum is:",num1+num2)
    case "-":
        print("the difference is:",num1-num2)
    case "*":
        print("the product is:",num1*num2)
    case "/":
        print("the division is:",num1/num2)
    case "%":
        print("the modulo is:",num1%num2)
    case "**":
        print("the exponent is:",num1**num2)
    case "//":
        print("the floor division is:",num1//num2)
    case _:
        print("Enter a valid operator")