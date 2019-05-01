def get_data_collection_dir(tag):
    return "D:/data_collection_{}".format(tag)


def get_library_name():
    return "rollen"


def get_library_dir():
    return "C:/NutCloudSync/code/rollen"


def get_module_dir(sub_module):
    module_dir = get_library_dir() + "/" + get_library_name()
    return module_dir + "/" + sub_module
