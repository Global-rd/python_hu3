"""
Írj legalább 2 fixture-t (2 különböző BankAccount object), amiket a
tesztjeidben használsz.
Írj legalább egy tesztet ami @pytest.mark.parametrize-t használ annak
érdekében, hogy a tesztet több input-ra is lefuttassa (pl: teszteld a
deposit() method-ot pontosan 0 és negatív szám inputtal is).
Tesztelj edge case-eket (pl: pénz küldése nem BankAccount
object-nek).
Írj teszteket amik arra irányulnak, hogy a megfelelő Exception
raise-elődik- e a megadott input-ra.

Extra: a BankAccount class nincs felkészülve minden lehetséges hibára
(non-number inputok, küldhetünk e saját magunknak pénzt stb.). Nézd át
alaposan a kódot, azonosítsd ezeket a hiányosságokat és implementáld a
szükséges változtatásokat a saját mappádban lévő file-ban. Ezután írj
teszteket amik ezeknek a kiegészítéseknek a helyességét ellenőrzik.
"""

from typing import Any
import pytest
from bank_account import BankAccount


@pytest.fixture
def account_with_balance() -> BankAccount:
    """Returns a BankAccount instance with an initial balance of 1000."""
    return BankAccount("Test User 1", 1000.0)


@pytest.fixture
def account_with_zero_balance() -> BankAccount:
    """Returns a BankAccount instance with a zero balance."""
    return BankAccount("Test User 2", 0.0)


def test_account_creation(account_with_balance: BankAccount) -> None:
    """Tests if the account is initialized with the correct owner and balance."""
    assert account_with_balance.owner == "Test User 1"
    assert account_with_balance.get_balance() == 1000.0


def test_initial_negative_balance_raises_error() -> None:
    """Tests if creating an account with a negative balance raises a ValueError."""
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Bad User", -100.0)


def test_deposit_positive_amount(account_with_zero_balance: BankAccount) -> None:
    """Tests depositing a positive amount increases the balance."""
    account_with_zero_balance.deposit(500.0)
    assert account_with_zero_balance.get_balance() == 500.0


@pytest.mark.parametrize("invalid_amount", [0, -100.0])
def test_deposit_invalid_amount_raises_error(account_with_balance: BankAccount, invalid_amount: float) -> None:
    """Tests if depositing a zero or negative amount raises a ValueError."""
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        account_with_balance.deposit(invalid_amount)


def test_withdraw_valid_amount(account_with_balance: BankAccount) -> None:
    """Tests withdrawing a valid amount decreases the balance."""
    account_with_balance.withdraw(300.0)
    assert account_with_balance.get_balance() == 700.0


@pytest.mark.parametrize("invalid_amount", [0, -100.0])
def test_withdraw_invalid_amount_raises_error(account_with_balance: BankAccount, invalid_amount: float) -> None:
    """Tests if withdrawing a zero or negative amount raises a ValueError."""
    with pytest.raises(ValueError, match="Withdraw amount must be positive."):
        account_with_balance.withdraw(invalid_amount)


def test_withdraw_insufficient_funds_raises_error(account_with_balance: BankAccount) -> None:
    """Tests if withdrawing an amount greater than the balance raises a ValueError."""
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_with_balance.withdraw(2000.0)


def test_successful_transfer(account_with_balance: BankAccount, account_with_zero_balance: BankAccount) -> None:
    """Tests a successful transfer between two accounts."""
    initial_balance_source = account_with_balance.get_balance()
    initial_balance_target = account_with_zero_balance.get_balance()
    transfer_amount = 500.0

    account_with_balance.transfer(transfer_amount, account_with_zero_balance)

    assert account_with_balance.get_balance() == initial_balance_source - transfer_amount
    assert account_with_zero_balance.get_balance() == initial_balance_target + transfer_amount


def test_transfer_to_invalid_target_raises_error(account_with_balance: BankAccount) -> None:
    """Tests if transferring to an invalid target (not a BankAccount) raises a TypeError."""
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        account_with_balance.transfer(100.0, "not_an_account")


def test_transfer_insufficient_funds_raises_error(account_with_balance: BankAccount, account_with_zero_balance: BankAccount) -> None:
    """Tests if transferring an amount greater than the source balance raises a ValueError."""
    with pytest.raises(ValueError, match="Insufficient funds."):
        account_with_balance.transfer(2000.0, account_with_zero_balance)


def test_get_balance(account_with_balance: BankAccount) -> None:
    """Tests if get_balance() returns the correct balance."""
    assert account_with_balance.get_balance() == 1000.0


def test_str_representation(account_with_balance: BankAccount) -> None:
    """Tests the string representation of the BankAccount object."""
    expected_str = "Account owner: Test User 1, Balance: 1000.00"
    assert str(account_with_balance) == expected_str

# --- Tests for Extra Tasks ---

@pytest.mark.parametrize("invalid_owner", ["", "   ", None, 123])
def test_invalid_owner_raises_error(invalid_owner: Any) -> None:
    """Tests if creating an account with an invalid owner raises an error."""
    with pytest.raises(ValueError, match="Owner must be a non-empty string."):
        BankAccount(invalid_owner, 100.0)

def test_initial_balance_not_a_number_raises_error() -> None:
    """Tests if creating an account with a non-numeric balance raises a TypeError."""
    with pytest.raises(TypeError, match="Initial balance must be a number."):
        BankAccount("Test User", "not a balance")

def test_deposit_not_a_number_raises_error(account_with_balance: BankAccount) -> None:
    """Tests if depositing a non-numeric amount raises a TypeError."""
    with pytest.raises(TypeError, match="Deposit amount must be a number."):
        account_with_balance.deposit("not a number")

def test_withdraw_not_a_number_raises_error(account_with_balance: BankAccount) -> None:
    """Tests if withdrawing a non-numeric amount raises a TypeError."""
    with pytest.raises(TypeError, match="Withdraw amount must be a number."):
        account_with_balance.withdraw("not a number")

def test_transfer_to_self_raises_error(account_with_balance: BankAccount) -> None:
    """Tests if transferring money to the same account raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot transfer money to the same account."):
        account_with_balance.transfer(100.0, account_with_balance)

def test_owner_name_is_stripped() -> None:
    """Tests if whitespace is stripped from the owner's name upon creation."""
    account = BankAccount("  Some Owner  ")
    assert account.owner == "Some Owner"