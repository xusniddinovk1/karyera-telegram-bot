from aiogram import Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from aiogram.types import Message

router = Router()


class CVForm(StatesGroup):
    waiting_name = State()
    waiting_speciality = State()
    waiting_experiences = State()
    waiting_skills = State()
    waiting_projects = State()


@router.message(Command("cv"))
async def process_cv(message: Message, state: FSMContext) -> None:
    await state.set_state(CVForm.waiting_name)
    await message.answer("Ism-Familiyangiz?")


@router.message(CVForm.waiting_name)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await state.set_state(CVForm.waiting_speciality)
    await message.answer("Mutaxassisligingiz? (masalan: Backend Developer)")


@router.message(CVForm.waiting_speciality)
async def process_speciality(message: Message, state: FSMContext) -> None:
    await state.update_data(speciality=message.text)
    await state.set_state(CVForm.waiting_experiences)
    await message.answer("Tajribangiz? (masalan: 2 yil Django, 1 yil FastAPI)")


@router.message(CVForm.waiting_experiences)
async def process_experiences(message: Message, state: FSMContext) -> None:
    await state.update_data(experiences=message.text)
    await state.set_state(CVForm.waiting_skills)
    await message.answer("Ko'nikmalaringiz? (masalan: Python, PostgreSQL, Docker)")


@router.message(CVForm.waiting_skills)
async def process_skills(message: Message, state: FSMContext) -> None:
    await state.update_data(skills=message.text)
    await state.set_state(CVForm.waiting_projects)
    await message.answer("Loyihalaringiz? (masalan: Karyera.ai — AI CV bot)")


@router.message(CVForm.waiting_projects)
async def process_projects(message: Message, state: FSMContext) -> None:
    await state.update_data(projects=message.text)

    # Barcha ma'lumotlarni yig'amiz
    data = await state.get_data()
    await state.clear()

    # Hozircha oddiy matn — keyinchalik AI ga yuboramiz
    await message.answer(
        f"✅ Ma'lumotlar qabul qilindi!\n\n"
        f"👤 Ism: {data['name']}\n"
        f"💼 Mutaxassislik: {data['speciality']}\n"
        f"📋 Tajriba: {data['experiences']}\n"
        f"🛠 Ko'nikmalar: {data['skills']}\n"
        f"🚀 Loyihalar: {data['projects']}\n\n"
        f"Tez orada CV tayyor bo'ladi..."
    )
