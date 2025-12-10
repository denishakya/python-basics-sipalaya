# Project 2 : Atm machine software 
# o using while loop,nested loop and control statemtents  


def atm_machine():
    balance = 1000
    pin = "1234"
    
    for attempt in range(3):
        entered_pin = input("Enter PIN: ")
        if entered_pin == pin:
            print("Access Granted")
            break
        else:
            print("Wrong PIN")
    else:
        print("Too many attempts! Exiting...")
        return

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print(f"Your balance: {balance}")
        elif choice == "2":
            amt = float(input("Enter amount to deposit: "))
            balance += amt
            print(f"Deposited {amt}. New balance: {balance}")
        elif choice == "3":
            amt = float(input("Enter amount to withdraw: "))
            if amt > balance:
                print("Insufficient balance!")
            else:
                balance -= amt
                print(f"Withdrawn {amt}. New balance: {balance}")
        elif choice == "4":
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice! Try again.")

print(atm_machine())