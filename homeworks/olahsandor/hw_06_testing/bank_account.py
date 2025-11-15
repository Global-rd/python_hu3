class BankAccount:
    """
        Bankszámla inicializálása: tulajdonos, egyenleg.
        owner: A számla tulajdonosa.
        balance: A számla kezdő egyenlege.
        ValueError: Ha a kezdő egyenleg negatív.
    """
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    """
        Pénz befizetése a számlára.
        amount: A befizetendő összeg.
        ValueError: Ha az összeg nem pozitív.
    """
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    """
        Pénz kivétele.
        amount: A kivenni kívánt összeg.
        ValueError: Ha az összeg nem pozitív/nincs fedezet.
    """
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    """
        Pénz átutalása egy másik Bankszámlára.
        amount: Az átutalandó összeg.
        target_account: A cél bankszámla.
        TypeError: Ha a cél nem BankAccount típusú.
        ValueError: Ha nincs elegendő fedezet.
    """
    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    """
        Visszaadja a számla aktuális egyenlegét.
    """
    def get_balance(self):
        return self.balance
    
    """
        Visszaadja a számla tulajdoonosát és annyak egyenlegét.
    """
    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"