from rollen.domain.ledger import LedgerReader
import logging
import os

logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)


class DatabaseInsertionService():

    def __init__(self, lines, tables, months):
        self.lines = lines
        self.tables = tables
        self.months = months

    def batch_insert(self):
        """
            line  eg. 2250 as int
            month eg. 201901 as int
            model from rollen.database.models as sqlalchemy::Base
        """
        self.check_files_exist()
        self.insert_data()
        for line in self.lines:
            for table in self.tables:
                for month in self.months:

    def check_files_exist(self):
        not_exist_files = []
        for line in self.lines:
            for table in self.tables:
                for month in self.months:
                    reader = LedgerReader(line, table)
                    file_name = reader.get_file_name(month)

                    if not os.path.exists(file_name):
                        not_exist_files.append(file_name)

        if len(not_exist_files) > 0:
            raise Exception("{} not exist!".format(not_exist_files))

    def insert_data(self):
        pass
