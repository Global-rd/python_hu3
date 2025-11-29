import pytest
from bank_account import BankAccount

# --- FIXTURE-ek --- #

@pytest.fixture
def account1():
    return BankAccount("Alice", 100.0)

@pytest.fixture
def account2():
    return BankAccount("Bob", 50.0)

# --- NORMÁL TESZTEK --- #

def test_initial_balance(account1):
    assert account1.get_balance() == 100.0

def test_deposit(account1):
    account1.deposit(25.0)
    assert account1.get_balance() == 125.0

def test_withdraw(account1):
    account1.withdraw(30.0)
    assert account1.get_balance() == 70.0

def test_transfer(account1, account2):
    account1.transfer(40.0, account2)
    assert account1.get_balance() == 60.0
    assert account2.get_balance() == 90.0

# --- HIBÁS ESETEK / EXCEPTION TESZTEK --- #

def test_initial_negative_balance():
    with pytest.raises(ValueError):
        BankAccount("NegativeUser", -100)

def test_deposit_zero_or_negative(account1):
    with pytest.raises(ValueError):
        account1.deposit(0)
    with pytest.raises(ValueError):
        account1.deposit(-10)

def test_withdraw_too_much(account2):
    with pytest.raises(ValueError):
        account2.withdraw(100)

def test_transfer_to_non_account(account1):
    with pytest.raises(TypeError):
        account1.transfer(10, "not_an_account")

# --- PARAMETRIZÁLT TESZT --- #

@pytest.mark.parametrize("amount", [0, -1, -100])
def test_invalid_deposits(account1, amount):
    with pytest.raises(ValueError):
        account1.deposit(amount)

# --- EXTRA: saját magunknak utalás letiltása --- #
def test_transfer_to_self(account1):
    with pytest.raises(ValueError):
        account1.transfer(10, account1)

# --- EXTRA: nem szám típusok kezelése --- #
@pytest.mark.parametrize("amount", ["10", None, [], {}])
def test_non_number_inputs(account1, amount):
    with pytest.raises(TypeError):
        account1.deposit(amount)
    with pytest.raises(TypeError):
        account1.withdraw(amount)
