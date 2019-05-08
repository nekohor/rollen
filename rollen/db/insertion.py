import os
import pandas as pd
import logging
from .database import DataBase
from .dustman import DustMan
from rollen import config


class Insertion():

    def __init__(self, rollen, table_name):
        self.rollen = rollen
        self.line = self.rollen.get_line()

        self.table_name = table_name
        self.tag = self.get_tag(self.table_name)

        self.dustman = DustMan(self.line)

        self.df_cols_path = (
            config.get_module_dir("db") + "/cols.xlsx"
        )
        self.df_cols = pd.read_excel(self.df_cols_path)

    def get_tag(self, table_name):
        self.table_names_dict = {
            "monthly": [
                "excel", "evaluate", "temp", "nonC41", "cid",
                "great_stat"],
            "yearly": ["performance_components"],
            "block": ["act_block", "shift_block"]
        }

        tag = ""
        for key, table_names in self.table_names_dict.items():
            if self.table_name in table_names:
                tag = key

        if tag == "":
            raise Exception("wrong tag dor data_collection_xxx_dirs")
        else:
            return tag

    def get_file_name(self, month_date):
        self.mdate = month_date
        return os.path.join(
            config.get_data_collection_dir(self.tag),
            getattr(self, "get_{}_file_name".format(self.tag))()
        )

    def get_yearly_file_name(self):
        if self.table_name == "performance_components":
            file_name = "{}/{}performance_components.xlsx".format(
                # self.rollen.time.get_year(self.mdate), self.line
                str(self.mdate)[:4], self.line
            )
        else:
            raise Exception("not having other item in yearly data")
        return file_name

    def get_block_file_name(self):
        return "{}/{}/{}_{}{}.xlsx".format(
            self.table_name, self.line, self.mdate, self.line, self.table_name)

    def get_monthly_file_name(self):
        return "{}/{}/{}_{}{}.xlsx".format(
            self.line, self.mdate, self.mdate, self.line, self.table_name)

    # read different data with DustMan()
    def read_data(self, month_date):
        file_name = self.get_file_name(month_date)
        df = pd.read_excel(file_name)

        # post process
        df.columns = pd.Series(df.columns).apply(lambda x: x.strip())
        df = self.dustman.clean_data(self.table_name, df)
        df.drop_duplicates("coil_id", "last", inplace=True)
        df["month"] = self.mdate
        df = self.select_cols(df)
        return df

    def select_cols(self, df):
        if self.table_name in self.df_cols.columns:
            is_null_cols = self.df_cols[self.table_name].notnull()
            cols = self.df_cols[is_null_cols][self.table_name]
            cols = list(cols) + ["month"]
            logging.info(cols)
            df = df.loc[:, cols]
        else:
            logging.info("df of Insertion() without selecting")
        return df

    def insert(self, month_date):
        logging.info("start insert {} {} {}".format(
            self.line, month_date, self.table_name))
        df = self.read_data(month_date)
        df = self.select_cols(df)
        df.to_sql(
            name=self.table_name.lower(),
            con=self.rollen.db.engine,
            if_exists="append",
            index=False)
        logging.info("complete insert {} {} {}".format(
            self.line, month_date, self.table_name))
