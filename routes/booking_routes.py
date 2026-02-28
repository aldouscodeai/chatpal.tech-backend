from fastapi import APIRouter
from models.booking import Booking
import json
import os

router = APIRouter()

# Absolute path to the leads.json file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILE_PATHH = os.path.join(BASE_DIR, "data", "leads.json")

@router.post("/book")
async def create_booking(booking:Booking):
    with open(FILE_PATHH, "r") as file:
        data = json.load(file)
        
        data.append(booking.dict())  
        
        with open(FILE_PATHH, "w") as file:
            json.dump(data, file, indent=4)

            return {"message": "Booking saved successfully!"} 
        
        