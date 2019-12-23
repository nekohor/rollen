import pandas as pd
from rollen import config


class Catego():

    def __init__(self):
        self.catego_df = pd.read_excel(
            config.get_module_dir("grade") +
            "/grade_categorization.xlsx")
        self.hash_df = self.get_hash_df()

    def get_categos(self):
        """细分的冷基排在右边"""
        return self.catego_df.columns

    def get_hash_df(self):
        hash_df = pd.DataFrame()
        for catego in self.get_categos():
            for grade in self.catego_df[catego]:
                hash_df.loc[grade, "catego"] = catego
        return hash_df

    def get_custom_categos(self, tag):
        categos = []
        if tag == "狭义冷基" or tag == "冷轧基料":
            categos = ["普通冷基", "高强冷基", "搪瓷钢", "IF钢", "低合金钢", "磷强化钢"]
        elif tag == "广义冷基":
            categos = ["普通冷基", "高强冷基", "搪瓷钢", "IF钢", "低合金钢", "磷强化钢", "商品材冷基"]
        elif tag == "高档冷基":
            # 注意为板坯钢种划分
            categos = ["汽车面板", "先进高强汽车用钢", "高端家电用钢"]
        elif tag == "无取向硅钢":
            categos = ["低牌号硅钢", "高牌号硅钢"]
        elif tag == "全硅钢":
            categos = ["低牌号硅钢", "高牌号硅钢", "取向硅钢"]
        elif tag == "狭义商品材":
            categos = ["普通商品材", "高强商品材"]
        elif tag == "广义商品材" or tag == "商品材":
            categos = ["普通商品材", "高强商品材", "商品材冷基"]
        else:
            if tag in self.get_categos():
                categos = [tag]
            else:
                raise Exception("unknown grade tag")

        return categos

    def get_custom_grades(self, specific_grades):
        return self.catego_df[
            self.get_custom_categos(specific_grades)
        ].values.reshape(-1)

    def cut(self, grade_series):
        # 修正grade series的index
        max_num = grade_series.shape[0]
        catego_series = pd.Series(index=range(max_num))
        i = 0
        for grade in grade_series:
            if grade in self.hash_df.index:
                catego_series[i] = self.hash_df.loc[grade, "catego"]
            i = i + 1
        return catego_series

    def select(self, df, grade_col, specific_grades):
        grade_list = []
        if isinstance(specific_grades, list):
            grade_list = specific_grades
        elif isinstance(specific_grades, str):
            if specific_grades == "全钢种":
                return df
            else:
                grade_list = self.get_custom_grades(specific_grades)
        else:
            raise Exception("specific_grades type unknown")
        return df.loc[df[grade_col].isin(grade_list)]

    def get_default_grade_col(self, tag):
        if tag in ["高档冷基", "汽车面板", "先进高强汽车用钢", "高端家电用钢"]:
            return "slab_grade"
        else:
            return "steel_grade"
