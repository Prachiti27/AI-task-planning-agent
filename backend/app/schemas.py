from pydantic import BaseModel
from typing import List

class TaskInput(BaseModel):
    goal: str
    days: int
    
class PlannedTask(BaseModel):
    task: str
    estimated_days: int
    priority: str


class PlanResponse(BaseModel):
    goal: str
    days: int
    plan: List[PlannedTask]
    markdown: str