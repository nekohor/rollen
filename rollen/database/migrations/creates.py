from rollen.database.models import Directory
from rollen.database.models import Chem
from rollen.database.models import NonC41
from rollen.database.models import ShiftBlock
from rollen.database.models import Evaluate
from rollen.database.models import Temp
from rollen.database.models import Excel
from rollen.database.models import Cid

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from rollen.database import DataBaseManager
from rollen.config.millline import HRM_TAG_LIST


def create_all_tables():

    for line_tag in HRM_TAG_LIST:

        engine = DataBaseManager.get_database("ledger")[line_tag]

        Directory.metadata.create_all(engine)

        Cid.metadata.create_all(engine)

        Excel.metadata.create_all(engine)
        Temp.metadata.create_all(engine)
