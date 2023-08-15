from .transaction import Transaction, TransactionType
from fastapi.exceptions import HTTPException

class BankAccount:
    def __init__(self,name:str,agency:str,account:str,current_balance:float = 0):
        self.__name = name
        self.__agency = agency
        self.__account = account
        self.__current_balance = current_balance
        self.__history = []

    def Deposit(self,ammount:float) -> None:
        if (ammount >= self.__current_balance * 2):
            raise HTTPException(status_code=403, detail="Depósito suspeito")

        self.__current_balance += ammount

        transactionObj = Transaction(TransactionType.DEPOSIT, ammount, self.__current_balance)
        self.__history.append(transactionObj.toDict())

    def Withdraw(self,ammount:float) -> None:
        if ammount > self.__current_balance:
            raise HTTPException(status_code=403, detail="Saldo insuficiente para transação")

        self.__current_balance -= ammount

        transactionObj = Transaction(TransactionType.WITHDRAW, ammount, self.__current_balance)
        self.__history.append(transactionObj.toDict())

    @property
    def name(self) -> str:
        return self.__name

    @property
    def agency(self) -> str:
        return self.__agency

    @property
    def account(self) -> str:
        return self.__account

    @property
    def current_balance(self) -> float:
        return self.__current_balance

    @property
    def history(self) -> dict:
        return {"all_transactions": self.__history}


