import asyncio
from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict
from apps.bot import create_bot, create_dispatcher
from apps.services.ai_service import ClaudeService

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str
    CLAUDE_API_KEY: str

    class Config:
        model_config = SettingsConfigDict(env_file=".env")


async def main() -> None:
    settings = Settings()
    bot = create_bot(settings.BOT_TOKEN)
    claude_service = ClaudeService(api_key=settings.CLAUDE_API_KEY)
    dp = create_dispatcher(claude_service)
    await dp.start_polling(bot, claude_service=claude_service)


if __name__ == "__main__":
    asyncio.run(main())
