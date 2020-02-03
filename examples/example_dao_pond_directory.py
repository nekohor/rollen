from rollen.dao import DirectoryDao


lines = [1580]
for line in lines:

    d = DirectoryDao("hrm{}".format(line))
    d.sync_table_with_date(20190305)
