import requests
from src.llm.schemas import LLMData, Header
from src.llm.config import Envs


def make_llm_request(data: LLMData, headers: Header) -> None:

    response = requests.post(
        json=data.dump(),
        header={"Authorization": Header}
    )
    print(response)
