import pytest
from bank_account import BankAccount


@pytest.fixture
def acc1():
    """Alap account 100 egységgel."""
    return BankAccount("Alice", 100)


@pytest.fixture
def acc2():
    """Másik account 50 egységgel."""
    return BankAccount("Bob", 50)


def test_initial_balance_positive():
    acc = BankAccount("John", 200)
    assert acc.get_balance() == 200


def test_initial_balance_negative_error():
    with pytest.raises(ValueError):
        BankAccount("John", -10)


@pytest.mark.parametrize("amount", [0, -5])
def test_deposit_invalid(amount, acc1):
    with pytest.raises(ValueError):
        acc1.deposit(amount)


def test_deposit_valid(acc1):
    acc1.deposit(50)
    assert acc1.get_balance() == 150


def test_withdraw_valid(acc1):
    acc1.withdraw(40)
    assert acc1.get_balance() == 60


@pytest.mark.parametrize("amount", [0, -10])
def test_withdraw_invalid_amount(amount, acc1):
    with pytest.raises(ValueError):
        acc1.withdraw(amount)


def test_withdraw_insufficient_funds(acc1):
    with pytest.raises(ValueError):
        acc1.withdraw(1000)


def test_transfer_valid(acc1, acc2):
    acc1.transfer(30, acc2)
    assert acc1.get_balance() == 70
    assert acc2.get_balance() == 80


def test_transfer_invalid_target(acc1):
    with pytest.raises(TypeError):
        acc1.transfer(10, "not a bank account")


def test_transfer_insufficient_funds(acc1, acc2):
    with pytest.raises(ValueError):
        acc1.transfer(1000, acc2)


def test_transfer_to_self_not_allowed(acc1):

    with pytest.raises(ValueError):
        acc1.transfer(10, acc1)
