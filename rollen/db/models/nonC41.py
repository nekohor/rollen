from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time, Float, TIMESTAMP
from sqlalchemy.orm import sessionmaker

import rollen

Base = declarative_base()


class NonC41(Base):
    __tablename__ = 'nonC41'

    id = Column(Integer, primary_key=True, autoincrement=True)
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

if __name__ == '__main__':
    lines = [2250, 1580]

    for line in lines:
        rln = rollen.roll(line)
        Base.metadata.create_all(rln.db.engine)
        DBSession = sessionmaker(bind=rln.db.engine)

        # 创建session
        session = DBSession()
        # 利用session创建查询，query(对象类).filter(条件).one()/all()

        session.close()
