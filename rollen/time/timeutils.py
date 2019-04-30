

class TimeUtils():

    def __init__(self):
        pass

    def get_year(self, month_date):
        """
        IN  month : int
        """
        return month_date // 100

    def get_month(self, month_date):

        return month_date % 100

    def get_month_dates(self, start, end):
        if isinstance(start, int):
            pass
        else:
            raise Exception("wrong type of start month date")

        if isinstance(end, int):
            pass
        else:
            raise Exception("wrong type of end month date")

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
