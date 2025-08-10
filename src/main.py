from fastapi import FastAPI
from src.llm.router import llm_router

app = FastAPI()
app.include_router(llm_router)