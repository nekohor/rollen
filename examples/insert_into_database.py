# encoding='utf-8'
import os
import pandas as pd
import rollen

from rollen.db import merge_for_cid
from rollen.db import formal_insert


def main():

    tools = rollen.roll()

    start_month_date = 201901
    end_month_date = 201904
    month_dates = tools.time.get_month_dates(
        start_month_date,
        end_month_date
    )

    # lines = [2250, 1580]
    # lines = [2250]
    lines = [1580]

    table_names = ["excel", "evaluate", "temp", "nonC41", "cid"]
    table_names = ["excel", "temp", "cid"]

    table_names = ["shift_block"]

    # merge_for_cid(lines, month_dates)
    formal_insert(lines, month_dates, table_names)

    # 成分性能
    year_list = [2018, 2019]
    table_names = ["performance_components"]
    formal_insert(lines, year_list, table_names)


if __name__ == '__main__':
    main()
