import datetime

print("WELCOME TO THE ATM MACHINE")

password = 5555
balance = 2000
transaction = []   # empty list
attempt = 0
max_attempts = 3

while attempt < max_attempts:
    pin = int(input("Enter the 4-digit ATM pin: "))

    if pin == password:
        print("--- Access Granted ---")

        while True:
            print("\n----- Select an option to perform -----")
            print("1. Check Balance")
            print("2. Deposit Balance")
            print("3. Withdraw Balance")
            print("4. Mini Statement")
            print("5. Exit")

            choice = int(input("Enter number (1/2/3/4/5): "))

            # 1️ : Check Balance
            if choice == 1:
                print(f"Current Balance: Rs {balance}")

            # 2️ : Deposit
            elif choice == 2:
                deposit = int(input("Enter the amount you want to deposit: Rs "))
                balance += deposit
                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                transaction.append((time, f"Deposited: Rs {deposit}"))
                print(f"Deposited successfully! New Balance: Rs {balance}")

            # 3️ :Withdraw
            elif choice == 3:
                withdraw = int(input("Enter the amount you want to withdraw: Rs "))
                if withdraw <= balance:
                    balance -= withdraw
                    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    transaction.append((time, f"Withdrawn: Rs {withdraw}"))
                    print(f"Withdrawn successfully! New Balance: Rs {balance}")
                else:
                    print("Insufficient balance!")

            # 4️ :Mini Statement
            elif choice == 4:
                print("\n--- Mini Statement ---")
                if not transaction:
                    print("No transactions yet.")
                else:
                    for t in transaction:
                        print(f"{t[0]} -> {t[1]}")
                    print(f"Available Balance: Rs {balance}")

            # 5 Exit
            elif choice == 5:
                print("Thank you for using the ATM machine! Please visit again.")
                break

            else:
                print("Invalid input! Please select between 1–5.")

        break   # exit after successful login

    else:
        attempt = attempt+1   #0+1
        remaining = max_attempts - attempt #3-1=2
        print(f"Incorrect PIN! Attempts left: {remaining}")

        if remaining == 0:
            print("Account blocked! Please try again later.")
            break