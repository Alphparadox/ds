import server

def main_menu():
    """Displays the main menu and handles user choices."""
    while True:
        print("\n--- RPC Simulation Menu ---")
        print("1. Calculate Factorial")
        print("2. Use Basic Calculator")
        print("3. Check for Prime Number")
        print("4. Generate Fibonacci Series")
        print("5. Find Max in a List")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                num = int(input("Enter a non-negative integer for factorial: "))
                # This is the Remote Procedure Call
                result = server.factorial(num)
                print(f"RPC Response: The factorial of {num} is {result}")

            elif choice == 2:
                op = input("Enter operator (+, -, *, /): ")
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                # This is the Remote Procedure Call
                result = server.calculator(op, num1, num2)
                print(f"RPC Response: {num1} {op} {num2} = {result}")

            elif choice == 3:
                num = int(input("Enter an integer to check if it's prime: "))
                # This is the Remote Procedure Call
                result = server.is_prime(num)
                if result:
                    print(f"RPC Response: {num} is a prime number.")
                else:
                    print(f"RPC Response: {num} is not a prime number.")

            elif choice == 4:
                limit = int(input("Enter the limit for the Fibonacci series: "))
                # This is the Remote Procedure Call
                result = server.fibonacci_series(limit)
                print(f"RPC Response: Fibonacci series up to {limit}: {result}")

            elif choice == 5:
                str_arr = input("Enter a list of numbers separated by space: ")
                num_list = [int(n) for n in str_arr.split()]
                # This is the Remote Procedure Call
                result = server.find_max(num_list)
                print(f"RPC Response: The maximum value in {num_list} is {result}")

            elif choice == 6:
                print("Exiting the RPC client.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main_menu()