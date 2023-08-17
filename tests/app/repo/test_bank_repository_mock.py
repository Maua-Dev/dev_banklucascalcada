import pytest
from src.app.entities.bankNotesParser import NotesToMoney
from src.app.entities.account import BankAccount
from src.app.repo.bank_repository_mock import IBankMock
from fastapi.exceptions import HTTPException
#from src.app.entities.item import Item
#from src.app.enums.item_type_enum import ItemTypeEnum
#from src.app.repo.item_repository_mock import ItemRepositoryMock
#
def test_repo():
    name = "Lucas"
    agency = "1234"
    account = "12345-6"
    accountExpected = BankAccount(name,agency,account,100.0)

    repo = IBankMock()
    repo.create_account(name,agency,account,100.0)

    assert accountExpected.toDict() == repo.get_account(agency,account).toDict()

    repo.deposit(agency,account, 10.0)
    assert repo.get_account(agency,account).current_balance == 110.0

    repo.withdraw(agency,account, 10.0)
    assert repo.get_account(agency,account).current_balance == 100.0

    with pytest.raises(HTTPException):
        repo.deposit(agency,account, 1000.0)

    with pytest.raises(HTTPException):
        repo.withdraw(agency,account, 1000.0)

