from sqlalchemy.orm import Session

from db.sqlite_db import SessionLocal
from models.booking import Booking


def save_booking(data: dict):

    db: Session = SessionLocal()

    booking = Booking(
        name=data["name"],
        email=data["email"],
        date=data["date"],
        time=data["time"]
    )

    db.add(booking)
    db.commit()
    db.close()