from rollen.database.models import Directory

from rollen.database.models import Temp
from rollen.database.models import Excel
from rollen.database.models import Cid

from rollen.database.models import Chem
from rollen.database.models import NonC41
from rollen.database.models import ShiftBlock
from rollen.database.models import Evaluate

from rollen.database import DataBaseManager
from rollen.config.millline import MILLLINE_LIST


def create_all_tables():

    for line in MILLLINE_LIST:

        engine = DataBaseManager.get_database("ledger")[line]

        Directory.metadata.create_all(engine)

        Cid.metadata.create_all(engine)
        Excel.metadata.create_all(engine)
        Temp.metadata.create_all(engine)

        Evaluate.metadata.create_all(engine)
        NonC41.metadata.create_all(engine)
        ShiftBlock.metadata.create_all(engine)
        Chem.metadata.create_all(engine)
