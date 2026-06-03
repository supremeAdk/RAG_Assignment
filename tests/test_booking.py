# test_booking.py

from services.booking_service import (
    extract_booking_info
)

print(
    extract_booking_info(
        "Book an interview for Supreme Adhikari on June 10 at 3 PM. Email is supreme@gmail.com"
    )
)