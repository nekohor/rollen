import os
import logging
import rollen
import pandas as pd
from .insertion import Insertion

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
                insertion = Insertion(rln, table_name)
                insertion.insert(month_date)


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


def formal_insert(lines, month_dates, table_names):
    check_files_exist(lines, month_dates, table_names)
    insert_into_database(lines, month_dates, table_names)
    remove_all_dupilicates(lines, table_names)


def merge_for_cid(lines, month_dates):
    table_names = ["temp", "excel"]
    check_files_exist(lines, month_dates, table_names)
    for line in lines:
        rln = rollen.roll(line)
        for month_date in month_dates:
            logging.info("start merge! {} {}".format(line, month_date))
            ins_excel = Insertion(rln, "excel")
            ins_temp = Insertion(rln, "temp")

            df_excel = ins_excel.read_data(month_date)
            df_temp = ins_temp.read_data(month_date)

            need_cols_in_excel = [
                "coil_id",
                "start_date",
                "datetime",
                "steel_grade",
                "coil_len",
                "aim_thick",
                "aim_width",
                "aim_crown"
            ]
            need_cols_in_temp = [
                "coil_id",
                "aim_fdt",
                "aim_ct"
            ]

            df_cid = pd.merge(
                df_excel[need_cols_in_excel],
                df_temp[need_cols_in_temp],
                how='left',
                on="coil_id"
            )

            df_cid.to_excel(
                Insertion(rln, "cid").get_file_name(month_date)
            )
            logging.info("complete merge! {} {}".format(line, month_date))
