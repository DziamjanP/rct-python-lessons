from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task import Task, TaskModel

class DBHandler:
    def __init__(self):
        database_url = "postgresql://postgres:postgres@localhost/rct_todo"
        engine = create_engine(database_url)
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
        return tasks

    def add_task(self, task):
        db = self.SessionLocal()
        db.add(task)
        db.commit()
        db.close()
