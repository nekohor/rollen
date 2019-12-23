from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time, Float, TIMESTAMP
from sqlalchemy.orm import sessionmaker

import rollen

Base = declarative_base()


class Cid(Base):
    __tablename__ = 'cid'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_id = Column(String(30), unique=True, nullable=False)
    start_date = Column(Date)
    start_time = Column(Time)
    datetime = Column(TIMESTAMP)
    end_date = Column(Date)
    end_time = Column(Time)
    slab_id = Column(String(30))
    slab_grade = Column(String(80))
    steel_grade = Column(String(80))
    slab_weight = Column(Float)
    coil_weight = Column(Float)
    next_process = Column(String(30))
    last_process = Column(String(30))
    fce_num = Column(String(10))
    dc_num = Column(String(10))
    coil_len = Column(Integer)
    aim_thick = Column(Float)
    aim_width = Column(Float)
    aim_crown = Column(Float)
    prod_order = Column(String(80))
    sale_order = Column(String(80))
    sale_item_id = Column(String(80))
    order_purpose = Column(String(30))

    aim_ht = Column(Integer)
    act_ht = Column(Integer)
    aim_fdt = Column(Integer)
    aim_ct = Column(Integer)

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
