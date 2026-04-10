
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import select

from database import Base, async_engine, Task, async_session
from Schemas import TaskSchema

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ['*'],
    allow_methods = ['*']
)


@app.get("/all_tasks")
async def get_all_tasks():
    async with async_session() as session:
        query = select(Task)
        result = await session.execute(query)
        users = result.scalars().all()
        return users


@app.post("/create_new_task")
async def post_task(task: TaskSchema):
    async with async_session() as session:
        new_task = Task(title = task.title)
        session.add(new_task)
        await session.commit()
    

@app.delete("/delete_task/{task_id}")
async def DeleteTask(task_id: int):
    async with async_session() as session:   
        del_task = await session.get(Task, task_id)
        if del_task:
            await session.delete(del_task)
        await session.commit()



if __name__ == "__main__":
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)
#http://127.0.0.1:8000/docs