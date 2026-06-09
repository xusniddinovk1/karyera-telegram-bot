from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from apps.services.analytics_service import AnalyticsService

router = Router()


@router.message(Command("start"))
async def command_start_handler(
        message: Message,
        analytics_service: AnalyticsService,

) -> None:
    analytics_service.track(
        user_id=message.from_user.id,
        event="bot_started",
        properties={
            "username": message.from_user.username,
            "full_name": message.from_user.full_name,
        }
    )
    await message.answer(
        "Salom! Karyera.ai ga xush kelibsiz 👋\n\n"
        "Men sizga:\n"
        "📄 Professional CV yaratishda\n"
        "🎯 Mock intervyuga tayyorlanishda\n"
        "yordam beraman.\n\n"
        "Boshlash uchun /cv yoki /interview yozing."
    )


@router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    await message.answer(
        "📌 Buyruqlar:\n\n"
        "/start — Botni ishga tushirish\n"
        "/cv — CV yaratish\n"
        "/interview — Mock intervyu\n"
        "/help — Yordam"
    )
