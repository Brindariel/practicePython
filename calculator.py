# Simple calculator with a "do-while" loop using a while loop

additional = "1. Add"
subtraction = "2. Subtract"
multiplication = "3. Multiply"
divide = "4. Divide"


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."



def calculator():
    while True:
     

        print("\nSelect Operation:")
        print(additional)
        print(subtraction)
        print(multiplication)
        print(divide)

        
        choice = input("Enter choice 1. 2. 3. 4. : ")

   
        if choice == 'q':
            print("Exiting the calculator.")
            break


        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid choice! Please select a valid operation 1. 2. 3. 4. :.")

     
        again = input("Do you want to perform another operation? (yes/no): ").strip().lower()

        if again not in ['yes', 'y']:
            print("Thank you for using the calculator!")
            break

# Run the calculator with the do-while loop
calculator()
