from fastapi import FastAPI

from app.api.routes.chat import router as chat_router
from app.api.routes.health import router as health_router

app = FastAPI(
    title="Ops-Pilot AI Service",
    version="2.0.0",
)


@app.get("/")
def root():
    return {"message": "Welcome to Ops-Pilot AI Service"}


app.include_router(health_router)
app.include_router(chat_router)