from typing import Literal
import pytest
from bank_account import BankAccount

@pytest.fixture
def empty_balance():
    return BankAccount("Test User", balance=0.0)

@pytest.fixture
def account_with_balance():
    return BankAccount("Bob Doyle", 100.0)

def test_deposit_item(empty_balance: BankAccount):
    empty_balance.deposit(200)
    assert empty_balance.get_balance() == 200

def test_deposit_negative_item(empty_balance: BankAccount):
    with pytest.raises(ValueError):
        empty_balance.deposit(-10)

def test_withdraw_success(account_with_balance: BankAccount):
    account_with_balance.withdraw(30)
    assert account_with_balance.get_balance() == 70

@pytest.mark.parametrize("amount, expected_exception",
                         [
                             ( -3, ValueError), #negative price
                             ( 0, ValueError), #zero amount
                             ( 5000, ValueError), #zeromore amount
                          ])
def test_withdraw_invalid_input(account_with_balance: BankAccount, amount: Literal[-3] | Literal[0] | Literal[5000], expected_exception: type[ValueError]):
    with pytest.raises(expected_exception):
        account_with_balance.withdraw(amount)


def test_transfer(empty_balance : BankAccount, account_with_balance: BankAccount):
    account_with_balance.transfer(20, empty_balance)
    assert account_with_balance.get_balance() == 80
    assert empty_balance.get_balance() == 20

def test_transfer_to_none_raises(account_with_balance: BankAccount):
    with pytest.raises(TypeError):
        account_with_balance.transfer(50, None)

def test_transfer_to_int_raises(account_with_balance: BankAccount):
    with pytest.raises(TypeError):
        account_with_balance.transfer(50, 12345)

def test_transfer_to_self_raises(account_with_balance: BankAccount):
    with pytest.raises(ValueError, match="Cannot transfer money to the same account"):
        account_with_balance.transfer(50, account_with_balance)