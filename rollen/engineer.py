from .time import TimeUtils
from .db import DataBase
from .grade import Catego


class Rollen():

    def __init__(self):
        self.time = TimeUtils()
        self.grade = Catego(self)

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

    def get_data_collection_dir(self, tag):
        return "d:/data_collection_{}".format(tag)

    def get_module_dir(self, sub_module):
        module_dir = "C:/NutCloudSync/code/rollen/rollen"
        return module_dir + "/" + sub_module
