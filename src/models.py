from .database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, text, BLOB
from sqlalchemy.orm import relationship

class Events(Base):
    __tablename__ = "events"


    event_id = Column(Integer, primary_key=True, index=True)
    event_name = Column(Integer)
    org_id = Column(Integer, primary_key=True, index=True)
    sponsor = Column(text)
    description = Column(text)
    materials_id = Column(Integer, primary_key=True, index=True)


class Materials(Base):
    __tablename__ = "materials"


    materials_id = Column(Integer, primary_key=True, index=True)
    video = Column(BLOB)
    photo = Column(BLOB)


class Reg_on_events(Base):
    __tablename__ = "reg_on_events"


    user_id = Column(Integer, primary_key=True, index=True)
    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer, primary_key=True, index=True)

    company_id = Column(Integer, primary_key=True, index=True)


class User(Base):
    __tabelname__ = "user"

    user_id = Column(Integer, primary_key=True, index=True, unique=True)
    full_name = Column(String, unique=True)
    email = Column(text, unique=True)
    password = Column(text)

class Company(Base):
    __tablename__ = "company"


    company_id = Column(Integer, primary_key = True, index = True)
    inn = Column(Integer, primary_key = True)
    email = Column(text, primary_key = True)
