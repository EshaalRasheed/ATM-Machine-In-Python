print("Welcome To ATM Machine")

correct_pin = "1234"
pin = input("Enter Your PIN: ") 
if pin == correct_pin:
    print("Pin is Correct")
    balance = 5000  

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            print(f"Your Current Balance is {balance}")
        
        elif choice == "2":
            amount = input("Enter the amount you want to deposit: ")
            if amount.isdigit():
                balance += int(amount)
                print(f"Your updated balance is {balance}")
            else:
                print("Invalid Input! Please enter a number")
        
        elif choice == "3":
            amount = input("Enter the amount you want to withdraw: ")
            if amount.isdigit():
                amount = int(amount)  
                if amount <= balance:
                    balance -= amount
                    print(f"You have withdrawn {amount}. Your current balance is {balance}")
                else:
                    print("Insufficient Funds")
            else:
                print("Invalid Input! Please enter a number")
        
        elif choice == "4":
            print("Thanks For Using ATM! Goodbye")
            break  
        
        else:
            print("Invalid Choice: Please Try again")
else:
    print("Invalid Pin Entered")
