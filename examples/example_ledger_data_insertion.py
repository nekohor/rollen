import logging

from rollen.service import LedgerService
from rollen.config.millline import MILLLINES
from rollen.config.millline import LINE2250
from rollen.config.millline import LINE1580
from rollen.utils import TimeUtils

logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)


start_month_date = 202003
end_month_date = 202003

# table_names = ["excel", "temp", "cid", "shiftblock"]
table_names = ["shiftblock"]

lines = [LINE1580]
# lines = [LINE2250]


# start_month_date = 201910
# end_month_date = 201912

# table_names = ["excel", "temp", "cid"]

# lines = [LINE2250]


def insert_into_database():

    month_dates = (
        TimeUtils.get_month_dates(start_month_date, end_month_date)
    )
    logging.info(month_dates)

    service = LedgerService(lines, table_names, month_dates)
    service.batch_insert()


insert_into_database()
