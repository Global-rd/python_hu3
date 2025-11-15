import pytest
from bank_account import BankAccount 

# 2 Fixture
@pytest.fixture
def test_account_john_snow():
    #1Fixture: Üres bankszámla.
    return BankAccount("John Snow", 0.0)

@pytest.fixture
def test_account_ellie_summer():
    #2Fixture: Feltöltött bankszámla.
    return BankAccount("Ellie Summer", 1000.0)

# @pytest.mark.parametrize teszt
@pytest.mark.parametrize("invalid_amount", [0, -10, -0.001])
def test_deposit_invalid_amount_raises_value_error(test_account_john_snow, invalid_amount):
    #Teszteli a deposit() metódust 0 és negatív inputokkal.
    initial_balance = test_account_john_snow.balance
    with pytest.raises(ValueError, match="Deposit amount must be positive."):
        test_account_john_snow.deposit(invalid_amount)
        
    # Ellenőrzés: az egyenleg nem változott
    assert test_account_john_snow.balance == initial_balance

# --- Edge Case Tesztek ---
# 1. Edge Case: Pénz küldése nem BankAccount objektumra.
def test_transfer_non_acc_type_error(test_account_ellie_summer):
    non_bank_account_object = ["a", "list"] 
    with pytest.raises(TypeError, match="Target must be a BankAccount instance."):
        test_account_ellie_summer.transfer(10.0, non_bank_account_object)

# 2. Edge Case: Pontosan a teljes egyenleg kivétele (sikeres kell legyen).
def test_withdraw_full_balance_successful(test_account_ellie_summer):
    # A kivételi összeget egy változóba tesszük
    withdraw_amount = 1000.0
    test_account_ellie_summer.withdraw(withdraw_amount)
    assert test_account_ellie_summer.balance == 0.0

# Exception Tesztek
def test_exception_init_negative_balance_raises_value_error():
    # 1. Exception Teszt: Negatív kezdő egyenleg esetén ValueError dobódik-e.
    with pytest.raises(ValueError, match="Initial balance cannot be negative."):
        BankAccount("Hibás", -1.0)

def test_exception_withdraw_insufficient_funds_raises_value_error(test_account_ellie_summer):
    # 2. Exception Teszt: Elégtelen fedezet esetén ValueError dobódik-e.
    with pytest.raises(ValueError, match="Insufficient funds."):
        # Próbálunk kivenni 1000.01-et, amikor csak 1000.0 van
        test_account_ellie_summer.withdraw(1000.01)