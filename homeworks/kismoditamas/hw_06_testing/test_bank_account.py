from unittest import mock
import pytest
from bank_account import BankAccount


@pytest.fixture
def bank_account_with_zero() -> BankAccount:
    return BankAccount(owner="Tim", balance=0.0)

@pytest.fixture
def bank_account_with_hundred() -> BankAccount:
    return BankAccount(owner="Tom", balance=100.0)

def test_account_creation(bank_account_with_hundred: BankAccount) -> None:
    """Tests if the account is initialized with the correct owner and balance."""
    assert bank_account_with_hundred.owner == "Tom"
    assert bank_account_with_hundred.get_balance() == 100.0


def test_initial_negative_balance_raises_error() -> None:
    """Tests if creating an account with a negative balance raises a ValueError."""
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Bad User", -100.0)

@pytest.mark.parametrize("invalid_amount,  expected_exception, message", 
                         [
                        (0, ValueError, "Deposit amount must be bigger than zero."),
                        (-10, ValueError, "Deposit amount must be positive."), 
                        (-0.001, ValueError, "Deposit amount must be positive."),
                        ("100", TypeError, "Amount must be a number.")
                        ])
def test_deposit_invalid_amount_raises_value_error(bank_account_with_zero, invalid_amount, expected_exception, message):    
    with pytest.raises(expected_exception, match=message):
        bank_account_with_zero.deposit(invalid_amount)

@pytest.mark.parametrize("invalid_amount,  expected_exception, message", 
                         [
                        (0, ValueError, "Withdraw amount must be bigger than zero."),
                        (-10, ValueError, "Withdraw amount must be positive."), 
                        (101, ValueError, "Insufficient funds."),
                        ("100", TypeError, "Amount must be a number.")
                        ])
def test_withdraw_invalid_amount_raises_value_error(bank_account_with_hundred, invalid_amount, expected_exception, message):    
    with pytest.raises(expected_exception, match=message):
        bank_account_with_hundred.withdraw(invalid_amount)


@pytest.mark.parametrize("invalid_amount,  expected_exception, message", 
                         [
                        (0, ValueError, "Withdraw amount must be bigger than zero."),
                        (-10, ValueError, "Withdraw amount must be positive."), 
                        (101, ValueError, "Insufficient funds."),
                        ("100", TypeError, "Amount must be a number.")
                        ])
def test_transfer_to_raises_amount_errors(bank_account_with_hundred, invalid_amount, expected_exception, message) :
    test_bank_account = BankAccount("Test", 50.0)
    with pytest.raises(expected_exception, match=message):
        bank_account_with_hundred.transfer(invalid_amount, test_bank_account)    

def test_transfer_to_account_itself_raises_value_error(bank_account_with_hundred) :
    with pytest.raises(ValueError, match="Cannot transfer to the same account."):
        bank_account_with_hundred.transfer(10, bank_account_with_hundred)

def test_transfer_to_good_scenario(bank_account_with_hundred) :
    target_account = BankAccount("Target", 50.0)
    bank_account_with_hundred.transfer(30.0, target_account)
    assert bank_account_with_hundred.get_balance() == 70.0
    assert target_account.get_balance() == 80.0