from rollen.database import DataBaseManager
from rollen.database.models import Cid
from sqlalchemy.orm import sessionmaker


class CidDao():

    def __init__(self, line):

        self.line = str(line)
        self.engine = DataBaseManager.get_ledger_database(self.line)
        self.DBSession = sessionmaker(bind=self.engine)

    def get_data_by_start_end(self, field_name, arrays):

        start = arrays[0]
        end = arrays[-1]

        session = self.DBSession()

        query = session.query(Cid).filter(
            getattr(Cid, field_name) >= start,
            getattr(Cid, field_name) <= end
        )

        session.close()

        return query

    def get_data_in_arrays(self, field_name, arrays):

        session = self.DBSession()
        query = session.query(Cid).filter(
            getattr(Cid, field_name).in_(arrays)
        )
        session.close()

        return query
