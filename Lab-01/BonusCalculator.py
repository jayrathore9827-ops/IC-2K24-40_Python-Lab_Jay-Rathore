while True:
    print("\n--- Calculator Menu ---\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Select an option (1-5): ")

    if choice == "5":
        print("Exiting calculator. Goodbye!")
        break

    if choice in ("1", "2", "3", "4"):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == "1":
            print(f"Result: {a + b}")
        elif choice == "2":
            print(f"Result: {a - b}")
        elif choice == "3":
            print(f"Result: {a * b}")
        elif choice == "4":
            print(f"Result: {a / b}" if b != 0 else "Error: Division by zero.")
    else:
        print("Invalid selection. Try again.")