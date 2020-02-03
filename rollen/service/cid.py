from rollen.dao import CidDao

from rollen.config.millline import MILLLINES
from rollen.utils.millline import MillLine
from rollen.utils import DirectoryUtils

import pandas as pd


class CidService():

    def __init__(self):
        pass

    def get_data_by_dates(self, line, dates):

        d = CidDao(line)
        query = d.get_data_by_start_end("start_date", dates)

        return self.to_df(query)

    def get_data_by_coil_ids(self, coil_ids):

        df = pd.DataFrame()
        for line in MILLLINES:
            d = CidDao(line)
            query = d.get_data_in_arrays("coil_id", coil_ids)
            df = df.append(self.to_df(query))
        df.index = list(range(df.shape[0]))
        return df

    def to_df(self, query):
        df = pd.read_sql(query.statement, query.session.bind)
        df = self.transfer_date(df)
        df = self.add_cur_dir(df)
        return df

    def transfer_date(self, df):
        df["start_date"] = (
            df["start_date"].apply(lambda x: x.strftime("%Y%m%d"))
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


if __name__ == '__main__':

    s = CidService()

    coil_ids = ["M19152616M",
                "M19157744W",
                "H19165201X",
                "M19164044M",
                "M19164047M",
                "H191600820",
                "H19132068A",
                "H191536710",
                "H191536720",
                "H191536730",
                "H190125860",
                "H190594910",
                "H190594920",
                "H190594930",
                "H190594940",
                "H190594950",
                "H190594960",
                "H190594970",
                "H190594980",
                "H190594990"]

    q = s.get_data_by_coil_ids(coil_ids)
    print(q)
