from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Chem(Base):
    __tablename__ = 'chem'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_id = Column(String(30), unique=True, nullable=False)

    prod_date = Column(String(80))
    slab_id = Column(String(80))
    convertor_id = Column(String(80))
    aim_thick = Column(String(80))
    aim_width = Column(String(80))
    steel_grade_in_plan = Column(String(80))
    act_weight = Column(String(80))
    block_reason = Column(String(80))
    specs = Column(String(80))
    record_man = Column(String(80))
    test_date = Column(String(80))
    yield_strength = Column(String(80))
    tensile_strength = Column(String(80))
    yield_ratio = Column(String(80))
    A = Column(String(80))
    test_again_result = Column(String(80))
    non_conformance = Column(String(80))
    last_steel_grade = Column(String(80))
    judger = Column(String(80))
    handle_date = Column(String(80))
    degrade_reason = Column(String(80))
    illustration = Column(String(80))
    comment = Column(String(200))
    is_appear_loss = Column(String(80))
    is_appear = Column(String(80))
    appear_date = Column(String(80))

    month = Column(Integer)
