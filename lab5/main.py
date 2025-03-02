from fastapi import BackgroundTasks, FastAPI, Path, Query

from db import DBHandler
from task import Task, TaskModel, TaskModelUpdate

app = FastAPI()

db = DBHandler()

def send_notification(message):
    print("Sent notification", message, "to some email.")

@app.get('/')
def index():
    return {"hey":"test"}

@app.get('/tasks')
def get_tasks(
    id: int = Query(None, title="Task's ID", description="Get only the task matching this id. Omit to return all.", gt=0),
    completed: bool = Query(None, title="Completed field", description="Will return only completed or incompleted tasks. Omit to return both."),
    limit: int = Query(None, title="Limit by", description="Limits amount of returned tasks by specified amount. Omit to return all matching tasks.", gt=0)):
    tasks = db.get_tasks(id = id, completed = completed, limit = limit)
    return {'tasks':tasks}

@app.post('/tasks')
def add_task(task: TaskModel, background_tasks: BackgroundTasks):
    db.add_task(Task(title=task.title, completed = task.completed, description = task.description, deadline = task.deadline))
    background_tasks.add_task(send_notification, f"You have a new task {task.title} due at {task.deadline}")
    return {'code':0}

@app.put('/tasks/{task_id}')
def update_task(task: TaskModelUpdate, task_id: int = Path(title = "Task's ID", description="Task will be identified using this id.", gt = 0)):
    db.update_task(task_id, task)
    return {'code':0}

@app.delete('/tasks/{task_id}')
def delete_task(task_id: int = Path(title="Task's ID", description="Task will be identified using this id.", gt = 0)):
    db.delete_task(task_id)
    return {'code':0}
