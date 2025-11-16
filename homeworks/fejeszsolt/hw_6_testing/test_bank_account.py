import pytest
from bank_account import BankAccount
from bank_account import SelfTransferError

@pytest.fixture
def acc_zsolt():
    return BankAccount ("Zsolt", 10000)

@pytest.fixture
def acc_olga():
    return BankAccount ("Olga", 50000)



@pytest.mark.parametrize("amount", [0,-10000])
def test_deposit_invalid_values(acc_zsolt, amount):
    """teszt 0 vagy negatív befizetésre"""
    with pytest.raises(ValueError):
        acc_zsolt.deposit(amount)

def test_deposit_faultless(acc_zsolt):
    """teszt a jóváírodott e a bafizetés a számlára"""
    acc_zsolt.deposit(1000)
    assert acc_zsolt.get_balance()==11000


def test_lack_of_funds(acc_olga):
     """teszt a számlán lévő összegnél nagyobb összeg kivételére"""
     with pytest.raises(ValueError):
         acc_olga.withdraw(55000)

def test_transfer_non_bankaccount(acc_olga):
     """teszt nem létező számlára való utalásra"""
     invalid_account="ismeretlen bankszámla"
     with pytest.raises(TypeError):
        acc_olga.transfer(100, invalid_account)
    
def test_deposit_right_exception(acc_zsolt):
    """teszt, megfelelő hibát dobe a withdraw, egyenleg nem válltozik"""
    start_balance=acc_zsolt.get_balance()
    with pytest.raises(ValueError) as errorinfo:
        acc_zsolt.withdraw(10001.00)
    assert "Insufficient funds." in str(errorinfo.value)
    assert acc_zsolt.get_balance() == start_balance

def test_self_transfer_error(acc_olga):
    """teszt, megfelelő hibát dobe önutalás esetén, egyenleg nem válltozik"""
    start_balance=acc_olga.get_balance()
    with pytest.raises(SelfTransferError):
        acc_olga.transfer(100000000, acc_olga)
    assert acc_olga.get_balance() == start_balance

def test_init_balance_not_number():
    """teszt számla létrehozása nyitóösszeg nem szám"""
    with pytest.raises(TypeError):
        BankAccount("Petra", "ötvenezer")

def test_deposit_non_number(acc_olga):
    """teszt befizetés nem szám"""
    with pytest.raises(TypeError):
        acc_olga.deposit("ezer")

def test_transfer_amount_non_number(acc_olga,acc_zsolt):
    """teszt átutalás összege nem szám"""
    with pytest.raises(TypeError):
        acc_olga.transfer("ezer", acc_zsolt)

