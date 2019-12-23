import os
import logging
import rollen
import pandas as pd
from .insertion import Insertion
from .cidbuilder import CidBuilder
from .tablebuilder import TableBuilder

logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)


def check_files_exist(line_list, month_date_list, table_name_list):
    not_exist_list = []
    for line in line_list:
        rln = rollen.roll(line)
        for month_date in month_date_list:
            for table_name in table_name_list:
                insertion = Insertion(rln, table_name)
                file_name = insertion.get_file_name(month_date)
                logging.info(file_name)
                if os.path.exists(file_name):
                    pass
                else:
                    not_exist = "{} {} {}".format(line, month_date, table_name)
                    not_exist_list.append(not_exist)
    if not_exist_list:
        logging.info(not_exist_list)
        raise Exception(
            "{} file(s) do(es) not exist!".format(len(not_exist_list)))
    else:
        logging.info("all files exist!")


def insert_into_database(line_list, month_date_list, table_name_list):
    for line in line_list:
        rln = rollen.roll(line)
        for month_date in month_date_list:
            for table_name in table_name_list:

                # insertion = Insertion(rln, table_name)
                # insertion.insert(month_date)

                tber = TableBuilder(rln, table_name)
                tber.insert(month_date)



def drop_all_tables(line_list, table_name_list):
    for line in line_list:
        rln = rollen.roll(line)
        for table_name in table_name_list:
            rln.db.drop(table_name)
            logging.info("drop done! {} {}".format(line, table_name))
        rln.db.conn.close()


def remove_all_dupilicates(line_list, table_name_list):
    for line in line_list:
        rln = rollen.roll(line)
        for table_name in table_name_list:
            rln.db.remove_dupilicates(table_name)
            logging.info("remove dups done! {} {}".format(line, table_name))
        rln.db.conn.close()


def insert_tables(lines, dates_list, table_names):
    """dates_list may be month_dates_lsit or year_dates_list"""
    check_files_exist(lines, dates_list, table_names)
    insert_into_database(lines, dates_list, table_names)
    # remove_all_dupilicates(lines, table_names)


def insert_cid(lines, month_dates):

    check_files_exist(lines, month_dates, ["excel", "temp"])
    for line in lines:
        for month_date in month_dates:

            rln = rollen.roll(line)

            cider = CidBuilder(rln)
            cider.merge(month_date)
            cider.to_excel(month_date)
            cider.insert()

            logging.info("complete insert cid {} {}".format(line, month_date))
