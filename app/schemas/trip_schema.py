from datetime import datetime
from .base_schema import BaseSchema


class TripBase(BaseSchema):
    user_id: int
    origin_name: str
    destination_name: str
    departure_date: datetime
    arrival_date: datetime


class TripCreate(TripBase):
    pass


class TripOut(TripBase):
    id: int
