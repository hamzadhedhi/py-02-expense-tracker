from sqlmodel import SQLModel,Field
from datetime import datetime
from typing import List

class Transaction(SQLModel,table=True):
    id: int = Field(default=None, primary_key=True)
    amount: float
    category: str
    created_at: datetime = Field(default_factory=lambda: datetime.now())
    type: str
    title: str
    desc: str
    # attachments: List[str]
    include_amount: bool