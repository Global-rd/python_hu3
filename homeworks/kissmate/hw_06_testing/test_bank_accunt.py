import pytest
import bank_account

@pytest.fixture
def account():
    return bank_account.BankAccount("Test User", 100.0)

@pytest.fixture
def target_account():
    return bank_account.BankAccount("Target User", 50.0)

@pytest.mark.parametrize("initial_balance", [50.0, 100.0])
def test_initial_balance(initial_balance):
    account = bank_account.BankAccount("Test User", initial_balance)
    assert account.get_balance() == initial_balance

@pytest.mark.parametrize("deposit_amount", [10.0, 50.0, 100.0])
def test_deposit(account, deposit_amount):
    previous_balance = account.get_balance()
    account.deposit(deposit_amount)
    assert account.get_balance() == previous_balance + deposit_amount
    
def test_transfer_to_non_accuntclass(account, target_account):
    account.transfer(30.0, target_account)
    assert account.get_balance() == 70.0
    assert target_account.get_balance() == 80.0

    with pytest.raises(ValueError):
        account.transfer(200.0, target_account)

    with pytest.raises(TypeError):
        account.transfer(10.0, "NotAnAccount")

def test_predidicted_error(account):
    with pytest.raises(ValueError):
        account.withdraw(-20.0)

def test_transfer_to_self(account):
    with pytest.raises(ValueError):
        account.transfer(-10.0, account)

def test_deposit_type_error(account):
    with pytest.raises(TypeError):
        account.deposit("fifty")

def test_negative_transfer_amount(account, target_account):
    with pytest.raises(ValueError):
        account.transfer(-30.0, target_account)