

class DataFrameQueryBuilder():

    def __init__(self):
        pass

    def table(self, df):
        self.df = df
        return self

    def where(self, col_name, operator, value):
