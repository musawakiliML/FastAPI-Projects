from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from schema import Item
import models

from database import Base, SessionLocal, engine

# create database
Base.metadata.create_all(engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()

app = FastAPI()

test_database = {
    1: {"task": "read books"},
    2: {"task": "Write blog"},
    3: {"task": "Create a youtube stream"},
}

# get all items


@app.get('/')
async def get_items(session: Session = Depends(get_session)):
    items = session.query(models.Item).all()
    #return test_database
    return items

# get a single item


@app.get("/{id}")
async def get_item(id: int):
    if id in test_database.keys():
        return test_database[id]
    else:
        return "Invalid ID"

# post an item option 1


@app.post('/')
async def add_item(item: Item, session: Session = Depends(get_session)):
    item = models.Item(task = item.task)
    session.add(item)
    session.commit()
    session.refresh(item)
    
    return item
    #new_id = len(test_database.keys()) + 1
    #test_database[new_id] = {"task":item.task}

    #return test_database

# update an item using put
@app.put('/{id}')
async def update_item(id: int, item:Item):
    test_database[id]['task'] = item.task
    
    return test_database

# delete an item using delete
@app.delete('/{id}')
async def delete_item(id: int):
    test_database.pop(id)
    
    return test_database

# @app.get('/')
# async def index() -> dict:
#    return {"data": "Hello World!!"}
