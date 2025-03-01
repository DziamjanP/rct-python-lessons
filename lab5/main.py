from fastapi import FastAPI, Query

from db import DBHandler

app = FastAPI()

@app.get('/')
def index():
    return {"hey":"test"}

@app.get('/tasks')
def get_tasks(id: int = Query(None), completed: bool = Query(None), limit: int = Query(None)):
    #get task(s) and filter them
    db = DBHandler()
    tasks = db.get_tasks(id = id, completed = completed, limit = limit)
    return {'tasks':tasks}

@app.put('/tasks')
def add_task():
    #add new task
    return {'code':0}

@app.post('/tasks')
def update_task():
    #update task
    return {'code':0}

@app.delete('/tasks')
def delete_task():
    return {'code':0}
