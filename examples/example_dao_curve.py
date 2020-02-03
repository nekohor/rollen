from rollen.database import DataBaseManager
from rollen.dao import CurveDao


dao = CurveDao()

l = dao.get_data("M19157502W", 'HSM2.WEDGE40')
print(l)
