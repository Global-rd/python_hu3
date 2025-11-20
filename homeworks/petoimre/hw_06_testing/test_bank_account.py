import pytest
from bank_account import BankAccount as ba

# pytest homeworks/petoimre/hw_06_testing/test_bank_account.py


@pytest.fixture
def ba_zero_balance():
    return ba("abc", 0)



# print(type(ba_zero_balance))    # <class '_pytest.fixtures.FixtureFunctionDefinition'>

@pytest.fixture
def ba_positive_balance():
    return ba("def", 1000)


def test_deposit_by_zero_balance(ba_zero_balance):
    ba_zero_balance.deposit(100)

    assert ba_zero_balance.get_balance() == 100
    #assert ba_zero_balance.get_balance() == 101


def test_deposit_by_pos_balance(ba_positive_balance):
    ba_positive_balance.deposit(100)

    assert ba_positive_balance.get_balance() == 1100
    #assert ba_positive_balance.get_balance() == 101


@pytest.mark.parametrize("deposit, expected_exception", 
                         [
                         (-1000, ValueError),
                         (0, ValueError),
                         ("ten", ValueError),
                         ])

def test_deposit_by_invalid_input(ba_positive_balance, deposit, expected_exception):
    with pytest.raises(expected_exception):
        ba_positive_balance.deposit(deposit)
        ba_positive_balance.withdraw(deposit)


@pytest.mark.parametrize("money, ba_obj, expected_exception", 
                         [
                         (-1000, ba("def",1000), ValueError),       
                         (0, ba("def",1000), ValueError),           
                         (100000, ba("def",1000), ValueError),         
                         ("ten", ba("def",1000), ValueError),
                         (100, ba("def",1000), ValueError),
                         ])

def test_transfer_by_invalid_input(ba_positive_balance, money, ba_obj, expected_exception):
    with pytest.raises(expected_exception):
        ba_positive_balance.transfer(money, ba_obj)   
        
        

