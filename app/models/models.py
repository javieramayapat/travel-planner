from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship


class User:
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(50), nullable=False)

    trips = relationship("Trips", back_populates="users")


class Trip:
    __tablename__ = "trips"

    id = Column(Integer, primary_key=True)
    origin_name = Column(String(100), nullable=False)
    destination_name = Column(String(400), nullable=False)
    departure_date = Column(TIMESTAMP, nullable=False)
    arrival_date = Column(TIMESTAMP, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))

    users = relationship("Users", back_populates="trips")
