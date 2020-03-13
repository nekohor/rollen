import numpy as np
import pandas as pd

import rollen
from rollen.config.millline import MILLLINES
from rollen.service import ResultService
from rollen.domain.grade import SteelGradeCatego


def get_all_data(start_date, end_date):
    df = pd.DataFrame()
    s = ResultService()
    for line in MILLLINES:
        dates = [start_date, end_date]
        data = s.get_data_by_dates(line, dates)
        df = df.append(data)
    return df


start_date = 20200101
end_date = 20200229

df = get_all_data(start_date, end_date)
df.drop_duplicates("steel_grade", "last", inplace=True)

grade = SteelGradeCatego()
all_grades = grade.get_all_steel_grades()
res = df.loc[~df["steel_grade"].isin(all_grades)][
    ["steel_grade", "start_date", "line"]]
res.to_excel("new_grades.xlsx")
