# encoding='utf-8'
import os
import pandas as pd
import rollen

from rollen.db import insert_cid
from rollen.db import insert_tables


def main():

    tools = rollen.roll()

    start_month_date = 201912
    end_month_date = 201912
    month_dates = tools.time.get_month_dates(
        start_month_date, end_month_date)

    # lines = [2250, 1580]
    # lines = [2250]
    lines = [1580]

    # table_names = ["excel", "temp", "evaluate", "nonC41"]
    # table_names = ["excel", "temp", "shiftblock"]
    # table_names = ["excel", "temp", "evaluate"]
    # table_names = ["excel", "temp"]
    # table_names = ["evaluate"]
    
    table_names = ["shiftblock"]
    insert_tables(lines, month_dates, table_names)

    table_names = ["excel", "temp"]
    insert_tables(lines, month_dates, table_names)
    insert_cid(lines, month_dates)

    # ------------------ 成分性能 ---------------------------
    # year_list = [2018, 2019]
    # table_names = ["chem"]
    # insert_tables(lines, year_list, table_names)


if __name__ == '__main__':
    main()
