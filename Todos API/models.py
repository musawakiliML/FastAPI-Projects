from pydantic import BaseModel

# Define our Todo API Data Model


class Item(BaseModel):
    item: str
    status: str

    class Config:
        Schema_extra = {
            'Example': {
                'item': "your todo",
                'status': 'completed'
            }
        }


class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        Schema_extra = {
            'Example': {
                'id': 1,
                'item': {
                    'item': "your todo",
                    'status': 'completed'
                }
            }
        }
