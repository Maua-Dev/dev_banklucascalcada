from .transaction import Transaction, TransactionType
from fastapi.exceptions import HTTPException

class BankAccount:
    def __init__(self,name:str,agency:str,account:str,initial_balance:float = 0):
        self.name = name
        self.agency = agency
        self.account = account
        self.current_balance = initial_balance 
        self.__history = []

    def toDict(self) -> dict:
        return {
            "name": self.name,
            "agency": self.agency,
            "account": self.account,
            "current_balance": self.current_balance
        }

    def addToHistory(self, transaction:Transaction) -> None:
        self.__history.append(transaction.toDict())

    @property
    def history(self) -> dict:
        return {"all_transactions": self.__history}
