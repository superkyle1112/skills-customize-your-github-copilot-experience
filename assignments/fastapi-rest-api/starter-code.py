# Starter code for FastAPI REST API assignment

from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Example resource model
class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

# In-memory database
items_db: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to your FastAPI REST API!"}

# Add your CRUD endpoints below
# ...
