from fastapi import APIRouter, status

from src.llm.schemas import RequestLLM, LLMResponse
from src.llm.prompts import Prompts
from src.llm.client import gemini_client

llm_router = APIRouter(prefix="/llm")


@llm_router.post("/completions", status_code=status.HTTP_201_CREATED)
async def completions(data: RequestLLM) -> LLMResponse:
    """This route handle llm requests"""
    return gemini_client.request_llm(data=data, prompt=Prompts.CLEAN_REQUEST)
