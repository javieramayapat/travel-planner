from typing import Dict, List
import requests

from ..config import settings

OPEN_WEATER_KEY = settings.OPEN_WEATER_KEY


def get_forecast_by_city_name(city_name: str) -> List[Dict]:
    """
    Allows return the 5 day forecast to next days with and interval of 3 hour
    to notice people

    Args:
        city_name (str): Name of the city to consult weather forecasts

    Returns:
        forecast: List[Dicts] A list of dictionaries with forecast with an interval of 3 hours
    """
    r = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={OPEN_WEATER_KEY}")
    result = r.json()
    forecasts = result['list']

    return forecasts
