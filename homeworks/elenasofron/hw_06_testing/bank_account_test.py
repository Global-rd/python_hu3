import pytest
from bank_account import BankAccount

#2 fixtures

@pytest.fixture
def account_balance() -> BankAccount:
    return BankAccount("Test User 1", 10000.0)

@pytest.fixture
def account_zero_balance() -> BankAccount:
    return BankAccount("Test User 2", 0.0)

def test_account_creation(account_balance: BankAccount) -> None:
    assert account_balance.owner == "Test User 1"
    assert account_balance.get_balance() == 10000.0

def test_withdraw_valid_amount(account_balance: BankAccount) -> None:
    account_balance.withdraw(2000.0)
    assert account_balance.get_balance() == 8000.0

def test_negative_amount() -> None:
    with pytest.raises(ValueError, match="Balance cannot be negative."):
        BankAccount("User types negative amount", -100.0)