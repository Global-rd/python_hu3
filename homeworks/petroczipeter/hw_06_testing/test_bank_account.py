import pytest
from bank_account import BankAccount

# FIXTUREK – 2 különböző számla objektum

@pytest.fixture
def empty_account():
    """0 Ft-tal induló teszt számla."""
    return BankAccount(owner="Peter", balance=0.0)

@pytest.fixture
def rich_account():
    """1000 Ft-tal induló teszt számla."""
    return BankAccount(owner="Anna", balance=1000.0)

# PARAMETRIZÁLT TESZT: deposit edge case-ek
# (0 és negatív érték)

@pytest.mark.parametrize(
    "amount",
    [0, -10, -0.01]
)
def test_deposit_invalid_values(empty_account, amount):
    with pytest.raises(ValueError):
        empty_account.deposit(amount)

# Sikeres deposit

def test_deposit_valid(empty_account):
    empty_account.deposit(500)
    assert empty_account.get_balance() == 500

# Sikeres withdraw

def test_withdraw_valid(rich_account):
    rich_account.withdraw(200)
    assert rich_account.get_balance() == 800

# Withdraw – túl nagy összeg (Exception)

def test_withdraw_insufficient_funds(empty_account):
    with pytest.raises(ValueError):
        empty_account.withdraw(1)

# Withdraw – negatív összeg (Exception)

def test_withdraw_negative_amount(rich_account):
    with pytest.raises(ValueError):
        rich_account.withdraw(-100)

# Átutalás – sikeres

def test_transfer_success(rich_account, empty_account):
    rich_account.transfer(300, empty_account)
    assert rich_account.get_balance() == 700
    assert empty_account.get_balance() == 300

# EDGE CASE: nem BankAccount-nak küld pénzt

def test_transfer_to_non_account(rich_account):
    with pytest.raises(TypeError):
        rich_account.transfer(100, "nem_jo_tipus")

# Transfer – insufficient funds

def test_transfer_insufficient_funds(empty_account, rich_account):
    with pytest.raises(ValueError):
        empty_account.transfer(100, rich_account)