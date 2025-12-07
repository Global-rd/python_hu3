class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        #nem szám típusú balance esetén is TypeError-t kell dobni
        if not isinstance(balance, (int, float)):
            raise TypeError("Balance must be a number.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        #nem szám típusú amount esetén is TypeError-t kell dobni
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.") 
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        #nem szám típusú amount esetén is TypeError-t kell dobni
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdraw amount must be a number.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        #magadhoz nem lehet utalni
        if target_account is self:
            raise ValueError("Cannot transfer to the same account.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
    