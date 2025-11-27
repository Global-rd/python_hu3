from typing import Literal
import pytest
from bank_account import BankAccount
from unittest.mock import patch

@pytest.fixture
def zero_balance_account():
    return BankAccount('Zero', 0.0)

@pytest.fixture
def with_balance_account():
    return BankAccount('Angie', 2000.0)

def test_deposit_zero_balance(zero_balance_account: BankAccount):   
    zero_balance_account.deposit(300.0)
    
    assert zero_balance_account.balance == 300.0

def test_deposit_with_balance(with_balance_account: BankAccount):
    with_balance_account.deposit(500.0)
    
    assert with_balance_account.balance == 2500.0

@pytest.mark.parametrize("owner,amount,expected_exception",
     [
          ("Bob",-1000, ValueError), # Negatív
          ("Cecil",0, ValueError)    # zero
     ]
)

@pytest.mark.parametrize("invalid_amount", [0, -50, -0.01])
def test_deposit_invalid_amount_raises_value_error(zero_balance_account: BankAccount, invalid_amount: float | Literal[0] | Literal[-50]):
    initial_balance = zero_balance_account.balance
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        zero_balance_account.deposit(invalid_amount)
    assert zero_balance_account.balance == initial_balance

# 2000 - 500
def test_withdraw_valid_amount(with_balance_account: BankAccount):
    with_balance_account.withdraw(500.0)
    assert with_balance_account.balance == 1500.0   

@pytest.mark.parametrize("invalid_amount", [0, -20])
def test_withdraw_invalid_amount_raises_value_error(with_balance_account: BankAccount, invalid_amount: float | Literal[0] | Literal[-20]):
    initial_balance = with_balance_account.balance
    with pytest.raises(ValueError, match="Withdrawal amount must be positive."):
        with_balance_account.withdraw(invalid_amount)
    assert with_balance_account.balance == initial_balance

# 2000 - 2500
def test_withdraw_valid_amount(with_balance_account: BankAccount):
    invalid_amount = 2500
    initial_balance = with_balance_account.balance
    with pytest.raises(ValueError, match="Insufficient funds."):
        with_balance_account.withdraw(invalid_amount)
    assert with_balance_account.balance == initial_balance

def test_transfer_another_account(with_balance_account: BankAccount, zero_balance_account: BankAccount):
    with_balance_account.transfer(1000.0, zero_balance_account)
    
    assert with_balance_account.balance == 1000.0 # 2000 - 1000
    assert zero_balance_account.balance == 1000.0 # 0 + 1000

def test_transfer_same_account_raises_value_error(with_balance_account: BankAccount):
    with pytest.raises(ValueError, match="Cannot transfer to the same account."):
        with_balance_account.transfer(1000.0, with_balance_account)