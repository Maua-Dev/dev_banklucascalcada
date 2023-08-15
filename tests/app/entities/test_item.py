import pytest
from src.app.entities.transaction import Transaction, TransactionType


def test_transaction():
    transactionType = TransactionType.DEPOSIT
    value = 10.0
    currentBalance = 10.0
    t = Transaction(transactionType, value, currentBalance)

    assert t.transactionType == transactionType
    assert t.value == value
    assert t.currentBalance == currentBalance
    assert type(t.toDict()) == dict
