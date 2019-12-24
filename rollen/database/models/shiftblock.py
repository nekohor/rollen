from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


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
