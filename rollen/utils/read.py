import pandas as pd

from rollen.utils import DirectoryUtils


class ReadUtils():

    @classmethod
    def read_excel_data(cls, line, table_name, month_date):

        excel_file_name = (
            DirectoryUtils.get_prod_data_dir("monthly", line, table_name) +
            "/{}_{}_{}.xlsx".format(line, table_name, month_date)
        )

        df = pd.read_excel(excel_file_name)
        return df
