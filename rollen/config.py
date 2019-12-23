
def get_prod_data_dir(frequency, line, table_name):
    return "D:/prod_data/ledger_{}/{}/{}".format(frequency, line, table_name)


def get_data_collection_dir(frequency):
    return "D:/data_collection_{}".format(frequency)


def get_intermediate_dir():
    return "D:/prod_data/intermediate"


def get_library_name():
    return "rollen"


def get_library_dir():
    return "D:/NutCloudSync/code/rollen"


def get_module_dir(sub_module):
    module_dir = get_library_dir() + "/" + get_library_name()
    return module_dir + "/" + sub_module


def get_log_pattern_dir(line):
    return get_module_dir("parser") + "/log/pattern/{}".format(line)
