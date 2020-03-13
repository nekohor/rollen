from rollen.service import ResultService

line = 1580
dates = [20190101, 20191231]

s = ResultService()
data = s.get_data_by_dates(line, dates)

# data.
print(data)
print(data.index)
data.to_excel(
    "d:/tmp/test_result_{}_{}_{}.xlsx".format(line, dates[0], dates[-1]))
