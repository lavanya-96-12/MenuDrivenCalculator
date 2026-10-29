def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    while True:
        print("\n=== Menu-Driven Calculator (Push 1) ===")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ").strip()
        if choice == '3':
            print("Exiting calculator. Goodbye!")
            break
        if choice in ['1', '2']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Error: Invalid numeric input. Please try again.")
                continue
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        else:
            print("Invalid selection. Please choose a valid menu option.")

if __name__ == "__main__":
    main()
