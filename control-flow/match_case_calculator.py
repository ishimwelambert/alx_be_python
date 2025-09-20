num1=int(input("Enter the first number:"))
num2=int(input("Enter the second number:"))
operator=input("Choose the operation (+, -, *, /):")
match operator:
    case addition if operator=="+":
        print(f"The result is {num1+num2}")
    case subtract if operator=="-":
        print(f"The result is {num1-num2}")
    case multiply if operator=="*":
        print(f"The result is {num1*num2}")
    case divide if operator=="/" and num2!=0:
        print(f"The result is {num1/num2}")
    case divide if operator=="/" and num2==0:
        print("cannot divide by zero")