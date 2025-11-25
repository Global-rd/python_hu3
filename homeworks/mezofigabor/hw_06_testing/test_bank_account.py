import pytest
from bank_account import BankAccount


# Fixtures
@pytest.fixture
def account_with_balance():
    """Fixture egy 1000 Ft egyenlegű számlához"""
    return BankAccount("Teszt Elek", 1000.0)


@pytest.fixture
def empty_account():
    """Fixture egy üres (0 Ft egyenlegű) számlához"""
    return BankAccount("Teszt Elekné", 0.0)


@pytest.fixture
def rich_account():
    """Fixture egy nagy egyenlegű számlához"""
    return BankAccount("Kis Teszt Elek", 50000.0)


class TestBankAccountInit:
    """Tesztek a BankAccount inicializálásához"""
    
    def test_init_with_valid_balance(self, account_with_balance):
        assert account_with_balance.owner == "Teszt Elek"
        assert account_with_balance.balance == 1000.0
    
    def test_init_with_zero_balance(self, empty_account):
        assert empty_account.owner == "Teszt Elekné"
        assert empty_account.balance == 0.0
    
    def test_init_with_negative_balance_raises_valueerror(self):
        """Teszt: negatív kezdőegyenleg ValueError-t dob"""
        with pytest.raises(ValueError, match="Initial balance cannot be negative"):
            BankAccount("Invalid User", -100.0)
    
    @pytest.mark.parametrize("balance", [-1, -0.01, -1000, -999999.99])
    def test_init_with_various_negative_balances_raises_valueerror(self, balance):
        """Teszt: különböző negatív értékek ValueError-t dobnak"""
        with pytest.raises(ValueError, match="Initial balance cannot be negative"):
            BankAccount("Test User", balance)


class TestDeposit:
    """Tesztek a befizetési művelethez"""
    
    def test_deposit_positive_amount(self, account_with_balance):
        account_with_balance.deposit(500.0)
        assert account_with_balance.balance == 1500.0
    
    def test_deposit_to_empty_account(self, empty_account):
        empty_account.deposit(100.0)
        assert empty_account.balance == 100.0
    
    @pytest.mark.parametrize("amount", [0, -1, -0.01, -100, -999.99])
    def test_deposit_invalid_amounts_raise_valueerror(self, account_with_balance, amount):
        """Teszt: 0 és negatív összegek ValueError-t dobnak"""
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            account_with_balance.deposit(amount)


class TestWithdraw:
    """Tesztek a kivételi művelethez"""
    
    def test_withdraw_valid_amount(self, account_with_balance):
        account_with_balance.withdraw(300.0)
        assert account_with_balance.balance == 700.0
    
    def test_withdraw_entire_balance(self, account_with_balance):
        account_with_balance.withdraw(1000.0)
        assert account_with_balance.balance == 0.0
    
    
    def test_withdraw_more_than_balance_raises_valueerror(self, account_with_balance):
        """Teszt: fedezethiány ValueError-t dob"""
        with pytest.raises(ValueError, match="Insufficient funds"):
            account_with_balance.withdraw(1500.0)
    
    @pytest.mark.parametrize("initial,withdraw_amount", [
        (100, 150),
        (0, 0.01),
        (50, 50.01),
        (1000, 1000.01)
    ])
    def test_withdraw_exceeding_balance_raises_valueerror(self, initial, withdraw_amount):
        """Teszt: egyenleget meghaladó kivét ValueError-t dob"""
        account = BankAccount("Test", initial)
        with pytest.raises(ValueError, match="Insufficient funds"):
            account.withdraw(withdraw_amount)


class TestTransfer:
    """Tesztek az átutalási művelethez"""
    
    def test_transfer_valid_amount_between_accounts(self, account_with_balance, empty_account):
        account_with_balance.transfer(400.0, empty_account)
        assert account_with_balance.balance == 600.0
        assert empty_account.balance == 400.0
    
    def test_transfer_entire_balance(self, account_with_balance, empty_account):
        account_with_balance.transfer(1000.0, empty_account)
        assert account_with_balance.balance == 0.0
        assert empty_account.balance == 1000.0
    
    def test_transfer_insufficient_funds_raises_valueerror(self, account_with_balance, empty_account):
        """Teszt: fedezethiány esetén ValueError"""
        with pytest.raises(ValueError, match="Insufficient funds"):
            account_with_balance.transfer(1500.0, empty_account)
        # Egyenlegek nem változtak
        assert account_with_balance.balance == 1000.0
        assert empty_account.balance == 0.0
    
    @pytest.mark.parametrize("amount", [0, -1, -100, -0.01])
    def test_transfer_invalid_amounts_raise_valueerror(self, account_with_balance, empty_account, amount):
        """Teszt: érvénytelen összegek átutalása ValueError-t dob"""
        with pytest.raises(ValueError, match="Withdraw amount must be positive"):
            account_with_balance.transfer(amount, empty_account)


class TestGetBalance:
    """Tesztek az egyenleg lekérdezéséhez"""
    
    def test_get_balance_returns_current_balance(self, account_with_balance):
        assert account_with_balance.get_balance() == 1000.0
    
    def test_get_balance_after_deposit(self, empty_account):
        empty_account.deposit(500.0)
        assert empty_account.get_balance() == 500.0
    
    def test_get_balance_after_withdraw(self, rich_account):
        rich_account.withdraw(10000.0)
        assert rich_account.get_balance() == 40000.0
