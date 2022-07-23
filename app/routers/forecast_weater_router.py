from fastapi import APIRouter, Path, status

from ..services import forecast_weater_service


router = APIRouter(prefix="/forecast", tags=['Forecast Weater'])


@router.get(path="/{city_name}", status_code=status.HTTP_200_OK)
def get_forecast_weater(city_name: str = Path(..., example="London")):
    forecast = forecast_weater_service.get_forecast_by_city_name(city_name)
    return forecast