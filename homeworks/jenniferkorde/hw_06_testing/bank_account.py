class BankAccount:
   from bank_account import BankAccount


@pytest.fixture
def szamla1():
    return BankAccount(0)

@pytest.fixture
def szamla2():
    return BankAccount(100)


def test_deposit(szamla1):
    szamla1.deposit(100)
    assert szamla1.balance == 100
    szamla1.deposit(0)  
    assert szamla1.balance == 100
    with pytest.raises(ValueError):
        szamla1.deposit(-30)


def test_transfer(szamla2, szamla1):
    szamla2.transfer(20, szamla1)
    assert szamla2.balance == 80
    assert szamla1.balance == 20


def test_transfer_wrong_target(szamla2):
    with pytest.raises(Exception):  
        szamla2.transfer(10, "valami")


def test_transfer_to_self(szamla2):
    try:
        szamla2.transfer(10, szamla2)
        assert False  
    except:
        assert True
