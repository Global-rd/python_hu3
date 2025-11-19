import pytest
from bank_account import BankAccount

# -------------------------------
# Fixtures
# -------------------------------
@pytest.fixture
def account1():
    return BankAccount("Tamás", 900)

@pytest.fixture
def account2():
    return BankAccount("Klára", 300)

# -------------------------------
# __init__ tests
# -------------------------------
@pytest.mark.parametrize(
    "owner, balance, expected_exception",
    [
        ("", 100, TypeError),
        (123, 100, TypeError),
        ("Alice", "100", TypeError),
        ("Alice", None, TypeError),
        ("Alice", -1, ValueError),
    ]
)
def test_init_errors(owner, balance, expected_exception):
    with pytest.raises(expected_exception):
        BankAccount(owner, balance)

@pytest.mark.parametrize(
    "owner, balance",
    [
        ("Alice", 100),
        ("Bob", 0),
        ("Charlie", 50.5),
        ("DefaultUser", None),
    ]
)
def test_init_success(owner, balance):
    account = BankAccount(owner) if balance is None else BankAccount(owner, balance)
    expected_balance = 0.0 if balance is None else balance
    assert account.owner == owner
    assert account.balance == expected_balance

# -------------------------------
# Deposit / Withdraw / Get Balance combined
# -------------------------------
@pytest.mark.parametrize(
    "initial_balance, operations, expected_balance",
    [
        (0, [], 0),
        (100, [], 100),
        (100, [("deposit", 50)], 150),
        (200, [("withdraw", 50)], 150),
        (300, [("deposit", 100), ("withdraw", 50)], 350),
    ]
)
def test_operations_and_get_balance(initial_balance, operations, expected_balance):
    account = BankAccount("TestUser", initial_balance)

    for op, amount in operations:
        if op == "deposit":
            account.deposit(amount)
        elif op == "withdraw":
            account.withdraw(amount)

    assert account.get_balance() == expected_balance

# -------------------------------
# Deposit / Withdraw invalid inputs
# -------------------------------
@pytest.mark.parametrize(
    "method, amount, expected_exception",
    [
        ("deposit", 0, ValueError),
        ("deposit", -5, ValueError),
        ("deposit", "abc", TypeError),
        ("withdraw", 0, ValueError),
        ("withdraw", -10, ValueError),
        ("withdraw", "xyz", TypeError),
        ("withdraw", 1000, ValueError),  # insufficient funds
    ]
)
def test_invalid_inputs(account1, account2, method, amount, expected_exception):
    account = account1 if method in ["deposit", "withdraw"] else None
    if method == "withdraw":
        account = account2 if amount == 1000 else account1

    with pytest.raises(expected_exception):
        getattr(account, method)(amount)

# -------------------------------
# Transfer success / failure
# -------------------------------
@pytest.mark.parametrize(
    "initial_src, initial_dst, transfer_amount, expect_exception",
    [
        (900, 300, 900, None),   # exact balance
        (900, 300, 500, None),   # less than balance
        (900, 300, 1000, ValueError),  # insufficient funds
        (900, 300, -50, ValueError),   # negative
        (900, 300, 0, ValueError),     # zero
        (900, 300, "abc", TypeError),  # invalid type
    ]
)
def test_transfer_operations(initial_src, initial_dst, transfer_amount, expect_exception):
    src = BankAccount("SrcUser", initial_src)
    dst = BankAccount("DstUser", initial_dst)

    if expect_exception:
        with pytest.raises(expect_exception):
            src.transfer(transfer_amount, dst)
    else:
        src.transfer(transfer_amount, dst)
        assert src.balance == initial_src - transfer_amount
        assert dst.balance == initial_dst + transfer_amount

def test_transfer_to_self_raises(account1):
    with pytest.raises(ValueError):
        account1.transfer(50, account1)
