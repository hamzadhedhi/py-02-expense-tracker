from fastapi import FastAPI
import uvicorn
from  dotenv import load_dotenv

load_dotenv()

from .models.transactions import Transaction
from .config.db import engine,create_table

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

def start():
    create_table()
    uvicorn.run('py_02_expense_tracker.main:app', reload=True)