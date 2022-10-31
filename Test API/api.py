from fastapi import FastAPI
from models import Item

app = FastAPI()

test_database = {
    1: {"task": "read books"},
    2: {"task": "Write blog"},
    3: {"task": "Create a youtube stream"},
}

# get all items


@app.get('/')
async def get_items():
    return test_database

# get a single item


@app.get("/{id}")
async def get_item(id: int):
    if id in test_database.keys():
        return test_database[id]
    else:
        return "Invalid ID"

# post an item option 1


@app.post('/')
async def add_item(item: Item):
    new_id = len(test_database.keys()) + 1
    test_database[new_id] = {"task":item.task}

    return test_database

# update an item using put
@app.put('/{id}')
async def update_item(id: int, item:Item):
    test_database[id]['task'] = item.task
    
    return test_database

# @app.get('/')
# async def index() -> dict:
#    return {"data": "Hello World!!"}
