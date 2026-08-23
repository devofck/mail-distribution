
from fastapi import APIRouter

router = APIRouter()


@router.get("/status")
async def status():
    return {"status": "ok"}


@router.get("/get_tasks")
async def get_tasks():
    tasks = None
    return {"tasks": tasks}

@router.get("add_telegram_sending")
async def add_telegram_sending():
    pass