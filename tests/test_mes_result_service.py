from rollen.service import ResultService


s = ResultService()

dates = [20200201, 20200218]
data = s.get_data_by_dates(1580, dates)

# data.
print(data)
print(data.index)
data.to_excel("d:/tmp/test_result_result.xlsx")
