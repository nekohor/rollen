from rollen.database import QueryBuilder
from rollen.utils import TimeUtils
from rollen.domain.grade import Catego
from rollen.utils import DirectoryUtils
from rollen.bootstrap import Registry

time = TimeUtils()
directory = DirectoryUtils()
grade = Catego()
db = QueryBuilder("ledger")

registry = Registry()
