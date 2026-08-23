from fastapi import FastAPI


#   routers
from app.v1.tasks import router as task_router

app = FastAPI(
    title="Mail delivery API",
    description="Mail delivery API",
    version="1.0",
)

app.include_router(task_router)
