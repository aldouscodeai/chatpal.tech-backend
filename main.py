from fastapi import FastAPI
from routes.booking_routes import router as booking_router

app = FastAPI()

app.include_router(booking_router)

@app.get("/")
async def home():
    return {"message": "Chatpal Backend running"}

