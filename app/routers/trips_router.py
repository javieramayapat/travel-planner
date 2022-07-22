from fastapi import APIRouter, Body, HTTPException, status, Path, Depends
from sqlalchemy.orm import Session

from ..dependencies import get_db
from ..schemas import trip_schema
from ..services import trip_service

router = APIRouter(prefix="/trips",
                   tags=['Trips'],
                   dependencies=[Depends(get_db)])


@router.get(path="/", response_model=list[trip_schema.TripOut], status_code=status.HTTP_200_OK)
def get_trips(db: Session = Depends(get_db)):
    trips = trip_service.get_trips(db=db)
    return trips


@router.get(path="/{trip_id}", response_model=trip_schema.TripOut, status_code=status.HTTP_200_OK)
def get_trip_detail(db: Session = Depends(get_db), trip_id: int = Path(..., gt=0, example=1)):
    trip = trip_service.get_trip(db=db, trip_id=trip_id)
    if trip is None:
        raise HTTPException(status_code=404, detail="Trip Not Found")
    return trip


@router.post(path="/", response_model=trip_schema.TripOut, status_code=status.HTTP_201_CREATED)
def create_trip(db: Session = Depends(get_db), trip: trip_schema.TripCreate = Body(...)):
    return trip_service.create_trip(db=db, trip=trip)
