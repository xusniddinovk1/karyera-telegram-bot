from aiogram import Router
from .start import router as start_router
from .cv import router as cv_router

__all__ = ["start_router", "cv_router"]