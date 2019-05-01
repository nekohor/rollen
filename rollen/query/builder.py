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
            self.onlykey(key)
        elif operator and not value:
            self.isequal(key, operator)
        elif not operator and value:
            self.isequal(key, value)
        elif operator and value:
            self.wheres.append([key, operator, value])
        else:
            raise Exception("other circums in where()")

        return self

    def onlykey(self, key):
        """ no return """

        if isinstance(key, list):
            self.add_conditions_to_wheres(key)
        else:
            raise Exception("wrong type of one param key")

    def add_conditions_to_wheres(self, conditions):
        """ no return """

        for elems in conditions:
            if isinstance(elems, list):
                raise Exception("type of condition not list")

            if len(elems) != 3:
                raise Exception("count of condition list not equal to 3")

            for elem in elems:
                if isinstance(elem, str):
                    pass
                else:
                    raise Exception("type of elem in condition not str")

        for key, oper, val in conditions:
            self.wheres.append([key, oper, val])

    def isequal(self, key, value):
        """ no return """

        if isinstance(key, str):
            pass
        else:
            raise Exception("wrong type of key, str needed")

        if isinstance(value, list):
            self.wheres.append([key, "in", value])
        else:
            self.wheres.append([key, "=", value])

    def operator_strategy(self, df, key, oper, val):
        if oper == "=" or oper == "==":
            return df.loc[df[key] == val]
        elif oper == "in" or oper == "isin":
            return df.loc[df[key].isin(val)]
        elif oper == "!=" or oper == "<>":
            return df.loc[df[key] != val]
        elif oper == ">":
            return df.loc[df[key] > val]
        elif oper == "<":
            return df.loc[df[key] < val]
        elif oper == ">=":
            return df.loc[df[key] >= val]
        elif oper == "<=":
            return df.loc[df[key] <= val]
        else:
            raise Exception("unknown operator")

    def get(self):
        for key, oper, val in self.wheres:
            self.df = self.operator_strategy(self.df, key, oper, val)
        return self.df
