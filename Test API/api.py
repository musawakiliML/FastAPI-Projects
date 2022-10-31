from fastapi import FastAPI

app = FastAPI()

test_database = {
    1:{"task":"read books"},
    2:{"task":"Write blog"},
    3:{"task":"Create a youtube stream"},
}

# get all items
@app.get('/')
async def get_items():
    return test_database

# get a single item
@app.get("/{id}")
async def get_item(id:int):
    return test_database[id]








#@app.get('/')
#async def index() -> dict:
#    return {"data": "Hello World!!"}
