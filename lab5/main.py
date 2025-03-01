from fastapi import FastAPI, Path, Query

from db import DBHandler
from task import Task, TaskModel, TaskModelUpdate

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

@app.put('/tasks/{task_id}')
def update_task(task: TaskModelUpdate, task_id: int = Path(title = "Task's ID", description="Task will be identified using this id.", gt = 0)):
    db.update_task(task_id, task)
    return {'code':0}

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int = Path(title="Task's ID", description="Task will be identified using this id.", gt = 0)):
    db.delete_task(task_id)
    return {'code':0}
