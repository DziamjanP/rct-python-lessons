from pydantic import BaseModel, Field

from task import TaskModel

class TasksResponse(BaseModel):
    tasks: list[TaskModel]

class TaskActionResponse(BaseModel):
    code: int = Field(title="Reponse code", description="Returns 0 if everything went well.")
    msg: str = Field(title="Response message", description="Additional information regarding request.")

    def make_success():
        return TaskActionResponse(code=0, msg="Success.")
    