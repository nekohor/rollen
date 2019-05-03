import rollen


rln = rollen.roll(1580)


df = rln.db.table("cid").where("month", "in", [201902, 201903]).get()

df.to_excel("D:/Work/query_db/result.xlsx")
