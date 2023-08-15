import pytest
from src.app.entities.transaction import Transaction, TransactionType
from src.app.entities.account import BankAccount
from fastapi.exceptions import HTTPException

def test_transaction():
    transactionType = TransactionType.DEPOSIT
    value = 10.0
    currentBalance = 10.0
    t = Transaction(transactionType, value, currentBalance)

    assert t.transactionType == transactionType
    assert t.value == value
    assert t.currentBalance == currentBalance
    assert type(t.toDict()) == dict

def test_account():
    name = "Roberto"
    agency = "1234"
    accountNum = "12345-6"
    startingBalance = 100.0

    account = BankAccount(name,agency,accountNum,startingBalance)

    assert account.name == name
    assert account.agency == agency
    assert account.account == accountNum
    assert account.current_balance == startingBalance

    account.Deposit(10.0)
    assert account.current_balance == 110.0

    account.Withdraw(10)
    assert account.current_balance == 100.0

    with pytest.raises(HTTPException):
        account.Deposit(1000.0)

    with pytest.raises(HTTPException):
        account.Withdraw(1000.0)

