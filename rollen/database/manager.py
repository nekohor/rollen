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
    def build_qms_database(cls):
        conn = cx_Oracle.connect("qms", "system", "172.27.36.1/qmsdb")
        return conn

    @classmethod
    def build_pond_database(cls):

        address = "localhost"
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
