import pytest
from bank_account import BankAccount

@pytest.fixture
def account1():
    return BankAccount("Laci", 1000)

@pytest.fixture
def account2():
    return BankAccount("Laci2", 500)

@pytest.mark.parametrize("amount", [0, -10])
def test_deposit_invalid_amount_raises(account1, amount):
    with pytest.raises(ValueError):
        account1.deposit(amount)

def test_deposit_invalid_type_raises(account1):
    with pytest.raises(TypeError):
        account1.deposit("asd")

def test_deposit_valid(account1):
    account1.deposit(200)
    assert account1.get_balance() == 1200

@pytest.mark.parametrize("amount", [0, -50])
def test_withdraw_invalid_amount_raises(account1, amount):
    with pytest.raises(ValueError):
        account1.withdraw(amount)

def test_withdraw_invalid_type_raises(account1):
    with pytest.raises(TypeError):
        account1.withdraw([50])

def test_withdraw_insufficient_funds(account1):
    with pytest.raises(ValueError):
        account1.withdraw(2000)

def test_withdraw_valid(account1):
    account1.withdraw(300)
    assert account1.get_balance() == 700

def test_transfer_to_non_account_object_raises(account1):
    with pytest.raises(TypeError):
        account1.transfer(100, "not_account")

def test_transfer_to_self_raises(account1):
    with pytest.raises(ValueError):
        account1.transfer(100, account1)

@pytest.mark.parametrize("amount", ["100", None])
def test_transfer_invalid_amount_type_raises(account1, account2, amount):
    with pytest.raises(TypeError):
        account1.transfer(amount, account2)

def test_transfer_insufficient_funds(account1, account2):
    with pytest.raises(ValueError):
        account1.transfer(5000, account2)

def test_successful_transfer(account1, account2):
    account1.transfer(200, account2)
    assert account1.get_balance() == 800
    assert account2.get_balance() == 700

def test_initial_balance_invalid_type():
    with pytest.raises(TypeError):
        BankAccount("John", "1000")

def test_initial_balance_negative():
    with pytest.raises(ValueError):
        BankAccount("John", -100)
