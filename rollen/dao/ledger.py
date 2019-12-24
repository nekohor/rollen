from rollen.database.models import Excel
from rollen.database.models import Temp
from rollen.database.models import Evaluate
from rollen.database.models import ShiftBlock
from rollen.database.models import Chem
from rollen.database.models import NonC41

from rollen.domain.ledger import LedgerReader
from rollen.database import DataBaseManager

import numpy as np
import logging

from sqlalchemy.orm import sessionmaker


class LedgerDao:

    def __init__(self, line, table_name, month):

        self.line = str(line)
        self.table_name = str(table_name)
        self.month = month

        self.reader = LedgerReader(self.line, self.table_name, self.month)
        self.engine = DataBaseManager.get_database("ledger")[self.line]
        self.model_class = self.get_model_class(self.table_name)

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

    def convert_field_type(self, field):
        result = None
        if type(field) == np.float64:
            result = float(field)
        elif type(field) == np.int64:
            result = int(field)
        else:
            result = field
        return result

    def get_model_obj(self, record):

        # get object of model class
        model_obj = self.model_class()

        for col in self.reader.get_cols():
            field = record[col]

            if self.is_nan(field):
                pass
            else:
                setattr(model_obj, col, self.convert_field_type(field))

        return model_obj

    def insert_data(self):
        # 创建Session对象
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

        # self.insert_data_one_by_one()
        self.insert_data_with_diff()
        self.session.close()

    def insert_data_with_diff(self):

        df = self.reader.read_data()
        df.index = list(range(0, df.shape[0]))

        total_coil_ids = df["coil_id"]
        first_coil_id = total_coil_ids[0]
        last_coil_id = total_coil_ids[df.shape[0] - 1]

        exists = self.session.query(
            self.model_class.coil_id
        ).filter(
            self.model_class.coil_id.between(first_coil_id, last_coil_id)
        ).all()

        exist_coil_ids = [x.coil_id for x in exists]
        not_exist_coil_ids = (
            set(total_coil_ids).difference(set(exist_coil_ids))
        )

        df_insert = df.loc[df["coil_id"].isin(not_exist_coil_ids)]

        if df_insert.shape[0] == 0:
            return

        for idx in df_insert.index:
            record = df_insert.loc[idx]
            self.session.add(self.get_model_obj(record))

            if idx % 1000 == 0:
                insertion_info = "{} {} {} {} added".format(
                    self.line, self.table_name, self.month, record["coil_id"])
                logging.info(insertion_info)

        self.session.commit()
        logging.info("{} {} {} commit completed".format(
            self.line, self.table_name, self.month))

    def insert_data_one_by_one(self):

        df = self.reader.read_data()
        df.index = list(range(0, df.shape[0]))

        for idx in df.index:

            record = df.loc[idx]
            coil_id = record["coil_id"]

            exists = self.session.query(self.model_class.coil_id).filter(
                self.model_class.coil_id == coil_id).first()

            insertion_info = "{} {} {} {}".format(
                self.line, self.table_name, self.month, coil_id)

            if exists is None:
                self.session.add(self.get_model_obj(record))

                logging.info(
                    "{} added".format(insertion_info)
                )
            else:
                logging.info(
                    "{} already exists".format(insertion_info)
                )

        self.session.commit()
