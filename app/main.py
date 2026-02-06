from fastapi import FastAPI
from app.api import auth, todos

app = FastAPI(title="Task Manager API")

app.include_router(auth.router)
app.include_router(todos.router)