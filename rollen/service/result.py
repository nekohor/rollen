import numpy as np

from rollen.dao import ResultDao

from rollen.config.millline import MILLLINES
from rollen.utils.millline import MillLine
from rollen.utils import DirectoryUtils

from dateutil.parser import parse


class ResultService():

    def __init__(self):
        pass

    def get_data_by_dates(self, line, dates):

        start_date = dates[0]
        end_date = dates[-1]

        if len(str(start_date)) == 8:
            start_time = str(start_date) + '000000'
        else:
            start_time = str(start_date)

        if len(str(end_date)) == 8:
            end_time = str(end_date) + '235959'
        else:
            end_time = str(end_date)
        print(start_time, end_time)
        d = ResultDao()
        data = d.get_data_by_line_and_time(line, start_time, end_time)
        return self.post_handle(data)

    def get_data_by_coil_ids(self, coil_ids):
        d = ResultDao()
        data = d.get_data_by_coil_ids(coil_ids)
        return self.post_handle(data)

    def get_data_by_date(self, start_date, end_date):
        start_time = str(start_date) + '000000'
        end_time = str(end_date) + '235959'
        d = ResultDao()
        data = d.get_data_by_time(start_time, end_time)
        return self.post_handle(data)

    def post_handle(self, df):
        df = self.transfer_date(df)
        df = self.add_cur_dir(df)
        return df

    def transfer_date(self, df):
        # result end_time responds to start_date in cid
        df["start_date"] = df['end_time'].apply(
            lambda x: np.nan if x is None else parse(str(x)).strftime("%Y%m%d")
        )
        return df

    def add_cur_dir(self, df):

        df["line"] = df["coil_id"].apply(lambda x: MillLine.get_line_by_id(x))
        df["cur_dir"] = [
            DirectoryUtils.get_pond_date_dir(
                df.loc[i, "line"], df.loc[i, "start_date"]
            ) for i in df.index
        ]
        return df
