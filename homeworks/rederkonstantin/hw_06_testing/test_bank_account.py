import pytest
from bank_account import BankAccount


@pytest.fixture                         # fixture teszteléshez, mindig a beállított példány fog a teszteken lefutni, módosítások nélkül
def empty_account():
    """
    Test Account with 0 usd ballance.
    """
    return BankAccount("TestTom_01")

@pytest.fixture
def hundred_usd_account():
    """
    Test Account with 0 usd ballance.
    """
    return BankAccount("TestTom_02", 100)

def test_increase_balance(empty_account):
    """
    Test function to test deposit function in BancAccount Class.
    If deposits 100 to empty balance result must be 100.
    """
    empty_account.deposit(100.0)
    assert empty_account.balance == 100.0

def test_withdraw_from_balance(empty_account):
    """
    Test withdraw function in BankAccount Class.
    Increase ballance with 100.
    Withdraw ballance with 50.
    Result must to be 50.
    Withdraw ballance with more 50.
    Result must be 0.
    """
    empty_account.deposit(100.0)
    empty_account.withdraw(50.0)
    assert empty_account.balance == 50.0
    empty_account.withdraw(50.0)
    assert empty_account.balance == 0.0

def test_withdraw_from_balance_not_empty_BancAccount(hundred_usd_account):
    """
    Test deposit and withdraw function on instance of BancAccount with 100 start ballance.
    Start ballance 100.
    We would like to see 150 after deposit 50.
    We would like to see 0 after withdraw 150.
    """
    hundred_usd_account.deposit(50.0)
    assert hundred_usd_account.balance == 150.0
    hundred_usd_account.withdraw(150.0)
    assert hundred_usd_account.balance == 0


# @pytest.mark.parametrize using test of zero float, negative float, negative integer.
@pytest.mark.parametrize("amount, expected_exception",
                         [
                             (0.0, ValueError),         # nulla float
                             (-0.1, ValueError),        # negatív float
                             (int(-1), ValueError)      # negatív integer
                         ])

def test_deposit_with_non_correct_value(empty_account, 
                                        amount, 
                                        expected_exception):
    """
    Test exeptions by different non accepted imputs.
    """
    with pytest.raises(expected_exception):
        empty_account.deposit(amount)

def test_send_money_to_other_account(hundred_usd_account, 
                                     empty_account):
    """
    Send 80 to other account and result must to be 80 on 
    ballance of other account.
    """
    hundred_usd_account.transfer(80, empty_account)
    assert empty_account.balance == 80

# Test for non BancAccount instance imput for transfer.
@pytest.mark.parametrize("target_account, expected_exception",
                         [
                             ("Test_John", TypeError),                                     # String imput
                             (12341234123412341234123412341234, TypeError),                 # Account number int
                         ])

def test_transfer_to_not_bancaccount(empty_account, 
                                     target_account, 
                                     expected_exception):
    """
    Test exeptions by different non accepted imputs.
    """
    with pytest.raises(expected_exception):
        empty_account.transfer(100.0,target_account)



# Test for non number inputs durint creation of BankAccount Class.
@pytest.mark.parametrize("initial_balance, expected_exception",
                         [
                             ("1000", TypeError),                                   # String imput
                             (True, TypeError),                                     # Bolean imput
                             ([1, "True", 3.5], TypeError),                         # List
                             ({1:"one",2:"two", 3:3}, TypeError)                               # dict
                         ])

def test_create_bankacount_bud_type_of_ballance_input(initial_balance, 
                                                      expected_exception):
    """
    Test create BankAccount Class wiht non number of imput.
    """
    with pytest.raises(expected_exception):
        BankAccount("Test_Tom", initial_balance)

def test_send_money_to_myself(empty_account):
    """
    Test send money to myself.
    """
    with pytest.raises(ValueError, 
                       match="Money sending to " \
                       "yourself is increase margin of Bank. " \
                       "They have enought."):
        empty_account.transfer(100, empty_account)
