#testelő py file Mesefigurák banki számlájához

from bank_account import BankAccount
import pytest


@pytest.fixture
def account():
    return BankAccount("Tom&Jerry", 100.0)

@pytest.fixture
def account_2():
    return BankAccount("Captain_Balu", 50.0)

@pytest.mark.parametrize("amount", [-50.0, 10.0])
def test_deposit_invalid_values(account: BankAccount, amount):
    with pytest.raises(ValueError):
        account.deposit(amount)

#-----------------------------

def test_deposit_negative_amount(account: BankAccount):
   
    with pytest.raises(ValueError):
        account.deposit(-50)

def test_deposit_non_number(account_2: BankAccount):
    
    with pytest.raises(TypeError):
        account_2.deposit("fifty")

def test_withdraw_negative_amount(account: BankAccount):
    
    with pytest.raises(ValueError):
        account.withdraw(-30)

def test_withdraw_non_number(account_2: BankAccount):
    
    with pytest.raises(TypeError):
        account_2.withdraw("fifty")

def test_withdraw_insufficient_funds(account: BankAccount):
    
    with pytest.raises(ValueError):
        account.withdraw(150)

def test_transfer_to_self(account: BankAccount):
    
    with pytest.raises(ValueError):
        account.transfer(50, account)

        
def test_transfer_insufficient_funds(account: BankAccount, account_2: BankAccount):
    with pytest.raises(ValueError):
        account.transfer(150, account_2)
