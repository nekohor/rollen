from rollen.dao import ResultDao


dao = ResultDao()

cols = dao.get_sql_columns()
print(cols)

data = dao.get_data_by_date(20200202, 20200202)
print(data)
