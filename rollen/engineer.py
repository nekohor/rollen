from .time import TimeUtils
from .db import DataBase
from .grade import Catego
from .query import DataFrameQueryBuilder
from .directory import Directory

# 　　 ┏┓       ┏┓+ +
# 　　┏┛┻━━━━━━━┛┻┓ + +
# 　　┃　　　　　　 ┃
# 　　┃　　　━　　　┃ ++ + + +
# 　 █████━█████  ┃+
# 　　┃　　　　　　 ┃ +
# 　　┃　　　┻　　　┃
# 　　┃　　　　　　 ┃ + +
# 　　┗━━┓　　　 ┏━┛
#        ┃　　  ┃
# 　　　　┃　　  ┃ + + + +
# 　　　　┃　　　┃　Code is far away from bug with the animal protecting
# 　　　　┃　　　┃ + 　　　　         神兽保佑,代码无bug
# 　　　　┃　　　┃
# 　　　　┃　　　┃　　+
# 　　　　┃　 　 ┗━━━┓ + +
# 　　　　┃ 　　　　　┣┓
# 　　　　┃ 　　　　　┏┛
# 　　　　┗┓┓┏━━━┳┓┏┛ + + + +
# 　　　　 ┃┫┫　 ┃┫┫
# 　　　　 ┗┻┛　 ┗┻┛+ + + +


class Engineer():

    def __init__(self):
        self.time = TimeUtils()
        self.grade = Catego()
        self.query = DataFrameQueryBuilder()
        self.direct = Directory()

    def set_line(self, line):
        if isinstance(line, int):
            self.line = line
        else:
            self.line = int(line)

        self.db = DataBase(self.line)
        return self

    def get_line(self):
        if hasattr(self, "line"):
            return self.line
        else:
            raise Exception("rollen object doesn't have line attr")
