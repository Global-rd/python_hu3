import pytest
from bank_account import BankAccount

# ---- Fixtures ----
@pytest.fixture
def account_a():
    return BankAccount("Alice", 100.0)

@pytest.fixture
def account_b():
    return BankAccount("Bob", 50.0)

# ---- Test initialization ----
def test_initial_balance_positive(account_a):
    assert account_a.get_balance() == 100.0

def test_initial_balance_negative():
    with pytest.raises(ValueError):
        BankAccount("Charlie", -10)

def test_owner_type_error():
    with pytest.raises(TypeError):
        BankAccount(123, 100)

# ---- Test deposit with parametrize ----
@pytest.mark.parametrize("amount", [0, -10])
def test_deposit_invalid_amount(account_a, amount):
    with pytest.raises(ValueError):
        account_a.deposit(amount)

def test_deposit_non_numeric(account_a):
    with pytest.raises(TypeError):
        account_a.deposit("abc")

def test_valid_deposit(account_a):
    account_a.deposit(50)
    assert account_a.get_balance() == 150.0

# ---- Test withdraw ----
def test_withdraw_valid(account_a):
    account_a.withdraw(50)
    assert account_a.get_balance() == 50.0

def test_withdraw_insufficient_funds(account_a):
    with pytest.raises(ValueError):
        account_a.withdraw(200)

def test_withdraw_non_numeric(account_a):
    with pytest.raises(TypeError):
        account_a.withdraw("xyz")

# ---- Test transfer ----
def test_transfer_valid(account_a, account_b):
    account_a.transfer(30, account_b)
    assert account_a.get_balance() == 70.0
    assert account_b.get_balance() == 80.0

def test_transfer_to_non_account(account_a):
    with pytest.raises(TypeError):
        account_a.transfer(10, "NotAnAccount")

def test_transfer_to_self(account_a):
    with pytest.raises(ValueError):
        account_a.transfer(10, account_a)

def test_transfer_invalid_amount(account_a, account_b):
    with pytest.raises(ValueError):
        account_a.transfer(-10, account_b)

def test_transfer_non_numeric_amount(account_a, account_b):
    with pytest.raises(TypeError):
        account_a.transfer("abc", account_b)

