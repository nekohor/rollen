import logging

from rollen.service import LedgerService
from rollen.config.millline import MILLLINES
from rollen.config.millline import LINE2250
from rollen.config.millline import LINE1580
from rollen.utils import TimeUtils

start_month_date = 201701
end_month_date = 201911

table_names = ["nonC41"]

lines = [LINE1580]


def insert_into_database():

    month_dates = (
        TimeUtils.get_month_dates(start_month_date, end_month_date)
    )
    logging.info(month_dates)

    service = LedgerService(lines, table_names, month_dates)
    service.batch_insert()


insert_into_database()
