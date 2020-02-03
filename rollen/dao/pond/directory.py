
from sqlalchemy.orm import sessionmaker

from rollen.database import DataBaseManager
from rollen.database.models import Directory


class DirectoryDao():

    def __init__(self, line):

        self.line = str(line)
        self.engine = DataBaseManager.get_database("ledger")[self.line]
        self.DBSession = sessionmaker(bind=self.engine)

    def insert_data(self, current_date, coil_ids):

        session = self.DBSession()

        data_list = [
            Directory(
                coil_id=coil_id,
                start_date=str(current_date)
            )
            for coil_id in coil_ids
        ]

        session.add_all(data_list)
        session.commit()
        session.close()

    def get_data_by_start_end(self, field_name, arrays):

        session = self.DBSession()

        start = arrays[0]
        end = arrays[-1]

        query = session.query(Directory).filter(
            getattr(Directory, field_name) >= start,
            getattr(Directory, field_name) <= end
        )
        session.close()

        return query

    def get_data_in_arrays(self, field_name, arrays):

        session = self.DBSession()
        query = session.query(Directory).filter(
            getattr(Directory, field_name).in_(arrays)
        )
        session.close()

        return query
