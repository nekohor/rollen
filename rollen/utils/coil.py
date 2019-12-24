from rollen.config.millline import LINE2250
from rollen.config.millline import LINE1580
from rollen.config.millline import HRM2250_COILID_HEADER
from rollen.config.millline import HRM1580_COILID_HEADER

from rollen.error import WrongMillLineError


class CoilUtils():

    @classmethod
    def get_coil_id_header(cls, line):

        if str(line) == LINE2250:
            return HRM2250_COILID_HEADER
        if str(line) == LINE1580:
            return HRM1580_COILID_HEADER

        raise WrongMillLineError(
            "line_tag matches wrong in get_coil_id_header")

    @classmethod
    def get_line_by_id(cls, coil_id):

        if type(coil_id) != str:
            raise WrongMillLineError("coilId is not a string")

        coil_id_header = coil_id[0]

        if coil_id_header == HRM2250_COILID_HEADER:
            return LINE2250
        if coil_id_header == HRM1580_COILID_HEADER:
            return LINE1580

        raise WrongMillLineError("line_tag matches wrong in get_line_by_id")
