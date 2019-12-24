import os

from sqlalchemy.orm import sessionmaker

from rollen.database import DataBaseManager
from rollen.utils.millline import MillLine

from rollen.database.models.directory import Directory


class DirectoryDao():

    def __init__(self, line):

        self.line = str(line)
        self.engine = DataBaseManager.get_database("coil")[self.line]

    def sync_table_with_date(self, current_date):

        if type(current_date) != str:
            current_date_str = str(current_date)
        else:
            current_date_str = current_date

        month = current_date_str[:6]
        date = current_date_str

        root_dir = MillLine.get_pond_root_dir(self.line)
        cur_dir = root_dir + "/{}/{}".format(month, date)
        header = MillLine.get_coil_id_header(self.line)

        coil_ids = [x for x in os.listdir(cur_dir) if x[0] == header]

        self.insert_data(current_date, coil_ids)

    def insert_data(self, current_date, coil_ids):

        Session = sessionmaker(bind=self.engine)
        session = Session()

        data_list = [
            Directory(
                coil_num=int(coil_id[1:-1]),
                coil_id=coil_id,
                pond_date=int(current_date)
            )
            for coil_id in coil_ids
        ]

        session.add_all(data_list)
        session.commit()
        session.close()