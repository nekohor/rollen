from rollen.dao import ResultDao


dao = ResultDao()

cols = dao.get_sql_columns()
print(cols)

data = dao.get_data_by_date(20200101, 20200103)

# data.
print(data)
data.to_excel("d:/tmp/test_result_dao.xlsx")
