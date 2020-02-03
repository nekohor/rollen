from rollen.dao import CidDao


d = CidDao(1580)

# query = d.get_data_by_dates([20191001, 20191003])

# for result in query:
#     print(result.start_date)
#     print()

query = d.get_data_by_start_end("start_date", [20191001, 20191002])

for result in query:
    print(result.start_date)
