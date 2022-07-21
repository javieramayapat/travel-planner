from fastapi import APIRouter, status, Path

router = APIRouter(prefix="/trips", tags=['Trips'])


@router.get(path="/", status_code=status.HTTP_200_OK)
def get_trips():
    pass


@router.get(path="/{trip_id}", status_code=status.HTTP_200_OK)
def get_trip_detail(trip_id: int = Path(..., gt=0, example=1)):
    return {"trip_id": trip_id}


@router.post(path="/", status_code=status.HTTP_201_CREATED)
def create_trip():
    pass
