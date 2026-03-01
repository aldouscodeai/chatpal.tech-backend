# 🚀 Chatpal Backend (MVP)

Autonomous AI-powered backend system for handling business bookings and customer interactions.

---

## ✅ Features

- Create Booking (POST /book)
- Get All Bookings (GET /bookings)
- Update Booking (PUT /book/{booking_id})
- Delete Booking (DELETE /book/{booking_id})
- Auto-generated Booking ID system

---

## 🛠 Tech Stack

- FastAPI
- Pydantic
- Uvicorn
- JSON file storage (MVP stage)

---

## 📦 Project Structure

chatpal_backend/
│
├── main.py  
├── models/  
│   └── booking.py  
├── routes/  
│   └── booking_routes.py  
├── data/  
│   └── leads.json  
├── requirements.txt  
└── .gitignore  

---

## ▶ How To Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Server runs on:

http://127.0.0.1:8000/docs

---

## 🎯 Current Stage

MVP – Core CRUD system completed.  
Next phase: Database integration + Authentication.

---

Built by Aldous Chakma