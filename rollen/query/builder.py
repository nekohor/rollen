import pandas as pd


class DataFrameQueryBuilder():

    def __init__(self):
        pass

    def table(self, df):
        self.wheres = []
        self.df = df
        return self

    def select(self, cols):
        if isinstance(cols, list) or isinstance(cols, pd.Series):
            self.df = self.df[cols]
        elif isinstance(cols, str):
            self.df = self.df[cols]
        else:
            raise Exception("wrong type of cols in select()")

        return self

    def where(self, key, operator=None, value=None):
        if not operator and not value:
            return None, None
        elif operator and not value:
            oper, val = self.isequal(operator)
        elif not operator and value:
            oper, val = self.isequal(value)
        elif operator and value:
            oper, val = operator, value
        else:
            raise Exception("other circums in builder where()")
        self.wheres.append([key, oper, val])
        return self

    def isequal(self, value):
        if isinstance(value, list):
            return self.isin()
        else:
            return "=", value

    def notequal(self, value):
        if isinstance(value, list):
            return self.notin()
        else:
            return "<>", value

    def isin(self, elems):
        oper = "IN"

        if isinstance(elems, list):
            pass
        else:
            raise Exception("wrong type of elems in isin()")

        val = "(" + ",".join([str(e) for e in elems]) + ")"

        return oper, val

    def notin(self, elems):
        oper = "NOT IN"

        if isinstance(elems, list):
            pass
        else:
            raise Exception("wrong type of elems in notin()")

        val = "(" + ",".join([str(e) for e in elems]) + ")"

        return oper, val

    def operator_func(self):

    def locate(self):
        for where in wheres:

    def get(self):
        return self.df
