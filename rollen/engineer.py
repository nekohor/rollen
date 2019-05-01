from .time import TimeUtils
from .db import DataBase
from .grade import Catego
from .query import DataFrameQueryBuilder


class Rollen():

    def __init__(self):
        self.time = TimeUtils()
        self.grade = Catego()
        self.query = DataFrameQueryBuilder()

    def set_line(self, line):
        if isinstance(line, int):
            pass
        else:
            raise Exception("line with wrong type (not int)")
        self.line = line
        self.db = DataBase(self.line)
        return self

    def get_line(self):
        if hasattr(self, "line"):
            return self.line
        else:
            raise Exception("rollen object doesn't have line attr")
