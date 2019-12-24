from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time, Float, TIMESTAMP
from sqlalchemy.orm import sessionmaker

import rollen

Base = declarative_base()


class Excel(Base):
    __tablename__ = 'excel'

    id = Column(Integer, primary_key=True, autoincrement=True)
    coil_id = Column(String(30), unique=True, nullable=False)
    start_date = Column(Date)
    start_time = Column(Time)
    end_date = Column(Date)
    end_time = Column(Time)
    datetime = Column(TIMESTAMP)
    shift = Column(String(30))
    convertor_id = Column(String(30))
    slab_id = Column(String(30))
    slab_grade = Column(String(80))
    slab_weight = Column(Float)
    coil_weight = Column(Float)
    specifications = Column(String(30))
    steel_grade = Column(String(80))
    next_process = Column(String(30))
    last_process = Column(String(30))
    specs_range = Column(String(30))
    pack_code = Column(String(30))
    plan_id = Column(String(30))
    cross_code = Column(String(30))
    area_code = Column(String(30))
    line_code = Column(String(30))
    col_code = Column(String(30))
    layer_code = Column(String(30))
    storage_time = Column(String(30))
    inner_diam = Column(Integer)
    outside_diam = Column(Integer)
    fce_num = Column(String(30))
    dc_num = Column(String(30))
    mean_crown = Column(Float)
    mean_wedge = Column(Float)
    mean_flatness = Column(Float)
    theoretical_weight = Column(Float)
    set_thick = Column(Float)
    mean_fdt = Column(Integer)
    mean_ct = Column(Integer)
    mean_thick = Column(Float)
    mean_width = Column(Float)
    coil_len = Column(Integer)
    order_width = Column(Float)
    slab_id_in_plan = Column(String(80))
    prod_order = Column(String(80))
    sale_order = Column(String(80))
    sale_item_id = Column(String(80))
    C_C = Column(Float)
    C_Si = Column(Float)
    C_Mn = Column(Float)
    C_P = Column(Float)
    C_S = Column(Float)
    C_AL = Column(Float)
    C_ALS = Column(Float)
    C_O = Column(Float)
    C_N = Column(Float)
    C_Cr = Column(Float)
    C_Ni = Column(Float)
    C_Mo = Column(Float)
    C_Nb = Column(Float)
    C_V = Column(Float)
    C_Ti = Column(Float)
    C_Cu = Column(Float)
    C_Ca = Column(Float)
    judge_result = Column(String(30))
    quality_grade = Column(String(80))
    old_steel_grade = Column(String(80))
    old_material_code = Column(String(80))
    is_cut_weight = Column(String(80))
    weight_after_deduction = Column(Float)
    weight_before_deduction = Column(Float)
    material_code = Column(String(30))
    last_steel_grade = Column(String(30))
    max_width = Column(Float)
    min_width = Column(Float)
    max_crown = Column(Float)
    min_crown = Column(Float)
    max_wedge = Column(Float)
    min_wedge = Column(Float)
    max_flatness = Column(Float)
    min_flatness = Column(Float)
    max_fdt = Column(Integer)
    min_fdt = Column(Integer)
    max_ct = Column(Integer)
    min_ct = Column(Integer)
    order_purpose = Column(String(30))
    aim_width = Column(Float)
    max_thick = Column(Float)
    min_thick = Column(Float)
    SN = Column(String(30))
    storage_num = Column(String(30))
    aim_thick = Column(Float)
    aim_crown = Column(Float)
    is_abnormal = Column(String(30))
    product_type = Column(String(30))

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