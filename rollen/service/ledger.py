from rollen.domain.ledger import LedgerReader
from rollen.dao import LedgerDao
import logging
import os

logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)


class LedgerService():

    def __init__(self, lines, tables, months):
        self.lines = lines
        self.tables = tables
        self.months = months

    def batch_insert(self):
        """
            line  eg. "2250" as string
            month eg. 201901 as int
            model from rollen.database.models as sqlalchemy::Base
        """
        self.check_files_exist()
        for line in self.lines:
            for table in self.tables:
                for month in self.months:
                    d = LedgerDao(line, table, month)
                    d.insert_data()

    def check_files_exist(self):
        not_exist_files = []
        for line in self.lines:
            for table in self.tables:
                for month in self.months:
                    reader = LedgerReader(line, table, month)
                    file_name = reader.get_file_name()

                    if not reader.is_file_exists():
                        not_exist_files.append(file_name)

        if len(not_exist_files) > 0:
            raise Exception("{} not exist!".format(not_exist_files))
