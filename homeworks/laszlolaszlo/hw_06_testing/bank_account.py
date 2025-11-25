class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("Owner must be a non-empty string.")
        if not isinstance(balance, (int, float)):
            raise TypeError("Initial balance must be a number.")
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner.strip()
        self.balance = float(balance)

    def deposit(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Deposit amount must be a number.")
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if not isinstance(amount, (int, float)):
            raise TypeError("Withdraw amount must be a number.")
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount') -> None:
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        if self == target_account:
            raise ValueError("Cannot transfer money to the same account.")
        self.withdraw(amount)
        target_account.deposit(amount)

    def get_balance(self) -> float:
        return self.balance

    def __str__(self) -> str:
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"