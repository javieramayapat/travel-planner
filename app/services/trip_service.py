from sqlalchemy.orm import Session

from ..models.models import Trip
from ..schemas import trip_schema


def get_trips(db: Session):
    return db.query(Trip).all()


def get_trip(db: Session, trip_id: int):
    return db.query(Trip).filter(Trip.id == trip_id).first()


def create_trip(db: Session, trip: trip_schema.TripCreate):
    db_trip = Trip(user_id=trip.user_id,
                   origin_name=trip.origin_name,
                   destination_name=trip.destination_name,
                   departure_date=trip.departure_date,
                   arrival_date=trip.arrival_date)

    db.add(db_trip)
    db.commit()
    db.refresh(db_trip)

    return db_trip
