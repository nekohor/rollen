from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Directory(Base):

    __tablename__ = "directory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_id = Column(String(30), unique=True, nullable=False)
    pond_date = Column(Integer)
