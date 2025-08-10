"""Schemas to handle LLM calls and responses."""

from dataclasses import dataclass
from typing import List


@dataclass
class RequestLLM:
    """Data for make a request to Gemini."""

    model: str
    contents: str | List[str]


@dataclass
class LLMResponse:
    """Data retrieved by the LLM."""

    content: List[str]
