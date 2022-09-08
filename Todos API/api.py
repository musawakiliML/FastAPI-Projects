from fastapi import FastAPI
from todo import todo_router

app = FastAPI()


@app.get('/')
async def index() -> dict:
    return {"message": "Welcome to my Todo API"}

app.include_router(todo_router)
