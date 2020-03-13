import pandas as pd
from rollen.utils import DirectoryUtils


class SteelGradeCatego():

    def __init__(self):
        self.df_catego = pd.read_excel(
            DirectoryUtils.get_module_dir("domain.grade") +
            "/steel_grade_categos.xlsx")
        self.df_catego.index = self.df_catego["steel_grade"]

    def get_all_steel_grades(self):
        return self.df_catego["steel_grade"]

    def select(self, df, grade_categos, level_num, grade_col="steel_grade"):

        catego_col = "catego{}".format(level_num)
        select_catego_cond = self.df_catego[catego_col].isin(grade_categos)
        steel_grades = self.df_catego.loc[select_catego_cond]["steel_grade"]
        return df.loc[df[grade_col].isin(steel_grades)]

    def get_categos(self, grade_series, level_num, grade_col="steel_grade"):
        max_num = grade_series.shape[0]
        catego_series = pd.Series(index=range(max_num))
        catego_col = "catego{}".format(level_num)
        i = 0
        for grade in grade_series:
            if grade in self.df_catego["steel_grade"]:
                catego_series[i] = self.df_catego.loc[grade, catego_col]
            i = i + 1
        return catego_series
