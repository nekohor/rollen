import os
import pandas as pd
import logging
from .dustman import DustMan
from rollen import config


class Insertion():

    def __init__(self, rollen, table_name):

        self.rollen = rollen
        self.line = self.rollen.get_line()

        self.table_name = table_name
        self.freq = self.get_frequency(self.table_name)

        self.dustman = DustMan(self.line)

        self.df_cols_path = (
            config.get_module_dir("db") + "/cols.xlsx"
        )
        self.df_cols = pd.read_excel(self.df_cols_path)

    def get_frequency(self, table_name):
        self.table_names_dict = {
            "monthly": ["excel", "temp", "shiftblock",
                        "evaluate", "nonC41", "cid"],
            "yearly": ["chem"]
        }

        freq = ""
        for key, table_names in self.table_names_dict.items():
            if self.table_name in table_names:
                freq = key

        if freq == "":
            raise Exception("wrong table_name dor ledger_[freq]_dirs")
        else:
            return freq

    # ------------------------- get file names -----------------------------
    # ----------------------------------------------------------------------
    def get_file_name(self, month_date):
        self.mdate = month_date
        file_name = os.path.join(
            config.get_prod_data_dir(
                self.freq, self.line, self.table_name),
            getattr(self, "get_{}_file_name".format(self.freq))()
        )
        return file_name

    def get_yearly_file_name(self):
        file_name = "{}_{}_{}.xlsx".format(
            self.line, self.table_name, str(self.mdate)[:4],
        )
        return file_name

    def get_monthly_file_name(self):
        return "{}_{}_{}.xlsx".format(
            self.line, self.table_name, self.mdate)
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------

    # read different data with DustMan()
    def read_data(self, month_date):
        file_name = self.get_file_name(month_date)
        df = pd.read_excel(file_name)

        # post process
        df.columns = pd.Series(df.columns).apply(lambda x: x.strip())
        df = self.dustman.clean_data(self.table_name, df)
        df.drop_duplicates("coil_id", "last", inplace=True)
        df["month"] = self.mdate

        # select columns
        df = self.select_cols(df)
        return df

    def select_cols(self, df):
        df = df.loc[:, self.get_cols()]
        return df

    def get_cols(self):
        if self.table_name in self.df_cols.columns:
            is_null_cols = self.df_cols[self.table_name].notnull()
            cols = self.df_cols[is_null_cols][self.table_name]
            cols = list(cols) + ["month"]
        else:
            logging.info("df of Insertion() without selecting")
        return cols

    def insert(self, month_date):
        logging.info("start insert {} {} {}".format(
            self.line, month_date, self.table_name))

        df = self.read_data(month_date)

        # df.to_sql(
        #     name=self.table_name.lower(),
        #     con=self.rollen.db.engine,
        #     if_exists="append",
        #     index=False)

        print(df.shape[1])
        df.to_sql(name='tmp_table', con=self.rollen.db.engine,
                  if_exists='replace', index=False)

        with self.rollen.db.engine.begin() as ctx:
            insert_sql = 'INSERT IGNORE INTO {} (SELECT * FROM tmp_table)'.format(
                self.table_name)
            ctx.execute(insert_sql)

        logging.info("complete insert {} {} {}".format(
            self.line, month_date, self.table_name))
