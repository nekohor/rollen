import os
import logging
import rollen
import pandas as pd
from sqlalchemy.orm import sessionmaker
from sqlalchemy import event

import pymysql
import numpy as np

from .insertion import Insertion
from .models import Excel
from .models import Temp
from .models import Evaluate
from .models import NonC41
from .models import ShiftBlock
from .models import Chem

class TableBuilder():

    def __init__(self, rln, tag):
        self.rln = rln
        self.tag = tag

        self.model_class = self.get_model_class(self.tag)

        self.insertion = Insertion(self.rln, self.tag)
        self.patch_for_float64()

    def patch_for_float64(self):

        def add_own_encoders(conn, cursor, query, *args):
            cursor.connection.encoders[np.float64] = (
                lambda value, encoders: float(value))

        event.listen(
            self.rln.db.engine,
            "before_cursor_execute",
            add_own_encoders)

    def get_model_class(self, table_name):
        model_class = None
        if table_name == "excel":
            model_class = Excel
        elif table_name == "temp":
            model_class = Temp
        elif table_name == "evaluate":
            model_class = Evaluate
        elif table_name == "nonC41":
            model_class = NonC41
        elif table_name == "shiftblock":
            model_class = ShiftBlock
        elif table_name == "chem":
            model_class = Chem
        else:
            raise Exception("wrong model tag for model class")
        return model_class

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

    def get_model_obj(self, record):
        # 创建Cid对象
        model_obj = self.model_class()

        for col in self.insertion.get_cols():
            field = record[col]

            # print(col, field)
            # print(type(field))

            if self.is_nan(field):
                pass
            else:
                setattr(model_obj, col, self.trans_type(field))

        return model_obj

    def insert_one_by_one(self):

        for idx in self.df.index:

            record = self.df.loc[idx]

            coil_id = record["coil_id"]

            exists = self.session.query(self.model_class).filter(
                self.model_class.coil_id == coil_id).first()

            if exists is None:
                self.session.add(self.get_model_obj(record))
                self.session.commit()
                print("commit ok", coil_id, self.tag, self.month_date)
            else:
                print(coil_id, "already exists")

    def find_start_idx(self):

        start_idx = -1

        cur_idx = 0
        print(self.df.index)
        while cur_idx < self.max_idx - 1:

            record = self.df.loc[cur_idx]
            coil_id = record["coil_id"]

            exists = self.session.query(self.model_class).filter(
                self.model_class.coil_id == coil_id).first()

            if exists is None:
                start_idx = cur_idx
                break
            else:
                print(coil_id, "already exists")

            cur_idx = cur_idx + 1

        return start_idx

    def insert_by_chunks(self):

        self.max_idx = len(self.df.index)
        # start_idx = self.find_start_idx()
        start_idx = 0

        if start_idx == -1:
            return

        chunk_size = 1000

        for chunk in range(start_idx, self.max_idx, chunk_size):

            model_objs = []

            chunk_start = chunk
            chunk_end = min(chunk + chunk_size, self.max_idx)
            for cur_idx in range(chunk_start, chunk_end):

                record = self.df.loc[cur_idx]
                print(record)
                coil_id = record["coil_id"]
                model_objs.append(self.get_model_obj(record))
                print(coil_id, "append to model obj list")

            self.session.bulk_save_objects(model_objs)
            print("bulk_save_objects, chunk at", chunk_start, chunk_end)

        self.session.commit()
        print("commit ok, chunk at", self.tag, self.month_date)

    def insert(self, month_date):
        self.DBSession = sessionmaker(bind=self.rln.db.engine)
        # 创建Session对象
        self.session = self.DBSession()

        self.month_date = month_date
        self.df = self.insertion.read_data(self.month_date)
        self.df.index = list(range(0, self.df.shape[0]))

        self.insert_one_by_one()
        # self.insert_by_chunks()

        self.session.close()