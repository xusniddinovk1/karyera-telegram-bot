from aiogram import Bot, Dispatcher
from apps.handlers import start_router, cv_router

from apps.services.ai_service import ClaudeService


def create_bot(token: str) -> Bot:
    return Bot(token=token)


def create_dispatcher(claude_service: ClaudeService) -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(cv_router)
    return dp
