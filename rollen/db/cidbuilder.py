import os
import logging
import rollen
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

import pymysql
import numpy as np

from .insertion import Insertion
from .models import Cid


class CidBuilder():

    def __init__(self, rln):
        self.rln = rln
        # self.cid = None

        def add_own_encoders(conn, cursor, query, *args):
            cursor.connection.encoders[np.float64] = (
                lambda value, encoders: float(value))

        event.listen(
            self.rln.db.engine,
            "before_cursor_execute",
            add_own_encoders)

    def is_nan(self, field):
        tag = False
        if field is np.nan:
            tag = True
        elif str(field) == 'nan':
            tag = True
        return tag

    def trans_type(self, field):
        result = None
        if type(field) == np.float64:
            result = float(field)
        elif type(field) == np.int64:
            result = int(field)
        else:
            result = field
        return result

    def commit(self, record):

        # 创建Cid对象
        cid = Cid()
        self.need_cols = self.need_cols_in_excel + self.need_cols_in_temp

        for col in self.need_cols:
            field = record[col]

            if self.is_nan(field):
                pass
            else:
                setattr(cid, col, self.trans_type(field))

        # 添加到session
        self.session.add(cid)
        # 提交
        self.session.commit()

    def insert(self):
        self.DBSession = sessionmaker(bind=self.rln.db.engine)
        # 创建Session对象
        self.session = self.DBSession()

        # self.df_cid = pd.read_excel(self.cid_filename)

        for idx in self.df_cid.index:

            record = self.df_cid.loc[idx]

            coil_id = record["coil_id"]

            exists = self.session.query(Cid).filter(
                Cid.coil_id == coil_id).first()

            if exists is None:
                self.commit(record)
            else:
                print(coil_id, "already exixts")

            print("commit ok", coil_id, record["datetime"])

        self.session.close()

    def merge(self, month_date):

        # df_excel = rln.db.table("excel").where(
        #     "month", "=", month_date).get()

        # df_temp = rln.db.table("temp").where(
        #     "month", "=", month_date).get()

        df_excel = Insertion(self.rln, "excel").read_data(month_date)
        df_temp = Insertion(self.rln, "temp").read_data(month_date)
        print(df_excel.shape)
        print(df_temp.shape)

        self.need_cols_in_excel = [
            "coil_id",
            "start_date",
            "start_time",
            "datetime",
            "end_date",
            "end_time",
            "slab_id",
            "slab_grade",
            "steel_grade",
            "slab_weight",
            "coil_weight",
            "next_process",
            "last_process",
            "fce_num",
            "dc_num",
            "coil_len",
            "aim_thick",
            "aim_width",
            "aim_crown",
            "prod_order",
            "sale_order",
            "sale_item_id",
            "order_purpose",
            "month"

        ]
        self.need_cols_in_temp = [
            "coil_id",
            "aim_ht",
            "act_ht",
            "aim_fdt",
            "aim_ct"
        ]

        self.df_cid = pd.merge(
            df_excel[self.need_cols_in_excel],
            df_temp[self.need_cols_in_temp],
            how='left',
            on="coil_id"
        )

    def to_excel(self, month_date):
        self.cid_filename = Insertion(
            self.rln, "cid").get_file_name(month_date)
        self.df_cid.to_excel(self.cid_filename)
