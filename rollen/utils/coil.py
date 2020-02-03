from rollen.config.millline import LINE2250
from rollen.config.millline import LINE1580
from rollen.config.millline import HRM2250_COILID_HEADER
from rollen.config.millline import HRM1580_COILID_HEADER

from rollen.error import WrongMillLineError

import os


class CoilUtils():

    @classmethod
    def get_coil_ids_in_dir(cls, cur_dir):

        coil_ids = os.listdir(cur_dir)

        return [x for x in coil_ids if os.path.isdir(cur_dir + "/" + x)]
