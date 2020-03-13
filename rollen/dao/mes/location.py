from rollen.database import DataBaseManager
from rollen.utils.millline import MillLine

from rollen.config.millline import LINE1580
from rollen.config.millline import LINE2250

from dateutil.parser import parse
import pandas as pd


class LocationDao():

    def __init__(self):
        self.conn = DataBaseManager.get_mes_database()
        self.rename_dict = {
            'coil_id': 'ACT_COIL_ID',
            'location': 'LOCATION',
            'operate_time': 'OPDATE',
        }

    def get_table_name(self, line):

        if str(line) == LINE1580:
            table_name = "MESL2L3_OHSM2HM012"
        elif str(line) == LINE2250:
            table_name = "MESL2L3_OHSMHM012"
        else:
            raise Exception("Wrong Mill Line")
        return table_name

    def get_sql_columns(self):
        return ["{} as {}".format(v, k) for k, v in self.rename_dict.items()]

    def get_sql(self, line):
        sql_cols = self.get_sql_columns()
        sql = "SELECT {cols} FROM {table}".format(
            cols=",".join(sql_cols),
            table=self.get_table_name(line)
        )
        return sql

    def get_data_by_sql(self, sql):
        df = pd.read_sql_query(sql, self.conn)
        df.columns = pd.Series(df.columns.values).apply(lambda x: x.lower())
        return df

    def get_sql_by_coil_ids(self, line, coil_ids):

        start_coil_id = coil_ids[0]
        end_coil_id = coil_ids[-1]
        res_sql = (
            self.get_sql(line) +
            " WHERE {col} >= '{start}' AND {col} <= '{end}'".format(
                col=self.rename_dict['coil_id'],
                start=start_coil_id,
                end=end_coil_id
            )
        )
        return res_sql

    def get_data_by_coil_ids(self, line, coil_ids):
        sql = self.get_sql_by_coil_ids(line, coil_ids)
        df = self.get_data_by_sql(sql)
        return df

    def get_sql_by_time(self, line, start_time, end_time):

        start_time_str = parse(str(start_time)).strftime("%Y-%m-%d %H:%M:%S")
        end_time_str = parse(str(end_time)).strftime("%Y-%m-%d %H:%M:%S")

        res_sql = (
            self.get_sql(line) +
            " WHERE {col} >= '{start}' AND {col} <= '{end}'".format(
                col=self.rename_dict['operate_time'],
                start=start_time_str,
                end=end_time_str
            )
        )
        return res_sql

    def get_data_by_time(self, line, start_time, end_time):
        sql = self.get_sql_by_time(line, start_time, end_time)
        df = self.get_data_by_sql(sql)
        return df
