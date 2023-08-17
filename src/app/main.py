from .entities.account import BankAccount
from .entities.bankNotesParser import NotesToMoney
from fastapi import FastAPI, HTTPException
from mangum import Mangum

bankAccount = BankAccount("Lucas","1234","12345-6",100.0)

app = FastAPI()

@app.get("/")
def Root():
    return bankAccount.toDict()

@app.post("/deposit")
def Deposit(notes:dict):
    ammount = NotesToMoney(notes)
    res = bankAccount.Deposit(ammount)
    return res

@app.post("/withdraw")
def Withdraw(notes:dict):
    ammount = NotesToMoney(notes)
    res = bankAccount.Withdraw(ammount)
    return res
    
@app.get("/history")
def History():
    return bankAccount.history

handler = Mangum(app, lifespan="off")
