from dateutil import parser
from datetime import timedelta


class TimeUtils():

    @classmethod
    def get_year(self, month_date):
        """
            month_date : int
        """
        return month_date // 100

    @classmethod
    def get_month(self, month_date):
        """
            month_date : int
        """
        return month_date % 100

    @classmethod
    def get_month_dates(self, start, end):
        """
            start : int
            end   : int
        """
        if isinstance(start, int):
            pass
        else:
            raise Exception("wrong type of start month date")

        if isinstance(end, int):
            pass
        else:
            raise Exception("wrong type of end month date")

        if start == end:
            return [start]
        elif start > end:
            raise Exception("start > end in get_month_dates")
        else:
            pass

        y = start // 100
        m = start % 100
        month_dates = []
        while (y * 100 + m) <= end:
            month_dates.append((y * 100 + m))
            m = m + 1
            if m > 12:
                y = y + 1
                m = 1
        return month_dates

    @classmethod
    def get_dates(cls, start_date, end_date):
        """ return a list of string """

        start_datetime = parser.parse(str(start_date))
        end_datetime = parser.parse(str(end_date))

        days = (end_datetime - start_datetime).days

        dates = []
        for i in range(days + 1):
            current_datetime = start_datetime + timedelta(days=i)
            dates.append(current_datetime.strftime("%Y%m%d"))

        return dates
