from rollen.database import QueryBuilder
from rollen.utils import TimeUtils
from rollen.domain.grade import Catego
from rollen.utils import DirectoryUtils


class Roller():

    def __init__(self):

        self.time = TimeUtils
        self.directory = DirectoryUtils

        self.db = QueryBuilder("ledger")

        self.grade = Catego()
