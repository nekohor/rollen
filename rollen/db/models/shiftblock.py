from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time, Float, TIMESTAMP
from sqlalchemy.orm import sessionmaker

import rollen

Base = declarative_base()


class ShiftBlock(Base):
    __tablename__ = 'shiftblock'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_id = Column(String(30), unique=True, nullable=False)
    order_thick = Column(String(80))
    order_width = Column(String(80))
    steel_grade = Column(String(80))
    next_process = Column(String(80))
    act_weight = Column(String(80))
    process_defect = Column(String(80))
    process_defect_desc = Column(String(80))
    coil_defect = Column(String(80))
    coil_defect_desc = Column(String(80))
    surface_defect = Column(String(80))
    surface_defect_desc = Column(String(80))
    treatment = Column(String(80))
    block_state = Column(String(80))
    block_man = Column(String(80))
    slab_grade = Column(String(80))
    surface_feedback_grade = Column(String(80))
    coil_quality_grade = Column(String(80))
    shape_quality_grade = Column(String(80))
    convertor_id = Column(String(80))
    slab_id = Column(String(80))

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