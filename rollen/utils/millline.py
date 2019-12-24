from rollen.config.millline import HRM1580_POND_ROOT_DIR
from rollen.config.millline import HRM2250_POND_ROOT_DIR
from rollen.config.millline import LINE2250
from rollen.config.millline import LINE1580
from rollen.config.millline import HRM2250_COILID_HEADER
from rollen.config.millline import HRM1580_COILID_HEADER


class WrongMillLineError(Exception):
    pass


class MillLine():

    @classmethod
    def get_coil_id_header(cls, line):

        if line == LINE2250:
            return HRM2250_COILID_HEADER
        if line == LINE1580:
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

    @classmethod
    def get_pond_root_dir(cls, line):

        if line == LINE2250:
            return HRM2250_POND_ROOT_DIR
        if line == LINE1580:
            return HRM1580_POND_ROOT_DIR

        raise WrongMillLineError("line_tag matches wrong for pond root dir")
