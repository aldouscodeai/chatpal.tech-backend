from fastapi import APIRouter
from models.booking import Booking
import json
import os

router = APIRouter()

# Absolute path to the leads.json file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATH = os.path.join(BASE_DIR, "data", "leads.json")

@router.post("/book")
async def create_booking(booking:Booking):
    with open(FILE_PATH, "r") as file:
        data = json.load(file)
        
        if len(data) == 0:
            new_id = 1
        else:
            new_id = data[-1]["id"] + 1

        booking_dict = booking.dict()
        booking_dict["id"] = new_id
        data.append(booking_dict)        
        
        with open(FILE_PATH, "w") as file:
            json.dump(data, file, indent=4)

        return {
            "message": "Booking saved successfully!",
                "booking_id": new_id
                }

@router.get("/bookings")
async def get_booking():

    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    return data


@router.delete("/book/{booking_id}")
async def delete_booking(booking_id: int):

    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    updated_data = [booking for booking in data if booking["id"] != booking_id]

    if len(data) == len(updated_data):
        return {"error": "Booking not found"}    

    with open(FILE_PATH, "w") as file:
        json.dump(updated_data, file, indent = 4)

    return {"message": f"Booking {booking_id} deleted successfully!"}

@router.put("/book/{booking_id}")
async def update_booking(booking_id: int, updated_booking: Booking):

    with open(FILE_PATH, "r") as file:
        data = json.load(file)

    booking_found = False

    for booking in data:
        if booking["id"] == booking_id:
            booking["name"] = updated_booking.name
            booking["phone"] = updated_booking.phone
            booking["email"] = updated_booking.email
            booking["service"] = updated_booking.service
            booking["slot"] = updated_booking.slot
            booking["notes"] = updated_booking.notes
            booking_found = True
            break

    if not booking_found:
        return {"error": "Booking not found"}

    with open(FILE_PATH, "w") as file:
        json.dump(data, file, indent=4)

    return {"message": f"Booking {booking_id} updated successfully"}
    