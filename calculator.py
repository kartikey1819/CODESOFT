def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    else:
        return x / y

def get_user_choice():
    print("enter operator:")
    print("+")
    print("-")
    print("*")
    print("/")
    return input("Enter choice (+/-/*//): ")

def main():
    while True:
        try:
            choice = get_user_choice()

            if choice in ('+', '-', '*', '/'):
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '+':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '-':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '*':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '/':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")

                # Ask user if they want to calculate again
                again = input("Do you want to calculate again? (yes/no): ").lower()
                if again != 'yes':
                    break
            else:
                print("Invalid input. Please enter 1, 2, 3, or 4.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
