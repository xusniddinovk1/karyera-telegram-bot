import asyncio
from dotenv import load_dotenv

from pydantic_settings import BaseSettings, SettingsConfigDict
from apps.bot import create_bot, create_dispatcher

load_dotenv()


class Settings(BaseSettings):
    BOT_TOKEN: str
    # CLAUDE_API_KEY: str

    class Config:
        model_config = SettingsConfigDict(env_file=".env")


async def main() -> None:
    settings = Settings()
    bot = create_bot(settings.BOT_TOKEN)
    dp = create_dispatcher()
    print("Bot ishga tushdi...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
