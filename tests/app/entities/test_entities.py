import pytest
from src.app.entities.transaction import Transaction, TransactionType
from src.app.entities.account import BankAccount
from src.app.entities.bankNotesParser import NotesToMoney
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

def test_note_parser():
    notes = {
        "2": 1,
        "5": 2,
        "10": 3,
        "20": 4,
        "50": 5 ,
        "100": 6,
        "200": 7
    }
    assert NotesToMoney(notes) == 2372
