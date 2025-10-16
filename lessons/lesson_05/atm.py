import os
import dotenv
dotenv.load_dotenv()

correct_pin = os.environ.get("PIN")
account_balance = 500.00

pin = input("Please enter PIN: ")

if pin == correct_pin:
    print("PIN accepted")
    print(f"Your current balance: $ {account_balance:.1f}")
    withdrawal_amount = float(input("Enter the amount you want to withdraw: $"))
    if withdrawal_amount > 0:
        if withdrawal_amount <= account_balance:
            account_balance -= withdrawal_amount
            print(f"Withdrawal successful! Your new balance is: $ {account_balance:.1f}")
        else:
            print("Insufficient funds.")
    else:
        print("Invalid amount. Please enter a positive number!")
else:
    print("Incorrect PIN. Please Try again!")