"""Module to handle Gemini stuff."""

from google import genai
from google.genai.types import GenerateContentResponse
from dotenv import load_dotenv
from typing import List

from src.llm.schemas import RequestLLM, LLMResponse


class GeminiClient:
    """Class to handle Gemini requests and responses."""

    def __init__(self) -> None:
        """Initializing class."""
        load_dotenv()
        self._client = genai.Client()
    
    def request_llm(self, data: RequestLLM, prompt: str) -> LLMResponse:
        """Make a request to Gemini.

        Args:
            data (RequestLLM): Contains all the necessary data to make a LLM Request.
            prompt (str): Prompt use to guide the LLM.

        Returns:
                LLMResponse: The response content.
        """
        try:
            contents = self._prepare_request_contents(
                data=data, prompt=prompt
            )
            response = self._client.models.generate_content(
                model=data.model, contents=contents
            )
            response_content = self._handle_response(response=response)
        except Exception as exc:
            print(f"Erro: {exc}")
        else:
            return response_content

    def _prepare_request_contents(self, data: RequestLLM, prompt: str) -> str | List[str]:
        """Make a request to Gemini.

        Args:
            data (RequestLLM): Contains all the necessary data to make a LLM Request.
            prompt (str): Prompt use to guide the LLM.

        Returns:
                str | List[str]: The response content.
        """
        if type(data.contents) is list():
            prepared_contents = []
            for content in data.contents:
                prepared_contents.append(prompt.value + content)
            return prepared_contents
        return prompt.value + data.contents

    def _handle_response(self, response: GenerateContentResponse) -> LLMResponse:
        """Catching the response content.
        
            Args:
                response (GenerateContentResponse): Response retrieved by the LLM.

            Returns:
                LLMResponse: The response content.
        """
        content_list = response.candidates[0].content.parts
        parts = []
        for content in content_list:
            parts.append(content.text)
        return LLMResponse(content=parts)


gemini_client = GeminiClient()
