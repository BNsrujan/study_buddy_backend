from fastapi import FastAPI
from app.routers import upload_router, summary_router, mcq_router, eval_router

app = FastAPI()

app.include_router(upload_router)
app.include_router(summary_router)
app.include_router(mcq_router)
app.include_router(eval_router)
