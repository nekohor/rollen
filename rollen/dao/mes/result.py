from rollen.database import DataBaseManager

import pandas as pd


class ResultDao():

    def __init__(self):
        self.conn = DataBaseManager.get_mes_database()
        self.rename_dict = {
            'coil_id': 'ACTCOILID',
            'start_time': 'PRODSTART',
            'end_time': 'PRODEND',
            'next_process': 'NEXTPROCCODE',
            'plan_id': 'SEQNO',
            'slab_id': 'ACTSLABID',
            'steel_grade': 'GRADENAME',
            'coil_length': 'COILLENGTH',
            'coil_weight': 'ACTCOILID',
            'coil_in_diam': 'COILINDIA',
            'coil_out_diam': 'COILOUTDIA',
            'fce_num': 'FURNACENO',
            'dc_num': 'COILERNR',
            'aim_thick': 'HEXIT',
            'aim_width': 'WEXIT',
            'aim_fdt': 'TEXIT',
            'aim_ct': 'TEXITCS',
            'aim_crown': 'CROWNEXIT',
            'slab_length': 'SLABLENGTH',
            'slab_width': 'SLABWIDTH',
            'slab_thick': 'SLABTHICKNESS',
            'slab_weight': 'SLABWEIGHT',
        }

    def get_column_dict(self):
        return self.rename_dict

    def get_sql_columns(self):
        return ["{} as {}".format(v, k) for k, v in self.rename_dict.items()]

    def get_sql(self):
        sql = (
            """
            SELECT {cols}
            FROM RHS_RESULT
            LEFT JOIN RSLAB_RESULT
            ON RHS_RESULT.ACTSLABID = RSLAB_RESULT.SLAB_ID
            """
        ).format(cols=",".join(self.get_sql_columns()))
        return sql

    def get_data_by_date(self, start_date, end_date):
        start_time = str(start_date) + '000000'
        end_time = str(start_date) + '235959'
        # print(start_time, end_time)

        return self.get_data_by_time(start_time, end_time)

    def get_data_by_time(self, start_time, end_time):
        # cursor = self.conn.cursor()
        # ... sql ...
        # cursor.execute(sql)
        # rows = cursor.fetchall()
        # cursor.close()
        # return rows

        sql = self.get_sql()
        sql = sql + \
            "WHERE PRODSTART >= '{}' AND PRODEND <= '{}'".format(
                start_time, end_time)

        df = pd.read_sql_query(sql, self.conn)
        df.columns = pd.Series(df.columns.values).apply(lambda x: x.lower())
        return df
