from pydantic import BaseModel, Field


class TaskSchema(BaseModel):
    title: str = Field(max_length = 20)
