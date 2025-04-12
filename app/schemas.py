from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
class TaskBase(BaseModel):
    title: str
    description: str = ""
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int

    class Config:
        orm_mode = True
