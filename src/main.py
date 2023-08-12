from database import *
from models import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
from fastapi import HTTPException
 
# создаем таблицы
Base.metadata.create_all(bind=engine)
 
app = FastAPI()
 
# определяем зависимость
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register/")
async def register(name: str, surname: str, email: str, password: str):
    db = SessionLocal()
    user = Users(name=name, surname=surname, email=email, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered successfully"}

@app.post("/login/")
async def login(email: str, password: str):
    db = SessionLocal()
    user = db.query(Users).filter(Users.email == email).first()
    if user is None or user.password != password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}

@app.post("/create_event/")
async def create_event(event_name: str, company_id: int, sponsor: str, description: str, materials_id: int):
    db = SessionLocal()
    event = Events(event_name=event_name, company_id=company_id, sponsor=sponsor, description=description, materials_id=materials_id)
    db.add(event)
    db.commit()
    db.refresh(event)
    return {"message": "Event created successfully"}

@app.get("/events/")
async def get_events():
    db = SessionLocal()
    events = db.query(Events).all()
    return events