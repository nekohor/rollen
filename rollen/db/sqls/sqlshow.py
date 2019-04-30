with open("excel.sql", encoding="utf-8") as f:
    for statement in f.readlines():
        print(statement)
