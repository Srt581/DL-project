# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, text, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()
metadata = Base.metadata

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)
    created_on = Column(DateTime, nullable=False)
    children = relationship("Teacher", secondary='link',back_populates="parents")


class Teacher(Base):
    __tablename__ = 'teacher'
    id = Column(Integer, nullable=False, primary_key=True)
    unique_id = Column(String(100), nullable=False)
    name = Column(String(100), nullable=False)
    created_on = Column(DateTime, nullable=False)
    parents = relationship("Students", secondary='link',back_populates="children")


class Link(Base):
    __tablename__ = 'link'
    id = Column(Integer, nullable=False, primary_key=True)
    students_id = Column(Integer, ForeignKey('students.id'))
    teacher_id = Column(Integer, ForeignKey('teacher.id'))
    created_on = Column(DateTime, nullable=False, default=datetime.datetime.now)

# engine = create_engine('sqlite:///mycollege.db', echo = True)
# Base.metadata.create_all(engine)

