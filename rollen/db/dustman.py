import pandas as pd


class DustMan():

    def __init__(self, line):
        self.line = line

    def clean_data(self, table_name, df):
        return getattr(self, "clean_{}_data".format(table_name))(df)

    def clean_evaluate_data(self, df):
        df["CoilID"] = df["CoilID"].map(lambda x: x.strip())
        df["AlloyName"] = df["AlloyName"].map(lambda x: x.strip())

        df["coil_id"] = df["CoilID"]
        df["steel_grade"] = df["AlloyName"]
        df["aim_thick"] = df["NomThick"]
        df["aim_width"] = df["NomWidth"]
        df["aim_crown"] = df["TargetCrown"]
        df["datetime"] = df["EndTime"]

        if 2250 == self.line:
            df["steel_grade"] = [
                ("MR" + x.strip()) if len(x) == 8 else x
                for x in df["steel_grade"]]
        else:
            pass
        return df

    def clean_temp_data(self, df):
        df["coil_id"] = df["热卷号"] = df["卷号"]
        df["aim_fdt"] = df["轧机出口目标温度"]
        df["aim_ct"] = df["热卷卷曲目标温度"]
        df["fdt_percent"] = df["出口温度公差比"]
        df["ct_percent"] = df["卷取温度公差比"]
        df["datetime"] = df["板坯出炉时间"]
        return df

    def clean_excel_data(self, df):
        df["coil_id"] = df["热卷号"]
        df["start_date"] = df["开始日期"]
        df["datetime"] = df["结束日期"].apply(lambda x: x + " ") + df["结束时间"]
        df["steel_grade"] = df["钢种"]
        df["coil_len"] = df["热卷长度"]
        df["aim_thick"] = df["目标厚度"]
        df["aim_width"] = df["目标宽度"]
        df["aim_crown"] = df["目标凸度"]
        return df

    def clean_cid_data(self, df):
        return df

    def clean_nonC41_data(self, df):
        df["coil_id"] = df["卷号"]
        df["datetime"] = df["生产时间"]
        return df

    def clean_great_stat_data(self, df):
        df["coil_id"] = df.index
        return df

    def clean_performance_components_data(self, df):
        df["coil_id"] = df["批号"]
        df["steel_grade"] = df["计划牌号"]
        df["weight"] = df["重量"]
        df["block_reason"] = df["初验不合格项"]
        df["yield_date"] = df["生产日期"]
        return df

    def clean_act_block_data(self, df):
        if 1580 == self.line:
            df["自动封闭原因"] = df["L3自动封闭情况"]
            df["分厂反馈信息"] = df["轧机反馈信息"]
            df["缺陷"] = df["主要表面缺陷类别"]
            df["缺陷描述"] = df["表面缺陷描述"]
            df["当班判定意见"] = df["表面质量判定结果"]
            df["白班判定意见"] = df["质检评定意见"]
        elif 2250 == self.line:
            df["实际重量"] = df["实际重量（吨）"]
        else:
            raise Exception("wrong mill line")
        df["coil_id"] = df["卷号"]
        df["steel_grade"] = df["钢种"]
        df["slab_weight"] = df["板坯重量"]
        df["act_weight"] = df["实际重量"].apply(pd.to_numeric, errors='coerce')
        df["start_date"] = df["开始日期"]
        df["block_reason"] = df["缺陷描述"].apply(lambda x: str(x))
        df["block_state"] = df["当班判定意见"].apply(lambda x: str(x))
        return df

    def clean_shift_block_data(self, df):
        df["coil_id"] = df["钢卷号"]
        df["steel_grade"] = df["钢种"]
        df["weight"] = df["重量(t)"]
        df["block_state"] = df["判定情况"].apply(lambda x: str(x))
        df = df.loc[df["钢种"] != "钢种"]
        return df
