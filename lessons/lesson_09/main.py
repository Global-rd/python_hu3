from bankaccount import BankAccount, InsufficientFundsError, InvalidAmountError
import pprint

def main():
    
    account_1 = BankAccount("Tim", "HU123", 500)
    account_2 = BankAccount("Jim", "HU456", 1500)
    account_3 = BankAccount("Timmy", "HU789")

    account_1.deposit(500)
    account_1.deposit(1500)
    account_1_balance = account_1.get_balance()
    print(account_1_balance)

    #try:
    #    account_2.withdraw(2000)
    #except InsufficientFundsError:
    #    print("Not enough money")

    account_2.withdraw(1000)
    acc1_transaction_log = account_1.get_transaction_history()
    print(acc1_transaction_log)



if __name__ == "__main__":
    main()