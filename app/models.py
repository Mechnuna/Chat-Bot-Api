from datetime import datetime
from enum import Enum
from sqlalchemy import create_engine, Column, Integer, ForeignKey, String
from sqlalchemy.orm import Session
from app.config import DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StreamStatus(Enum):
    USER = 'user'
    BOT = 'bot'


def connect_db():
    engine = create_engine(DATABASE_URL, connect_args={'check_same_thread': False})
    print(engine.connect())
    session = Session(bind=engine.connect())
    return session


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created_at = Column(String, default=datetime.utcnow())


class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    text_messagee = Column(String)
    message_number = Column(Integer)
    type_user = Column(String, default=StreamStatus.USER.value)
    created_at = Column(String, default=datetime.utcnow())


class Answers(Base):
    __tablename__ = 'answers'

    id = Column(Integer, primary_key=True)
    id_question = Column(Integer)
    id_answer = Column(Integer)
    type_answer = Column(String)
    text_messages = Column(String)
