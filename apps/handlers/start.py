from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def command_start_handler(message: Message) -> None:
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
