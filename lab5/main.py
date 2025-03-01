from fastapi import FastAPI, Query

from db import DBHandler
from task import Task, TaskModel

app = FastAPI()

db = DBHandler()

@app.get('/')
def index():
    return {"hey":"test"}

@app.get('/tasks')
def get_tasks(id: int = Query(None), completed: bool = Query(None), limit: int = Query(None)):
    #get task(s) and filter them
    tasks = db.get_tasks(id = id, completed = completed, limit = limit)
    return {'tasks':tasks}

@app.post('/tasks')
def add_task(task: TaskModel):
    db.add_task(Task(title=task.title, completed = task.completed, description = task.description, deadline = task.deadline))
    return {'code':0}

@app.put('/tasks')
def update_task():
    #update task
    return {'code':0}

@app.delete('/tasks')
def delete_task():
    return {'code':0}
