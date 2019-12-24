from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP


Base = declarative_base()


class Temp(Base):
    __tablename__ = 'temp'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_id = Column(String(30), unique=True, nullable=False)

    steel_grade = Column(String(80))
    aim_thick = Column(Float)
    aim_width = Column(Float)
    mean_fdt = Column(Float)
    aim_fdt = Column(Float)
    fdt_bias = Column(Float)
    mean_ct = Column(Float)
    aim_ct = Column(Float)
    ct_bias = Column(Float)
    act_ht = Column(Float)
    aim_ht = Column(Float)
    ht_bias = Column(Float)
    fdt_perc = Column(Float)
    ct_perc = Column(Float)
    slab_id = Column(String(80))
    extract_time = Column(TIMESTAMP)
    order_purpose = Column(String(30))
    charge_temp = Column(Float)
    charge_time = Column(TIMESTAMP)
    fce_num = Column(String(30))
    slab_weight = Column(Float)
    act_weight = Column(Float)

    month = Column(Integer)
