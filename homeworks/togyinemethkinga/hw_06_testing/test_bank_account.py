import pytest
from bank_account import BankAccount

@pytest.fixture
def zero_balance():
    # 0 összegű teszt számla
    return BankAccount("X", 0.0)

@pytest.fixture
def test_account():
    # nem 0 összegű teszt számla
    return BankAccount("Y", 1000.0)

@pytest.mark.parametrize("amount, expected_exception",
                         [
                             (-100.0, ValueError), # negativ összeg
                             ( 0.0, ValueError), # zero összeg
                             ( 100.0, ValueError) #túl nagy összeg
                         ])


def test_withdraw_invalid_number(zero_balance, amount, expected_exception):
    # ellenőrizzük a negativ, 0 és túl magas összegre a pénzkivételt
     with pytest.raises(expected_exception):
        zero_balance.withdraw(amount)

def test_withdraw(test_account):
    # teszteljük, hogy kikerül-e a pénz a számláról
    test_account.withdraw(1000.0)
    assert test_account.balance == 0.0

@pytest.mark.parametrize("amount, expected_exception",
                         [
                             (-100.0, ValueError), # negativ összeg
                             ( 0.0, ValueError) # zero összeg
                         ])


def test_deposit_invalid_number(zero_balance, amount, expected_exception):
    # negativ vagy 0 értéket akarunk berakni
     with pytest.raises(expected_exception):
        zero_balance.deposit(amount)


def test_deposit(zero_balance):
    # teszteljük, hogy berakja-e a pénzt a számlára
    zero_balance.deposit(100.0)
    assert zero_balance.balance == 100.0


@pytest.mark.parametrize("amount, target_account, expected_exception",
                         [
                             (-100.0, test_account, TypeError), # negativ összeg
                             ( 0.0, test_account, TypeError), # zero összeg
                             (100.0, test_account, TypeError) # túl magas összeg
                         ])

def test_transfer_invalid_number(zero_balance, amount, target_account, expected_exception):
    # negativ, 0 vagy túl magas értéket akarunk utalni
    with pytest.raises(expected_exception):
        zero_balance.transfer(amount, target_account)


def test_transfer_invalid_type(test_account):
    # nem megfelelő tipus kiszűrése
    invalid_account = ["a","b"]
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        test_account.transfer(100.0, invalid_account)


