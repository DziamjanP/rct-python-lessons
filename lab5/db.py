from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task import Task

class DBHandler:
    def __init__(self):
        database_url = "postgresql://postgres:postgres@localhost/rct_todo"
        engine = create_engine(database_url)
        # Create a session factory using the engine
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    def get_tasks(self):
        db = self.SessionLocal()
        tasks = db.query(Task).all()
        db.close()
        return tasks

    def add_task(self, task):
        db = self.SessionLocal()
        db.add(task)
        db.commit()
        db.close()
