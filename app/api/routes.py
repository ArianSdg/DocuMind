import json

from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from langchain_core.output_parsers import StrOutputParser

from app.api.schemas import AnswerOut, QuestionIn
from app.llm.factory import get_llm
from app.prompts import SIMPLE_PROMPT

health_router = APIRouter()
router = APIRouter(prefix='/v1')


def sse(event: dict) -> str:
    return f"data: {json.dumps(event, ensure_ascii=False)}\n\n"


@health_router.get('/health')
async def health():
    return {"status": "ok", "app_name": "documind"}


@router.post('/simple', response_model=AnswerOut)
async def simple(body: QuestionIn):
    chain = SIMPLE_PROMPT | get_llm() | StrOutputParser()
    answer = await chain.ainvoke(body.model_dump())

    return AnswerOut(answer=answer)

@router.post('/simple/stream')
async def stream_simple(body: QuestionIn):
    chain = SIMPLE_PROMPT | get_llm() | StrOutputParser()

    async def events():
        async for token in chain.astream(body.model_dump()):
            yield sse({"type": "token", "text": token})

        yield sse({"type": "done"})
    return StreamingResponse(events(), media_type="text/event-stream")