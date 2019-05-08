# encoding='utf-8'
import os
import pandas as pd
import rollen

from rollen.db import merge_for_cid
from rollen.db import formal_insert


def main():

    tools = rollen.roll()

    start_month_date = 201904
    end_month_date = 201904
    month_dates = tools.time.get_month_dates(
        start_month_date,
        end_month_date
    )

    lines = [2250, 1580]
    lines = [2250]
    # lines = [1580]

    table_names = ["excel", "evaluate", "temp", "nonC41", "cid"]
    # item_list = ["excel", "temp", "nonC41"]
    table_names = ["excel", "temp", "cid"]
    # item_list = ["excel", "evaluate", "temp", "nonC41"]
    # item_list = ["cid"]
    # item_list = ["great_stat"]
    # item_list = ["shift_block"]
    # item_list = ["act_block"]

    merge_for_cid(lines, month_dates)
    formal_insert(lines, month_dates, table_names)

    # 成分性能
    # year_list = [2018, 2019]
    # table_names = ["performance_components"]
    # formal_insert(lines, year_list, table_names)


if __name__ == '__main__':
    main()
