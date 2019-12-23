import os
import pandas as pd


class Directory:

    def __init__(self):
        pass

    def mkdir(self, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    def get_base_dir(self):
        return os.path.dirname(os.path.abspath(__file__))

    def get_prod_data_dir(self, frequency, line, table_name):
        return (
            "D:/prod_data/ledger_{}/{}/{}".format(frequency, line, table_name)
        )

    def read_excel_data(self, line, table_name, month_date):

        excel_file_name = (
            self.get_prod_data_dir("monthly", line, table_name) +
            "/{}_{}_{}.xlsx".format(line, table_name, month_date)
        )

        df = pd.read_excel(excel_file_name)
        return df
