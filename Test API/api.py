from fastapi import FastAPI

app = FastAPI()

test_database = {
    1:{"task":"read books"},
    2:{"task":"Write blog"},
    3:{"task":"Create a youtube stream"},
}

@app.get('/')
async def get_items():
    return test_database










#@app.get('/')
#async def index() -> dict:
#    return {"data": "Hello World!!"}
