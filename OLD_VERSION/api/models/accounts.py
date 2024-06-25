from pydantic import BaseModel
from typing import Optional

class Account(BaseModel):
    id: int



class AccountShortModel(BaseModel):
    id: int | str
    name: str