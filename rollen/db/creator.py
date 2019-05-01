from rollen import config
import os


class Creator():

    def __init__(self):
        self.sqls_dir = config.get_module_dir("db") + "/sqls"
        # self.table_names = ["excel", "temp", "cid", "nonC41", "evaluate"]

    def create(self, conn, table_name):
        sql_file_path = self.sqls_dir + "/{}.sql".format(table_name)

        if os.path.exists(sql_file_path):
            pass
        else:
            raise Exception("{}.sql does not exist".format(table_name))

        cursor = conn.cursor()
        with open(sql_file_path, encoding="utf-8") as f:
            for statement in f.readlines():
                cursor.execute(statement)
