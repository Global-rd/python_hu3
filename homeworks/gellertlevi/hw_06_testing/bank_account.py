class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.balance += amount
    
    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds.")
        self.balance -= amount

    def transfer(self, amount: float, target_account: 'BankAccount'):
        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be a BankAccount instance.")
        self.withdraw(amount)
        target_account.deposit(amount)
    
    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account owner: {self.owner}, Balance: {self.balance:.2f}"
    

    #unit tests

import pytest
from bank_account import BankAccount  

# Fixtures 
@pytest.fixture # test account1
def account_alice():
    
    return BankAccount("Alice", 100)

@pytest.fixture
def account_bob(): # test account2
    
    return BankAccount("Bob", 200)

# parametrize
@pytest.mark.parametrize(
    "amount, should_raise",
    [
        (0, True),       #  0 betét
        (-10, True),     # negatív betét
        (50, False)      # Normál betét
    ]
)
def test_deposit(account_alice, amount, should_raise):
    
    if should_raise:
        with pytest.raises(ValueError):
            account_alice.deposit(amount)
    else:
        old_balance = account_alice.get_balance()
        account_alice.deposit(amount)
        assert account_alice.get_balance() == old_balance + amount

# Withdraw test
def test_withdraw(account_alice):
    
    
    account_alice.withdraw(50)
    assert account_alice.get_balance() == 50

    
    with pytest.raises(ValueError):
        account_alice.withdraw(1000)

    
    with pytest.raises(ValueError):
        account_alice.withdraw(-20)

    
    with pytest.raises(ValueError):
        account_alice.withdraw(0)

# Transfer test
def test_transfer(account_alice, account_bob):
    
    
    account_alice.transfer(50, account_bob)
    assert account_alice.get_balance() == 50
    assert account_bob.get_balance() == 250

    
    with pytest.raises(ValueError):
        account_alice.transfer(1000, account_bob)

    
    with pytest.raises(TypeError):
        account_alice.transfer(10, "not_an_account")


def test_initial_balance_negative():
    
    with pytest.raises(ValueError):
        BankAccount("Charlie", -100)

# String representation
def test_str_method(account_alice):
    
    result = str(account_alice)
    assert "Alice" in result
    assert f"{account_alice.get_balance():.2f}" in result
