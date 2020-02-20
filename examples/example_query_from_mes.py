from rollen.service import ResultService


line = 2250
dates = [20200201, 20200218]

s = ResultService()
data = s.get_data_by_dates(line, dates)


result_filename = (
    "d:/tmp/mes_result_{}_{}_{}.xlsx".format(
        line, dates[0], dates[-1]
    )
)
data.to_excel(result_filename)
