from pydantic import BaseModel, Field


class QuestionIn(BaseModel):
    question: str = Field(min_length=2, max_length=2000)

class AnswerOut(BaseModel):
    answer: str
    sources: list = Field(default_factory=list)