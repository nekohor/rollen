import toml
from rollen.utils import DirectoryUtils


class Registry:

    @classmethod
    def get_configs(cls):
        if not hasattr(cls, '_configs'):
            cls._configs = cls.build_configs()
            return cls._configs
        return cls._configs

    @classmethod
    def get_config(cls, key):
        return cls.get_configs()[key]

    @classmethod
    def build_configs(cls):
        configs = {}

        toml_cfg_dir = DirectoryUtils.get_toml_cfg_dir() + "/"

        configs["factors"] = {}
        configs["factors"]["qms"] = toml.load(
            toml_cfg_dir + "factors_qms.toml")
        configs["factors"]["internal"] = toml.load(
            toml_cfg_dir + "factors_internal.toml")

        configs["lengthMode"] = toml.load(
            toml_cfg_dir + "length_division_mode.toml")

        return configs
