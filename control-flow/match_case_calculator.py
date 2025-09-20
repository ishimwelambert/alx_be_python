num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case "+":  # Addition
        print("The result is:", num1 + num2)
    case "-":  # Subtraction
        print("The result is:", num1 - num2)
    case "*":  # Multiplication
        print("The result is:", num1 * num2)
    case "/":  # Division
        if num2 != 0:
            print("The result is:", num1 / num2)
        else:
            print("Cannot divide by zero")
    case _:  # Default
        print("Invalid operator entered.")


