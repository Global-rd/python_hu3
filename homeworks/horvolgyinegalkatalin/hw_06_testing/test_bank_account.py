
import pytest
from bank_account import BankAccount

"""
Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a
tesztjeidben használsz.
"""
@pytest.fixture
def object1():
    return BankAccount("Alibaba",20000.0)

@pytest.fixture
def object2():
    return BankAccount("Alibaba2",0.0)


"""
Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak
érdekében, hogy a tesztet több input-ra is lefuttassa (pl: teszteld a
deposit() method-ot pontosan 0 és negatív szám inputtal is).
"""

@pytest.mark.parametrize("test_amount,expected_exception",
                         [
                             (-1, ValueError), #negative amount
                             (0, ValueError), #zero quantity
                             ("Vadalmafa88",TypeError) #non number
#vizsgálnám a tizedesek számát, de nem tudom hogy kell, csak érvényes fillér érték lehessen pénznemtől függően
                         ])
 
def test_deposit_invalid_imput(object1,test_amount,expected_exception):
    with pytest.raises(expected_exception):   
         object1.deposit(test_amount)
       


"""● Tesztelj edge case-eket (pl: pénz küldése nem BankAccount
object-nek)."""

@pytest.mark.parametrize("invalid_target,expected_exception",
                         [
                             (-1, TypeError), #non BankAcccount type
                             ("Vadalmafa88",TypeError) #non BankAcccount type
                         ])
def test_transfer_invalid_bank_acccount_type(object1,invalid_target,expected_exception):
    with pytest.raises(expected_exception,match="Target must be a BankAccount instance."):
        object1.transfer(26.555,invalid_target)

"""
● Írj teszteket amik arra irányulnak, hogy a megfelelő Exception
raise-elődik- e a megadott input-ra.
"""

@pytest.mark.parametrize("test_amount, expected_exception",
                         [
                             (-1, ValueError), #negative amount
                             (0, ValueError), #zero quantity
                             ("Vadalmafa88",TypeError), #non number
                             (25000, ValueError), #negative self.balance
                         ])
def test_withdraw_invalid_invalid_amount(object2, test_amount, expected_exception):
    with pytest.raises(expected_exception):
        object2.withdraw(test_amount)

