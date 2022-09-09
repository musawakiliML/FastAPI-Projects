from fastapi import APIRouter
from models import Todo

# Define todo route instances
todo_router = APIRouter()

todo_list = []


@todo_router.post("/todo")
async def add_todo(todo: Todo) -> dict:
    todo_list.append(todo)
    return {'message': 'Todo added succesfully'}


@todo_router.get('/todo')
async def retrieve_todos() -> dict:
    return {'todo list': todo_list}
