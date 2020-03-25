from rollen.service import ResultService


# line = 1580
line = 2250

# dates = [20200229, 20200229]
dates = [20191101, 20200324]
# dates = [20200211, 20200211]
# dates = [20191209153000, 20191209193000]

s = ResultService()
data = s.get_data_by_dates(line, dates)


result_filename = (
    "d:/tmp/mes_result_{}_{}_{}.xlsx".format(
        line, dates[0], dates[-1]
    )
)
data.to_excel(result_filename)
