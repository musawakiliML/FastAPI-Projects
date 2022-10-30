from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def get_items():
    return ['item 1', 'item 2', 'item 3']










#@app.get('/')
#async def index() -> dict:
#    return {"data": "Hello World!!"}
