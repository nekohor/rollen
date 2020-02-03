from rollen.database import QueryBuilder
import datetime


db_type = "ledger"
line = 2250
table_name = "excel"


start_date = 20191201
end_date = 20191231


def query():

    q = QueryBuilder(db_type)
    q.millline(line).table(table_name)
    q.where(
        [
            ['start_date', '>=', start_date],
            ['start_date', '<=', end_date],
            ['slab_grade', "regexp", "345"]
        ]
    )
    df = q.get()

    root_dir = "e:/query_result"
    time_tag = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = "/query_{}_{}_{}_{}_{}.xlsx".format(
        line, table_name, start_date, end_date, time_tag)
    df.to_excel(root_dir + "/" + filename)


if __name__ == '__main__':
    query()
