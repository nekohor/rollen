import os

from rollen.config.millline import LINE2250
from rollen.config.millline import LINE1580

# from rollen.config.millline import HRM2250_COILID_HEADER
# from rollen.config.millline import HRM1580_COILID_HEADER

from rollen.config.millline import HRM2250_POND_ROOT_DIR
from rollen.config.millline import HRM1580_POND_ROOT_DIR

from rollen.error import WrongMillLineError


class DirectoryUtils():

    @classmethod
    def mkdir(cls, dir_name):
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

    @classmethod
    def get_base_dir(cls):
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
    def get_lib_root_dir(cls):
        return "D:/NutCloudSync/code"

    @classmethod
    def get_lib_name(cls):
        return "rollen"

    @classmethod
    def get_lib_dir(cls):
        return cls.get_lib_root_dir() + "/" + "rollen"

    @classmethod
    def get_lib_cfg_dir(cls):
        return cls.get_lib_dir() + "/" + "config"

    @classmethod
    def get_toml_cfg_dir(cls):
        return cls.get_lib_root_dir() + "/Statistician/config"

    @classmethod
    def get_tasks_dir(cls):
        return cls.get_lib_root_dir() + "/pondo/tasks"

    @classmethod
    def get_module_dir(cls, module):
        module_root_dir = cls.get_lib_dir() + "/" + cls.get_lib_name()
        module_relative_path = module.split(".")
        return module_root_dir + "/" + "/".join(module_relative_path)

    @classmethod
    def get_pond_root_dir(cls, line):

        if str(line) == LINE2250:
            return HRM2250_POND_ROOT_DIR
        if str(line) == LINE1580:
            return HRM1580_POND_ROOT_DIR

        raise WrongMillLineError("line_tag matches wrong for pond root dir")

    @classmethod
    def get_pond_date_dir(cls, line, date):

        current_date = str(date)

        date_dir = "{}/{}/{}".format(
            cls.get_pond_root_dir(line),
            current_date[:6],
            current_date
        )

        return date_dir

    @classmethod
    def get_pond_date_dirs(cls, line, dates):

        date_dirs = []
        for date in dates:
            cur_dir = cls.get_pond_date_dir(line, date)

            if os.path.exists(cur_dir):
                date_dirs.append(cur_dir)
            else:
                continue

        return date_dirs
