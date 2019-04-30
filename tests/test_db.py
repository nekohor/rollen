from rollen.db import check_files_exist
from rollen.db import remove_all_dupilicates
import rollen
import logging
logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)


def test_check_files_exist():
    line_list = [2250, 1580]
    tools = rollen.roll()
    month_date_list = tools.time.get_month_dates(201701, 201803)
    table_name_list = ["excel", "temp"]
    check_files_exist(line_list, month_date_list, table_name_list)


def test_remove_all_duplicates():
    line_list = [1580]
    table_name_list = ["cid"]
    remove_all_dupilicates(line_list, table_name_list)


if __name__ == '__main__':
    main()
