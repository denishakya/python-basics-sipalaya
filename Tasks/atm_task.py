balance = 12000
pin = 1234
pin_attempts = 3

print("Welcome to the ATM Machine".center(40, "="), "\n")

while pin_attempts > 0:
    user_pin = int(input("Enter your PIN: "))
    if user_pin == pin:
        print("\nPIN accepted. Welcome!\n")
        
        while True:
            print("""
                ATM MENU
            1 --> Check Balance
            2 --> Withdraw Money
            3 --> Deposit Money
            4 --> Exit
            """)
            
            choice = input("Choose an option (1-4): ")
            
            if choice == '1':
                print(f"\nYour current balance is: {balance}\n")
            
            elif choice == '2':
                withdraw_amount = int(input("Enter withdrawal amount (max 20000): "))
                if withdraw_amount <= 0:
                    print("\nInvalid amount!\n")
                elif withdraw_amount > balance:
                    print("\nInsufficient balance!\n")
                elif withdraw_amount > 20000:
                    print("\nWithdrawal limit exceeded!\n")
                else:
                    balance -= withdraw_amount
                    print(f"\nWithdrawal successful! Remaining balance: {balance}\n")
                    print("Thank you for your transaction!\n")
                break
            
            elif choice == '3':
                deposit_amount = int(input("Enter deposit amount (max 20000): "))
                if deposit_amount <= 0:
                    print("\nInvalid amount!\n")
                elif deposit_amount > 20000:
                    print("\nDeposit limit exceeded!\n")
                else:
                    balance += deposit_amount
                    print(f"\nDeposit successful! Current balance: {balance}\n")
                    print("Thank you for your transaction!\n")
                break
            
            elif choice == '4':
                print("\nThank you for using our ATM. Goodbye!\n")
                break
            
            else:
                print("\nInvalid option. Please choose again.\n")
        
        break
    
    else:
        pin_attempts -= 1
        if pin_attempts == 0:
            print("\nIncorrect PIN entered 3 times. Your account is blocked!\n")
        else:
            print(f"\nWrong PIN! Attempts left: {pin_attempts}\n")
