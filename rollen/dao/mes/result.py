from rollen.database import DataBaseManager
from rollen.utils.millline import MillLine

from rollen.config.millline import LINE2250
from rollen.config.millline import LINE1580

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
            'coil_weight': 'ACTCOILWEIGHT',
            'coil_in_diam': 'COILINDIA',
            'coil_out_diam': 'COILOUTDIA',
            'fce_num': 'FURNACENO',
            'dc_num': 'COILERNR',
            'aim_thick': 'HEXIT',
            'aim_width': 'WEXIT',
            'aim_fdt': 'TEXIT',
            'aim_ct': 'TEXITCS',
            'aim_crown': 'CROWNEXIT',

            'flat_perc': 'FLATEXITPON',
            'crown_perc': 'CROWNEXITPON',
            'wedge_perc': 'WEDGEEXITPON',

            # table slab_result
            # 'slab_grade': 'GRADE_ID',
            # 'slab_length': 'SLABLENGTH',
            # 'slab_width': 'SLABWIDTH',
            # 'slab_thick': 'SLABTHICKNESS',
            # 'slab_weight': 'SLABWEIGHT',

            # table slab_info
            'slab_grade': 'STEELGRADE',
            'slab_length': 'LENGTH',
            'slab_width': 'WIDTH',
            'slab_thick': 'THICKNESS',
            'slab_weight': 'WEIGHT',


            # table order_usage
            # 'order_usage': 'L4_USAGE',
        }

    def get_column_dict(self):
        return self.rename_dict

    def get_sql_columns(self):
        return ["{} as {}".format(v, k) for k, v in self.rename_dict.items()]

    def get_sql(self, line=None):

        def left_join_slab_result(sql):
            res_sql = (
                sql +
                " LEFT JOIN RSLAB_RESULT" +
                " ON RHS_RESULT.ACTSLABID = RSLAB_RESULT.SLAB_ID")

            return res_sql

        def left_join_slab_info(sql):
            res_sql = (
                sql +
                " LEFT JOIN A_SLABINFO" +
                " ON RHS_RESULT.ACTSLABID = A_SLABINFO.SLABID")

            return res_sql

        def left_join_order_usage_table(sql, line):

            if str(line) == LINE2250:
                order_usage_table = "PSI_BACK_PDI_HRM"
            elif str(line) == LINE1580:
                order_usage_table = "PSI_BACK_PDI_HRM_HM2"

            res_sql = (
                sql +
                " LEFT JOIN {order_usage_table}" +
                " ON RHS_RESULT.L4PONO = {order_usage_table}.L4PO"
            ).format(order_usage_table=order_usage_table)
            return res_sql

        initial_sql = "SELECT {cols} FROM RHS_RESULT"

        if line is None:
            sql_cols = self.get_sql_columns()
            sql = initial_sql.format(cols=",".join(sql_cols))
            sql = left_join_slab_info(sql)

        else:
            self.rename_dict['order_usage'] = 'L4_USAGE'
            sql_cols = self.get_sql_columns()
            sql = initial_sql.format(cols=",".join(sql_cols))
            sql = left_join_slab_info(sql)
            sql = left_join_order_usage_table(sql, line)

        return sql

    def get_data_by_sql(self, sql):
        df = pd.read_sql_query(sql, self.conn)
        df.columns = pd.Series(df.columns.values).apply(lambda x: x.lower())
        df.drop_duplicates("coil_id", "last", inplace=True)
        df = df.sort_values(by='coil_id')
        df = df.reset_index(drop=True)
        return df

    def get_data_by_time(self, start_time, end_time):
        # cursor = self.conn.cursor()
        # ... sql ...
        # cursor.execute(sql)
        # rows = cursor.fetchall()
        # cursor.close()
        # return rows

        sql = self.get_sql()
        sql = (
            sql + " WHERE PRODEND >= '{}' AND PRODEND <= '{}'"
        ).format(start_time, end_time)

        data = self.get_data_by_sql(sql)
        return data

    def get_data_by_line_and_time(self, line, start_time, end_time):

        if str(line) == LINE2250:
            time_column = "PRODEND"
        elif str(line) == LINE1580:
            time_column = "PRODSTART"
            # time_column = "PRODEND"

        sql = self.get_sql(line)
        sql = (
            sql +
            " WHERE {time_column} >= '{start_time}'"
            " AND {time_column} <= '{end_time}'"
        ).format(
            time_column=time_column,
            start_time=start_time,
            end_time=end_time)

        coil_id_header = MillLine.get_coil_id_header(line)
        sql = sql + " AND ACTCOILID LIKE '{}%'".format(coil_id_header)

        data = self.get_data_by_sql(sql)
        return data

    def get_data_by_coil_ids(self, coil_ids):
        sql = self.get_sql()

        sql_coil_ids = ", ".join(["'" + x + "'" for x in coil_ids])
        print(sql_coil_ids)
        sql = (
            sql +
            " WHERE ACTCOILID IN ( {} )".format(sql_coil_ids)
        )
        data = self.get_data_by_sql(sql)
        return data
