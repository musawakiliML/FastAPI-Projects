from pydantic import BaseModel

# Define our Todo API Data Model
class Item(BaseModel):
    item: str
    status: str

class Todo(BaseModel):
    id: int
    item: Item