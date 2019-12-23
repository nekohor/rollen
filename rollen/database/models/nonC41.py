from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP


Base = declarative_base()


class NonC41(Base):
    __tablename__ = 'nonC41'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_num = Column(Integer, unique=True, nullable=False)
    coil_id = Column(String(30), unique=True, nullable=False)

    datetime = Column(TIMESTAMP)
    mean_flat = Column(Float)
    max_flat = Column(Float)
    min_flat = Column(Float)
    steel_grade = Column(String(80))
    mean_width = Column(Float)
    mean_thick = Column(Float)
    up_to_standard = Column(Integer)

    month = Column(Integer)
