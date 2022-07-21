from fastapi import FastAPI, status
from typing import Dict

from .routers import trips_router

app = FastAPI(title="📑 Travel Planner API 📑",
              version="1.0",
              description="Personal trip planner integrating weather data from OpenWeater's Public API")


@app.get(path="/", tags=['Root'], status_code=status.HTTP_200_OK)
def index() -> Dict[str, str]:
    return {"Hello": "Travelers 🛫"}


app.include_router(trips_router.router, prefix="/api/v1")
