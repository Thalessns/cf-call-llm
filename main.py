import sys
from pathlib import Path

from src.llm.client import make_llm_request 
from src.llm.schemas import LLMData, Message, Headers

# Definindo python path
sys.path.apped(str(Path(__file__).parent.parent))


message = Message(
    role = "user",
    content = "Muito bom dia senhor deeepseek"
)


make_llm_request(
    data=LLMData(messages=[message], headers=Headers())
)