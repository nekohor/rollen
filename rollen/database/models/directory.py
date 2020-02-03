from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer

Base = declarative_base()


class Directory(Base):

    __tablename__ = "directory"

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_id = Column(String(30), unique=True, nullable=False)
    start_date = Column(String(8))
