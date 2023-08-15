from fastapi import FastAPI, HTTPException
from mangum import Mangum

app = FastAPI()

@app.get("/")
def Root():
    pass

@app.post("/deposit")
def Deposit():
    pass

@app.post("/withdraw")
def Withdraw():
    pass

@app.get("/history")
def History():
    pass

handler = Mangum(app, lifespan="off")
