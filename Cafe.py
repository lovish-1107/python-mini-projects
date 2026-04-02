def show_menu():
    print("\n--- Cafe Menu ---")
    print("1. Coffee - ₹100")
    print("2. Tea - ₹50")
    print("3. Sandwich - ₹150")
    print("4. Pizza - ₹250")


def get_price(choice):
    if choice == 1:
        return 100
    elif choice == 2:
        return 50
    elif choice == 3:
        return 150
    elif choice == 4:
        return 250
    else:
        return 0


def cafe_system():
    total = 0

    while True:
        show_menu()
        choice = int(input("Enter item number: "))
        qty = int(input("Enter quantity: "))

        price = get_price(choice)

        if price == 0:
            print("Invalid item!")
            continue

        total += price * qty

        more = input("Do you want to order more? (y/n): ")
        if more.lower() != 'y':
            break

    gst = total * 0.05   # 5% GST
    final_bill = total + gst

    print("\n--- Final Bill ---")
    print("Total Amount:", total)
    print("GST (5%):", gst)
    print("Final Amount:", final_bill)


# Run program
cafe_system()