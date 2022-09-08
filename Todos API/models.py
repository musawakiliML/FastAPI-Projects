from pydantic import BaseModel

# Define our Todo API Data Model


class Todo(BaseModel):
    id: int
    item: str
