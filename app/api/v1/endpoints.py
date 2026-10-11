from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()


class Task(BaseModel):
    name: str
    description: str
    id: int


tasks: list[Task] = []


@router.get("/tasks/", status_code=status.HTTP_200_OK)
async def all_task() -> list[Task]:
    """Return all the tasks"""
    # tasks = [{ "id": 1, "name": "playing cricket"}, {"id": 2, "name": "Shopping dress"}]
    return tasks


@router.post("/tasks", status_code=status.HTTP_201_CREATED)
async def create_task(task: Task) -> list[Task]:
    """create the task"""

    tasks.append(task)
    return tasks


@router.get("/tasks/{task_id}", status_code=status.HTTP_200_OK)
async def get_task(task_id: int) -> list[Task]:
    """get task by id"""
    res = [task for task in tasks if task.id == task_id]
    if len(res) == 0:
        raise HTTPException(status_code=404, detail="Item not found")
    return res
