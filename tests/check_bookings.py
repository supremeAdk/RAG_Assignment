from db.sqlite_db import SessionLocal
from models.booking import Booking

db = SessionLocal()

bookings = db.query(Booking).all()

for booking in bookings:
    print(
        booking.id,
        booking.name,
        booking.email,
        booking.date,
        booking.time
    )

db.close()