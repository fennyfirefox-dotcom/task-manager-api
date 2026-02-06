from sqlalchemy.orm import Session
from app.models.todo import Todo
from app.schemas.todo import TodoCreate, TodoUpdate


def get_todos_by_user(db: Session, user_id: int):
    return db.query(Todo).filter(Todo.user_id == user_id).all()


def get_todo(db: Session, todo_id: int, user_id: int) -> Todo | None:
    return db.query(Todo).filter(
        Todo.id == todo_id,
        Todo.user_id == user_id
    ).first()


def create_todo(
    db: Session,
    todo: TodoCreate,
    user_id: int
) -> Todo:
    new_todo = Todo(
        **todo.model_dump(),
        user_id=user_id
    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo


def update_todo(
    db: Session,
    todo: Todo,
    data: TodoUpdate
) -> Todo:
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(todo, field, value)

    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo: Todo):
    db.delete(todo)
    db.commit()
