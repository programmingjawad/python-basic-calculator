
#takes input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Operators:\n Addition = + \n Subtraction = - \n Multiplication = * \n Division = /")
op = (input("Enter a operator: "))
# returns the result
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator.\n Make sure to add the correct number for operators")
new_math = True
# creates a continuous loop for the calculator if input from user is yes
while new_math:
    new_mat = input("Do you want to use the calculator again? (yes/no): ")
    if new_mat == "yes":
        num1 = float(input("Enter first number: "))

        num2 = float(input("Enter second number: "))
        print("Operators:\n Addition = + \n Subtraction = - \n Multiplication = * \n Division = /")
        op = (input("Enter a operator: "))
        if op == "+":
            print(num1 + num2)
        elif op == "-":
            print(num1 - num2)
        elif op == "*":
            print(num1 * num2)
        elif op == "/":
            print(num1 / num2)
        else:
            print("Invalid operator.\n Make sure to add the correct number for operators")
    elif new_mat == "no":
        print("Thanks for using our calculator")
        break
    else:
        print("Make sure to type the correct input.")
# if the user input is not valid , prints the statement
else:
    print("Invalid input")
# ends the loop if the user input is no
if new_math == "no":
    print("See you again!!!")
