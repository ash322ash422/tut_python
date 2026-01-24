# Simple Grocery List Manager (Beginner Version)

grocery = {}

while True:
    print("\n--- Grocery Manager ---")
    print("1. Add item")
    print("2. View items")
    print("3. Remove item")
    print("4. Total bill")
    print("5. Exit")

    choice = input("Enter choice (1-5): ")

    # Add item
    if choice == "1":
        item = input("Enter item name: ").lower()
        quantity = int(input("Enter quantity: "))
        price = float(input("Enter price: "))

        grocery[item] = quantity * price
        print("Item added!")

    # View items
    elif choice == "2":
        if not grocery:
            print("Grocery list is empty.")
        else:
            print("\nItem\tTotal Price")
            print("-" * 20)
            for item, total in grocery.items():
                print(f"{item}\t{total}")

    # Remove item
    elif choice == "3":
        item = input("Enter item name to remove: ").lower()

        if item in grocery:
            del grocery[item]
            print("Item removed.")
        else:
            print("Item not found.")

    # Total bill
    elif choice == "4":
        total_bill = 0
        for total in grocery.values():
            total_bill += total

        print(f"Total Bill: ₹{total_bill}")

    # Exit
    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")
