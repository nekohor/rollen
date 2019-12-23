import rollen
import time

line = 1580
start_mdate = 201901
end_mdate = 201911
# table_name = "shift_block"
# table_name = "evaluate"
table_name = "cid"

rln = rollen.roll(line)
mdates = rln.time.get_month_dates(start_mdate, end_mdate)
time_tick = time.strftime("%Y%m%d%H%M%S", time.localtime())

# df = rln.db.table(table_name).where("month", "in", mdates).get()
# df = rln.db.table(table_name).where("coil_id", "re",
#                                     "MGW").where("month", "in", mdates).get()
df = rln.db.table(table_name
                  ).where("steel_grade", "re", "^MGW"
                          ).where("month", "in", mdates).get()

# df = rln.db.table(table_name
#                   ).where("slab_grade", "=", "MBTLA33001"
#                           ).where("month", "in", mdates).get()

df.to_excel("D:/work/query_db/{}_{}_result_{}.xlsx".format(
    line, table_name, time_tick))
