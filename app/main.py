from fastapi import FastAPI, status
from typing import Dict

from .models import models
from .config.database import engine
from .routers import trips_router, forecast_weater_router


models.Base.metadata.create_all(bind=engine)


app = FastAPI(title="📑 Travel Planner API 📑",
              version="1.0",
              description="Personal trip planner integrating weather data from OpenWeater's Public API")


@app.get(path="/", tags=['Root'], status_code=status.HTTP_200_OK)
def index() -> Dict[str, str]:
    return {"Hello": "Travelers 🛫"}


app.include_router(trips_router.router, prefix="/api/v1")
app.include_router(forecast_weater_router.router, prefix="/api/v1")
