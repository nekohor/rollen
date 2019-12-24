import os
import pandas as pd

from rollen.domain.ledger import LedgerCleaner
from rollen.utils import DirectoryUtils


class LedgerReader():

    def __init__(self, line, table_name, month_date):

        self.line = str(line)
        self.table_name = table_name
        self.month_date = month_date

        self.file_name = self.get_file_name()

        self.cleaner = LedgerCleaner(self.line)

        self.df_cols = pd.read_excel(
            DirectoryUtils.get_module_dir("domain.ledger") + "/cols.xlsx")

    def get_frequency(self):
        self.table_names_dict = {
            "monthly": ["cid", "excel", "temp", "shiftblock",
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
    def is_file_exists(self):

        is_exist = True

        if self.table_name == "cid":

            excel_file_name = LedgerReader(
                self.line, "excel", self.month_date).get_file_name()
            temp_file_name = LedgerReader(
                self.line, "temp", self.month_date).get_file_name()

            if (
                not os.path.exists(excel_file_name) or
                not os.path.exists(temp_file_name)
            ):
                is_exist = False
        else:
            if not os.path.exists(self.file_name):
                is_exist = False

        return is_exist

    def get_file_name(self):

        self.freq = self.get_frequency()

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
    def read_data(self):

        if self.table_name == "cid":
            self.build_cid_data(self.file_name)

        df = pd.read_excel(self.file_name)

        # post process
        df.columns = pd.Series(df.columns).apply(lambda x: x.strip())
        df = self.cleaner.clean_data(self.table_name, df)
        df.drop_duplicates("coil_id", "last", inplace=True)

        # build constant columns
        # df["coil_num"] = df["coil_id"].apply(lambda x: int(str(x)[1:-1]))
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

    def build_cid_data(self, file_name):

        df_excel = LedgerReader(
            self.line, "excel", self.month_date).read_data()
        df_temp = LedgerReader(
            self.line, "temp", self.month_date).read_data()

        need_cols_in_excel = [
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

        need_cols_in_temp = [
            "coil_id",
            "aim_ht",
            "act_ht",
            "aim_fdt",
            "aim_ct"
        ]

        df_cid = pd.merge(
            df_excel[need_cols_in_excel],
            df_temp[need_cols_in_temp],
            how='left',
            on="coil_id"
        )
        df_cid.to_excel(file_name)
