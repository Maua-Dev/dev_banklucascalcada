from enum import Enum
from time import time

class TransactionType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"

class Transaction:
    def __init__(self, transactionType:TransactionType, value:float, currentBalance:float) -> None:
        assert value > 0, "Value must be higher than zero"
        self.__type = transactionType
        self.__value = value
        self.__currentBalance = currentBalance
        self.__timestamp = time()

    def toDict(self) -> dict:
        return {
            "type": self.__type.value,
            "value": self.__value,
            "current_balance": self.__currentBalance,
            "timestamp": self.__timestamp
        }

    @property 
    def transactionType(self) -> TransactionType:
        return self.__type

    @property
    def value(self) -> float:
        return self.__value

    @property
    def currentBalance(self) -> float:
        return self.__currentBalance
    
    @property
    def timestamp(self) -> float:
        return self.__timestamp

if __name__ == "__main__":
    a = Transaction(TransactionType.DEPOSIT, 10.0, 10.0)
