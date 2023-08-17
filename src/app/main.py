from .entities.account import BankAccount
from .entities.bankNotesParser import NotesToMoney
from .repo.bank_repository_mock import IBankMock 
from fastapi import FastAPI, HTTPException
from mangum import Mangum

repo = IBankMock()
repo.create_account("Lucas","1234","12345-6",100.0)

app = FastAPI()

@app.get("/")
def Root():
    return repo.get_account("1234","12345-6")

@app.post("/deposit")
def Deposit(notes:dict):
    ammount = NotesToMoney(notes)
    res = repo.deposit("1234","12345-6",ammount)
    return res

@app.post("/withdraw")
def Withdraw(notes:dict):
    ammount = NotesToMoney(notes)
    res = repo.withdraw("1234","12345-6",ammount)
    return res
    
@app.get("/history")
def History():
    return repo.get_history("1234","12345-6")

handler = Mangum(app, lifespan="off")
