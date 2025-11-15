from typing import Literal
import pytest
from bank_account import BankAccount
from unittest.mock import patch

@pytest.fixture
def empty_account():
     return BankAccount("Attila")

@pytest.fixture
def another_account():
     return BankAccount("Peter", 100.0)


# Test #1 - Deposit test
def test_deposit_no_balance(empty_account):     
     empty_account.deposit(100.0)

     assert empty_account.balance ==  100.0
     assert empty_account.owner ==  "Attila"

# Test #2 - Deposit test

def test_deposit_with_balance(another_account):     
     another_account.deposit(400.0)

     assert another_account.balance ==  500.0
     assert another_account.owner ==  "Peter"

# Test #3 - Deposit test zero, negative values

@pytest.mark.parametrize("owner,amount,expected_exception",
     [
          ("Attila",-100, ValueError), # Negatív
          ("Attila",0, ValueError)      # zero
     ]
)
def test_deposit_invalid_input(empty_account, owner, amount, expected_exception):    
     with pytest.raises(expected_exception):
          empty_account.deposit(amount)

# Test #4 - Edge case
# Ehhez google segítség kellett, de nem teljesen világos ennek a működése, mert az  előző példában meg kellett adni expected_exception-t és az a paraméter szerepelt a raise-ben.

def test_transfer_to_non_bank_account_raises(another_account):    
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        another_account.transfer(10.0, "not-an-account")

# Test 5 - Withdraw not enought money or negative
# Itt nem tudom, hogy kell -e vizsgálni, hogy melyik raise-ágra kerül a végrehajtás?
@pytest.mark.parametrize("amount,expected_exception",
     [
          (-100, ValueError), 
          (200, ValueError),
           ("alma",TypeError) 
     ]
)
def test_withdraw_not_money(another_account, amount, expected_exception):
     with pytest.raises(expected_exception):
          another_account.withdraw(amount)

