import os
import pandas as pd

from rollen.domain.ledger import LedgerCleaner
from rollen.utils import DirectoryUtils


class LedgerReader():

    def __init__(self, line, table_name):

        self.line = line
        self.table_name = table_name

        self.freq = self.get_frequency()

        self.cleaner = LedgerCleaner(self.line)

        self.df_cols = pd.read_excel(
            DirectoryUtils.get_module_dir("app.ledger") + "/cols.xlsx")

    def get_frequency(self):
        self.table_names_dict = {
            "monthly": ["excel", "temp", "shiftblock",
                        "evaluate", "nonC41", "cid", "backoff", "shape"],
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

        self.month_date = month_date

        file_name = os.path.join(
            DirectoryUtils.get_prod_data_dir(
                self.freq, self.line, self.table_name),
            getattr(self, "get_{}_file_name".format(self.freq))()
        )
        return file_name

    def get_yearly_file_name(self):
        file_name = "{}_{}_{}.xlsx".format(
            self.line, self.table_name, str(self.month_date)[:4],
        )
        return file_name

    def get_monthly_file_name(self):
        return "{}_{}_{}.xlsx".format(
            self.line, self.table_name, self.month_date)
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------

    # read different data filter with cleaner
    def read_data(self, month_date):

        file_name = self.get_file_name(month_date)

        # read file as pandas.dataframe
        df = pd.read_excel(file_name)

        # post process
        df.columns = pd.Series(df.columns).apply(lambda x: x.strip())
        df = self.cleaner.clean_data(self.table_name, df)
        df.drop_duplicates("coil_id", "last", inplace=True)
        df["month"] = self.month_date

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
            raise Exception("table_name not in df_cols")
        return cols
