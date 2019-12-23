import os

from rollen.config.millline import HRM2250_TAG
from rollen.config.millline import HRM1580_TAG
from rollen.config.millline import HRM2250_COILID_HEADER
from rollen.config.millline import HRM1580_COILID_HEADER

from rollen.config.millline import HRM2250_POND_ROOT_DIR
from rollen.config.millline import HRM1580_POND_ROOT_DIR

from rollen.error import WrongMillLineError


class DirectoryUtils():

    @classmethod
    def mkdir(cls, self, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    @classmethod
    def get_base_dir(cls, self):
        return os.path.dirname(os.path.abspath(__file__))

    @classmethod
    def get_prod_data_dir(cls, frequency, line, table_name):
        return (
            "D:/prod_data/ledger_{}/{}/{}".format(frequency, line, table_name)
        )

    @classmethod
    def get_intermediate_dir(cls):
        return "D:/prod_data/intermediate"

    @classmethod
    def get_lib_name(cls):
        return "rollen"

    @classmethod
    def get_lib_dir(cls):
        return "D:/NutCloudSync/code/rollen"

    @classmethod
    def get_lib_cfg_dir(cls):
        return cls.get_lib_dir() + "/" + "config"

    @classmethod
    def get_module_dir(cls, module):
        module_root_dir = cls.get_lib_dir() + "/" + cls.get_lib_name()
        module_relative_path = module.split(".")
        return module_root_dir + "/" + "/".join(module_relative_path)

    @classmethod
    def get_pond_root_dir(cls, line_tag):

        if line_tag == HRM2250_TAG:
            return HRM2250_POND_ROOT_DIR
        if line_tag == HRM1580_TAG:
            return HRM1580_POND_ROOT_DIR

        raise WrongMillLineError("line_tag matches wrong for pond root dir")
