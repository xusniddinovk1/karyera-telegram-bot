from abc import ABC, abstractmethod


class AIInterface(ABC):

    @abstractmethod
    async def generate_text(self, prompt: str) -> str:
        pass
