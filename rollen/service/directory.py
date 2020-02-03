from rollen.config.millline import MILLLINES
from rollen.utils import DirectoryUtils
from rollen.utils.millline import MillLine

from rollen.dao import DirectoryDao
import os
import pandas as pd


class DirectoryService():

    def sync(self):

        for line in MILLLINES:

            root_dir = MillLine.get_pond_root_dir(line)
            months = os.listdir(root_dir)

            for month in months:

                month_dir = root_dir + "/" + month

                dates = [x for x in os.listdir(month_dir) if len(x) == 8]

                for date in dates:

                    self.sync_table_with_date(line, date)

                    print(line, date, "sync complete")

    def sync_table_with_date(self, line, date):

        cur_dir = DirectoryUtils.get_pond_date_dir(line, date)
        header = MillLine.get_coil_id_header(line)
        total_coil_ids = [x for x in os.listdir(cur_dir) if x[0] == header]

        if len(total_coil_ids) == 0:
            return

        d = DirectoryDao(line)
        exists = d.get_data_by_start_end("coil_id", total_coil_ids).all()
        exist_coil_ids = [x.coil_id for x in exists]

        not_exist_coil_ids = (
            set(total_coil_ids).difference(set(exist_coil_ids))
        )

        d.insert_data(date, not_exist_coil_ids)

    def get_data_by_dates(self, line, dates):

        d = DirectoryDao(line)
        query = d.get_data_by_start_end("start_date", dates)

        return self.to_df(query)

    def get_data_by_coil_ids(self, coil_ids):

        df = pd.DataFrame()
        for line in MILLLINES:
            d = DirectoryDao(line)
            query = d.get_data_in_arrays("coil_id", coil_ids)
            df.append(self.to_df(query))
        df.index = list(range(df.shape[0]))
        return df

    def to_df(self, query):
        df = pd.read_sql(query.statement, query.session.bind)
        df = self.transfer_date(df)
        df = self.add_cur_dir(df)
        return df

    def transfer_date(self, df):
        df["start_date"] = df["start_date"].apply(lambda x: str(x))
        return df

    def add_cur_dir(self, df):

        df["line"] = df["coil_id"].apply(lambda x: MillLine.get_line_by_id(x))
        df["cur_dir"] = [
            DirectoryUtils.get_pond_date_dir(
                df.loc[i, "line"], df.loc[i, "start_date"]
            ) for i in df.index
        ]
        return df
