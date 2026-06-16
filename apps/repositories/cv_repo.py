from sqlalchemy.ext.asyncio import AsyncSession
from apps.models.cv import CV


class CVRepository:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    async def save(self, telegram_id: int, data: dict, cv_text: str) -> CV:
        cv = CV(
            telegram_id=telegram_id,
            name=data["name"],
            speciality=data["speciality"],
            experiences=data["experiences"],
            skills=data["skills"],
            projects=data["projects"],
            cv_text=cv_text
        )
        self.session.add(cv)
        await self.session.commit()
        return cv