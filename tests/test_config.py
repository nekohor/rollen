from rollen import config
import logging
logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)


def test_get_dirs():
    logging.info(config.get_module_dir("db"))
