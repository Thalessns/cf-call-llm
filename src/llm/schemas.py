from dataclasses import dataclass
from typing import List, Field
from os import environ


@dataclass
class Message:
    role: str 
    content: str


@dataclass
class LLMData:
    model: str = Field(default="deepseek-chat")
    messages: List[Message]


@dataclass
class Headers:
    Authorization: str = Field(default=f"Bearer {environ.get('LLM_API_KEY')}")
    Content-Type: str = Field(default="application/json")
