from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import  Column, Integer, String

#Строка подкючения
SQLALCHEMY_DATABASE_URL = "sqlite:///./CODE300.db"
#Движок бд
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"chek_same_thread" : False}
)

#сессия базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#создаем базовый класс для моделей
Base = declarative_base()

class User(Base):
    __tablename__ = "people"
 
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer,)
