

print("Select an operator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Remainder")
operation = input()
if operation == "1":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number"))
    print(num1 + num2)
elif operation == "2":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(num1 - num2)
elif operation == "3":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second"))
    print(num1 * num2)
elif operation == "4":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(num1 / num2)
elif operation == "5":
    num1 = float(input("Enter first number"))
    num2 = float(input("Enter second number"))
    print(num1)
else:
    print("Invalid")