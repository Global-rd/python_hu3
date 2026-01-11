import pytest
from bank_account import BankAccount
from unittest.mock import patch

@pytest.fixture
def empty_account():
    return BankAccount("User_1")

@pytest.fixture
def another_account():
    return BankAccount("User_2", 100.0)

def test_depostit_no_balance(empty_account):
    empty_account.deposit(100.0)

    assert empty_account.balance == 100.0
    assert empty_account.owner == "User_1"

def test_deposit_with_balance(another_account):
    another_account.deposit(400.0)

    assert another_account.balance == 500.0
    assert another_account.owner == "User_2"

@pytest.mark.parametrize("amount, exception_expected",
                        [
                            (-100, ValueError), 
                            (0, ValueError)  
                        ])  
def test_deposit_invalid_input(empty_account, amount, exception_expected):    
     with pytest.raises(exception_expected):
          empty_account.deposit(amount)
