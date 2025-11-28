import pytest
from bank_account import BankAccount
from unittest.mock import patch

@pytest.fixture
def acc1():
    return BankAccount("Olivia", 500)

@pytest.fixture
def acc2():
    return BankAccount("Tom", 300)

@pytest.mark.parametrize("amount", [0,-10])
def test_deposit_invalid_values(acc1, amount):
    with pytest.raises(ValueError):
        acc1.deposit(amount)

def test_transfer_to_non_account(acc1):
    with pytest.raises(TypeError):
        acc1.transfer(50, "nem_szamla")

def test_initial_balance_negative():
    with pytest.raises(ValueError):
        BankAccount("Olivia", -100)

def test_withdraw_insufficient_funds(acc1):
    with pytest.raises(ValueError):
        acc1.withdraw(1000)   # több mint 500

def test_deposit_non_numeric(acc1):
    with pytest.raises(TypeError):
        acc1.deposit("alma")

def test_withdraw_non_numeric(acc1):
    with pytest.raises(TypeError):
        acc1.withdraw("tíz")

def test_initial_balance_non_numeric():
    with pytest.raises(TypeError):
        BankAccount("Olivia", "száz")

def test_transfer_to_self(acc1):
    with pytest.raises(ValueError):
        acc1.transfer(50, acc1)


