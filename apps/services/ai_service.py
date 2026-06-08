from anthropic import AsyncAnthropic
from apps.interfaces.ai_interface import AIInterface


class ClaudeService(AIInterface):
    def __init__(self, api_key: str) -> None:
        self.client = AsyncAnthropic(api_key=api_key)

    async def generate_text(self, prompt: str) -> str:
        message = await self.client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
