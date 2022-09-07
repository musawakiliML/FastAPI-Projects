from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def index() -> dict:
    return {"data": "Hello World!!"}
