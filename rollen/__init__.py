from rollen.database import QueryBuilder
from rollen.utils import TimeUtils
from rollen.domain.grade import Catego
from rollen.utils import DirectoryUtils

time = TimeUtils
directory = DirectoryUtils

db = QueryBuilder("ledger")

grade = Catego()
