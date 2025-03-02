from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task import Task, TaskModel, TaskModelUpdate

class DBHandler:
    def __init__(self):
        database_url = "postgresql://postgres:postgres@localhost/rct_todo"
        engine = create_engine(database_url, pool_size=20, max_overflow=40)
        # Create a session factory using the engine
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    def get_tasks(self, id = None, completed = None, limit = None):
        db = self.SessionLocal()
        res = db.query(Task)
        if (id != None):
            res = res.filter(Task.id == id)
        if (completed != None):
            res = res.filter(Task.completed == completed)
        if (limit != None):
            res = res.limit(limit)
        db.close()
        tasks = []
        for task in res:
            tasks.append(TaskModel.model_validate(task))
        if len(tasks) == 0:
            raise HTTPException(status_code=404, detail=f"No tasks matching the query found")
        return tasks

    def add_task(self, task):
        db = self.SessionLocal()
        db.add(task)
        db.commit()
        task_id = task.id
        db.close()
        return task_id

    def update_task(self, task_id, info: TaskModelUpdate):
        db = self.SessionLocal()
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if (db_task == None):
            raise HTTPException(status_code=404, detail=f"Task with id {task_id} doesn't exist")
        if (info.title != None):
            db_task.title = info.title
        if (info.description != None):
            db_task.description = info.description
        if (info.completed != None):
            db_task.completed = info.completed
        if (info.deadline != None):
            db_task.deadline = info.deadline
        db.commit()
        db.close()
    
    def delete_task(self, task_id):
        db = self.SessionLocal()
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if (db_task == None):
            raise HTTPException(status_code=404, detail=f"Task with id {task_id} doesn't exist")
        db.delete(db_task)
        db.commit()
        db.close()
