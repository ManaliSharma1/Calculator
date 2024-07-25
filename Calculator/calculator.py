print("***** SIMPLE CALCULATOR *****")
def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        print("Select an operation:")
        print("+: Addition")
        print("-: Subtraction")
        print("*: Multiplication")
        print("/: Division")
        print("%: Remainder")
        print("q: Exit")

        choice = input("Enter your choice to perform operations (+, -, *, /, %) or q for exit: ")

        if choice == '+':
            result = num1 + num2
            print("The result of", num1, "+", num2, "is: ", result, "\n")
        elif choice == '-':
            result = num1 - num2
            print("The result of", num1, "-", num2, "is: ", result, "\n")
        elif choice == '*':
            result = num1 * num2
            print("The result of", num1, "*", num2, "is: ", result, "\n")
        elif choice == '/':
            result = num1 / num2
            print("The result of", num1, "/", num2, "is: ", result, "\n")
        elif choice == '%':
            result = num1 % num2
            print("The result of", num1, "%", num2, "is: ", result, "\n")
        elif choice == 'q':
            break
        else:
            print("Invalid choice, please enter a valid operation\n")

calculator()
