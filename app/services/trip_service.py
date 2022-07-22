from sqlalchemy.orm import Session

from ..models.models import Trip


def get_trips(db: Session):
    return db.query(Trip).all()


def get_trip(db: Session, trip_id: int):
    return db.query(Trip).filter(Trip.id == trip_id).first()


def create_trip(db: Session):
    pass