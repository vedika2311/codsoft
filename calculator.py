
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("*************************************************")
print ("           Command Line CALCULATOR            ")
print("*************************************************")
print()
print("Which operation you want to perform..?")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:

    choice = input("Enter choice(1/2/3/4): ")  # take input from the user

    if choice in ('1', '2', '3', '4'):   # check if choice is one of the four options
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            result = add(num1, num2)
            print(num1, "+", num2, "=", result)
            print("Answer = ",result)

        elif choice == '2':
            result = subtract(num1, num2)
            print(num1, "-", num2, "=", result)
            print("Answer = ", result)

        elif choice == '3':
            result = multiply(num1, num2)
            print(num1, "*", num2, "=",result)
            print("Answer = ", result)

        elif choice == '4':
            result = divide(num1, num2)
            print(num1, "/", num2, "=", result)
            print("Answer = ", result)



        decision = input("Do you want to perform next calculation? (yes/no): ")      # check if user wants another calculation
        if decision == "yes":  # continue the while loop if answer is yes
            continue

        elif decision == "no": # break the while loop if answer is no
            break

        else:
            print("Invalid input")

    else:
        print("Oops wrong choice code...Please Enter valid choice code")
