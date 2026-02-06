from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.security import get_current_user
from app.models.user import User
from app.schemas.todo import TodoCreate, TodoUpdate, TodoResponse
from app.crud import todo as crud_todo

router = APIRouter(prefix="/todos", tags=["Todos"])


@router.get("/", response_model=list[TodoResponse])
def get_my_todos(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_todo.get_todos_by_user(db, current_user.id)


@router.post("/", response_model=TodoResponse)
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return crud_todo.create_todo(db, todo, current_user.id)


@router.patch("/{todo_id}", response_model=TodoResponse)
def update_todo(
    todo_id: int,
    data: TodoUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = crud_todo.get_todo(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404)

    return crud_todo.update_todo(db, todo, data)


@router.delete("/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    todo = crud_todo.get_todo(db, todo_id, current_user.id)
    if not todo:
        raise HTTPException(status_code=404)

    crud_todo.delete_todo(db, todo)
    return {"ok": True}
