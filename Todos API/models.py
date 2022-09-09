from pydantic import BaseModel

# Define our Todo API Data Model


class Item(BaseModel):
    item: str
    status: str

    class Config:
        schema_extra = {
            'example': {
                'item': "your todo",
                'status': 'completed'
            }
        }


class Todo(BaseModel):
    id: int
    item: Item

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'item': {
                    'item': "your todo",
                    'status': 'completed'
                }
            }
        }


class TodoItem(BaseModel):
    item: str

    class Config:
        schema_extra = {
            "example": {
                'item': "Read the next chapter of the book"
            }
        }
