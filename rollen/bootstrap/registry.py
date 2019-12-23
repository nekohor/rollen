import toml
from rollen.utils import DirectoryUtils


class Registry:

    @classmethod
    def get_config(cls):
        if not hasattr(cls, '_instance'):
            cls._instance = cls.build_config()
        return cls._instance

    @classmethod
    def build_config(cls):
        configs = {}

        lib_cfg_dir = DirectoryUtils.get_lib_cfg_dir()

        configs["factors"] = {}
        configs["factors"]["qms"] = toml.load(lib_cfg_dir + "factors_qms.toml")

        return configs
