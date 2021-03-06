from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, TIMESTAMP

Base = declarative_base()


class Evaluate(Base):
    __tablename__ = 'evaluate'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_id = Column(String(30), unique=True, nullable=False)

    steel_grade = Column(String(80))
    aim_thick = Column(Float)
    aim_width = Column(Float)
    aim_fdt = Column(Float)
    aim_ct = Column(Float)
    aim_crown = Column(Float)
    start_time = Column(TIMESTAMP)
    end_time = Column(TIMESTAMP)
    prof_rate = Column(String(80))
    size_rate = Column(String(80))
    temp_rate = Column(String(80))
    overall_rate = Column(String(80))
    thick_rate = Column(String(80))
    thick_perc = Column(Float)
    thick_head_perc = Column(Float)
    thick_tail_perc = Column(Float)
    width_rate = Column(String(80))
    width_perc = Column(Float)
    width_head_perc = Column(Float)
    width_tail_perc = Column(Float)
    cw_rate = Column(String(80))
    c10_perc = Column(Float)
    c10_avg = Column(Float)
    c10_min = Column(Float)
    c10_max = Column(Float)
    c25_perc = Column(Float)
    c25_avg = Column(Float)
    c25_min = Column(Float)
    c25_max = Column(Float)
    c40_perc = Column(Float)
    c40_avg = Column(Float)
    c40_min = Column(Float)
    c40_max = Column(Float)
    c50_perc = Column(Float)
    c50_avg = Column(Float)
    c50_min = Column(Float)
    c50_max = Column(Float)
    c100_perc = Column(Float)
    c100_avg = Column(Float)
    c100_min = Column(Float)
    c100_max = Column(Float)
    w10_perc = Column(Float)
    w10_avg = Column(Float)
    w10_min = Column(Float)
    w10_max = Column(Float)
    w25_perc = Column(Float)
    w25_avg = Column(Float)
    w25_min = Column(Float)
    w25_max = Column(Float)
    w40_perc = Column(Float)
    w40_avg = Column(Float)
    w40_min = Column(Float)
    w40_max = Column(Float)
    w50_perc = Column(Float)
    w50_avg = Column(Float)
    w50_min = Column(Float)
    w50_max = Column(Float)
    w100_perc = Column(Float)
    w100_avg = Column(Float)
    w100_min = Column(Float)
    w100_max = Column(Float)
    flat_rate = Column(String(80))
    flat_perc = Column(Float)
    flat_head_perc = Column(Float)
    flat_tail_perc = Column(Float)
    fdt_rate = Column(String(80))
    fdt_perc = Column(Float)
    fdt_head_perc = Column(Float)
    fdt_tail_perc = Column(Float)
    fdt_mid_perc = Column(Float)
    ct_rate = Column(String(80))
    ct_perc = Column(Float)
    ct_head_perc = Column(Float)
    ct_tail_perc = Column(Float)
    ct_mid_perc = Column(Float)
    rdt_rate = Column(String(80))
    rdt_perc = Column(Float)
    rdw_rate = Column(String(80))
    rdw_perc = Column(Float)
    fdw_rate = Column(String(80))
    fdw_perc = Column(Float)
    tbc_rate = Column(String(80))
    tbc = Column(Float)
    si_rate = Column(String(80))
    si1_perc = Column(Float)
    si2_perc = Column(Float)
    si3_perc = Column(Float)

    month = Column(Integer)
