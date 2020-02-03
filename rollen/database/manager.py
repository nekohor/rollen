import cx_Oracle
from sqlalchemy import create_engine

from rollen.config.millline import LINE2250
from rollen.config.millline import LINE1580


class DataBaseManager:

    @classmethod
    def get_database(cls, db_tag):

        if not hasattr(cls, db_tag):
            cls.build_database(db_tag)

        return getattr(cls, db_tag)

    @classmethod
    def get_mes_database(cls):
        return DataBaseManager.get_database("mes")

    @classmethod
    def get_qms_database(cls):
        return DataBaseManager.get_database("qms")

    @classmethod
    def get_ledger_database(cls, line):
        return DataBaseManager.get_database("ledger")[str(line)]

    @classmethod
    def build_database(cls, db_tag):
        setattr(
            cls,
            db_tag,
            getattr(
                cls,
                "build_{}_database".format(db_tag)
            )()
        )

    @classmethod
    def build_mes_database(cls):
        conn = cx_Oracle.connect("hrmmes", "hrmmes", "172.25.12.7/hrmcrm")
        return conn

    @classmethod
    def build_qms_database(cls):
        conn = cx_Oracle.connect("qms", "system", "172.27.36.1/qmsdb")
        return conn

    @classmethod
    def build_pond_database(cls):

        address = "192.168.88.158"
        port = 3306
        user = "root"
        password = ""

        db_name = "pond"
        charset = "utf8mb4"

        # 将数据写入mysql的数据库，
        # 但需要先通过sqlalchemy.create_engine建立连接,
        # 且字符编码设置为utf8mb4，否则有些latin字符不能处理
        engine = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}?charset={}'
            .format(user, password, address, port, db_name, charset)
        )

        return engine

    @classmethod
    def build_ledger_database(cls):

        address = "localhost"
        port = 3306
        user = "root"
        password = ""

        db_name = "coil_{}"
        charset = "utf8mb4"

        # 将数据写入mysql的数据库，
        # 但需要先通过sqlalchemy.create_engine建立连接,
        # 且字符编码设置为utf8mb4，否则有些latin字符不能处理
        engines = {}
        engines[LINE2250] = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}?charset={}'
            .format(
                user,
                password,
                address,
                port,
                db_name.format(LINE2250),
                charset
            )
        )

        engines[LINE1580] = create_engine(
            'mysql+pymysql://{}:{}@{}:{}/{}?charset={}'
            .format(
                user,
                password,
                address,
                port,
                db_name.format(LINE1580),
                charset
            )
        )

        return engines

    @classmethod
    def remove_dupilicates(cls, line, db_tag, table_name):

        if line is None:
            conn = cls.get_database(db_tag)
        else:
            conn = cls.get_database(db_tag)[str(line)].connect()

        temp_table_name = "tmp_tbl_for_removing_dupilicates"

        cursor = conn.cursor()
        cursor.execute("DROP TABLE IF EXISTS tmp_table")
        cursor.execute("create table {} as SELECT ".format(temp_table_name) +
                       "DISTINCT * FROM {}".format(table_name))
        cursor.execute("DROP TABLE IF EXISTS {}".format(table_name))
        cursor.execute("RENAME TABLE {} TO {}".format(
            temp_table_name, table_name))
        cursor.close()
