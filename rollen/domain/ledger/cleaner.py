import pandas as pd
import numpy as np


class LedgerCleaner():

    def __init__(self, line):
        self.line = line

    def clean_data(self, table_name, df):
        return getattr(self, "clean_{}_data".format(table_name))(df)

    def clean_excel_data(self, df):
        df["coil_id"] = df["热卷号"]
        df["start_date"] = df["开始日期"]
        df["start_time"] = df["开始时间"]
        df["end_date"] = df["结束日期"]
        df["end_time"] = df["结束时间"]
        df["datetime"] = df["结束日期"].apply(
            lambda x: x + " ") + df["结束时间"].apply(lambda x: str(x))
        df["shift"] = df["成品库班次"]
        df["convertor_id"] = df["钢水炉号"]
        df["slab_id"] = df["实际板坯号"]
        df["slab_grade"] = df["板坯钢种"]
        df["slab_weight"] = df["板坯重量"]
        df["coil_weight"] = df["实际重量（吨）"]
        df["specifications"] = df["规格"]
        df["steel_grade"] = df["钢种"]
        df["next_process"] = df["下道工序号"]
        df["last_process"] = df["末道工序号"]
        df["specs_range"] = df["规格范围"]
        df["pack_code"] = df["打包标准代码"]
        df["plan_id"] = df["生产计划号"]
        df["cross_code"] = df["跨号"]
        df["area_code"] = df["库区号"]
        df["line_code"] = df["行号"]
        df["column_code"] = df["列号"]
        df["layer_code"] = df["层次"]
        df["storage_time"] = df["入库时间"]
        df["inner_diam"] = df["内径"]
        df["outside_diam"] = df["外径"]
        df["fce_num"] = df["加热炉"]
        df["dc_num"] = df["卷取机"]
        df["mean_crown"] = df["凸度"]
        df["mean_wedge"] = df["楔形"]
        df["mean_flatness"] = df["平直度"]
        df["theoretical_weight"] = df["理论重量"]
        df["set_thick"] = df["设定厚度"]
        df["mean_fdt"] = df["轧机出口平均温度"]
        df["mean_ct"] = df["平均卷取温度"]
        df["mean_thick"] = df["平均厚度"]
        df["mean_width"] = df["平均宽度"]
        df["coil_len"] = df["热卷长度"]
        df["order_width"] = df["订单宽度"]
        df["slab_id_in_plan"] = df["计划板坯号"]
        df["prod_order"] = df["生产订单号"]
        df["sale_order"] = df["销售订单号"]
        df["sale_item_id"] = df["销售行项目号"]
        df["C_C"] = df["C_C"]
        df["C_Si"] = df["C_Si"]
        df["C_Mn"] = df["C_Mn"]
        df["C_P"] = df["C_P"]
        df["C_S"] = df["C_S"]
        df["C_AL"] = df["C_AL"]
        df["C_ALS"] = df["C_ALS"]
        df["C_O"] = df["C_O"]
        df["C_N"] = df["C_N"]
        df["C_Cr"] = df["C_Cr"]
        df["C_Ni"] = df["C_Ni"]
        df["C_Mo"] = df["C_Mo"]
        df["C_Nb"] = df["C_Nb"]
        df["C_V"] = df["C_V"]
        df["C_Ti"] = df["C_Ti"]
        df["C_Cu"] = df["C_Cu"]
        df["C_Ca"] = df["C_Ca"]
        df["judge_result"] = df["综判结果"]
        df["quality_grade"] = df["质量等级"]
        df["old_steel_grade"] = df["旧钢种"]
        df["old_material_code"] = df["旧物料"]
        df["is_cut_weight"] = df["是否扣重"]
        df["weight_after_deduction"] = df["扣重后重量"]
        df["weight_before_deduction"] = df["扣重前重量"]
        df["material_code"] = df["物料号"]
        df["last_steel_grade"] = df["最终钢种"]
        df["max_width"] = df["宽度最大值"]
        df["min_width"] = df["宽度最小值"]
        df["max_crown"] = df["凸度最大值"]
        df["min_crown"] = df["凸度最小值"]
        df["max_wedge"] = df["楔形最大值"]
        df["min_wedge"] = df["楔形最小值"]
        df["max_flatness"] = df["平直度最大值"]
        df["min_flatness"] = df["平直度最小值"]
        df["max_fdt"] = df["轧机出口温度最大值"]
        df["min_fdt"] = df["轧机出口温度最小值"]
        df["max_ct"] = df["热轧卷取温度最大值"]
        df["min_ct"] = df["热轧卷取温度最小值"]
        df["order_purpose"] = df["订单用途"]
        df["aim_width"] = df["目标宽度"]
        df["max_thick"] = df["厚度最大值"]
        df["min_thick"] = df["厚度最小值"]
        df["SN"] = df["SN"]
        df["storage_num"] = df["库位号"]
        df["aim_thick"] = df["目标厚度"]
        df["aim_crown"] = df["目标凸度"]
        df["is_abnormal"] = df["是否异常"]

        try:
            df["product_type"] = df["产品类型"]
        except:
            df["product_type"] = np.nan

        return df

    def clean_temp_data(self, df):
        df["coil_id"] = df["热卷号"] = df["卷号"]
        df["steel_grade"] = df["钢种"]
        df["aim_thick"] = df["厚度"]
        try:
            df["aim_width"] = df["宽度"]
        except:
            df["aim_width"] = np.nan
        df["mean_fdt"] = df["轧机出口平均温度"]
        df["aim_fdt"] = df["轧机出口目标温度"]
        df["fdt_bias"] = df["轧机出口温度差值"]
        df["mean_ct"] = df["热卷卷曲平均温度"]
        df["aim_ct"] = df["热卷卷曲目标温度"]
        df["ct_bias"] = df["热卷卷曲温度差值"]
        df["act_ht"] = df["板坯平均温度"]
        df["aim_ht"] = df["计划出炉温度"]
        df["ht_bias"] = df["板坯温度差值"]
        df["fdt_perc"] = df["出口温度公差比"]
        df["ct_perc"] = df["卷取温度公差比"]
        df["slab_id"] = df["板坯号"]
        df["extract_time"] = df["板坯出炉时间"].apply(lambda x: str(x))
        df["order_purpose"] = df["订单用途"]
        try:
            df["charge_temp"] = df["板坯入炉温度"]
            df["charge_time"] = df["板坯入炉时间"].apply(lambda x: str(x))
            df["fce_num"] = df["加热炉炉号"]
            df["slab_weight"] = df["板坯重量"]
            df["act_weight"] = df["成品重量"]
        except:
            df["charge_temp"] = np.nan
            df["charge_time"] = np.nan
            df["fce_num"] = np.nan
            df["slab_weight"] = np.nan
            df["act_weight"] = np.nan
        return df

    def clean_cid_data(self, df):
        return df

    def clean_evaluate_data(self, df):
        df["CoilID"] = df["CoilID"].map(lambda x: x.strip())
        df["AlloyName"] = df["AlloyName"].map(lambda x: str(x).strip())

        df["coil_id"] = df["CoilID"]
        df["steel_grade"] = df["AlloyName"]

        if 2250 == self.line:
            df["steel_grade"] = [
                ("MR" + x.strip()) if len(x) == 8 else x
                for x in df["steel_grade"]]
        else:
            pass

        df["aim_thick"] = df["NomThick"]
        df["aim_width"] = df["NomWidth"]
        df["aim_fdt"] = df["NomTemp"]
        df["aim_ct"] = df["NomCTTemp"]
        df["aim_crown"] = df["TargetCrown"]
        df["start_time"] = df["StartTime"].apply(lambda x: str(x))
        df["end_time"] = df["EndTime"].apply(lambda x: str(x))
        df["prof_rate"] = df["ProfileRate"]
        df["size_rate"] = df["SizeRate"]
        df["temp_rate"] = df["TempRate"]
        df["overall_rate"] = df["OverallRate"]
        df["thick_rate"] = df["ThickRate"]
        df["thick_perc"] = df["ThickPerc"]
        df["thick_head_perc"] = df["ThickHeadPerc"]
        df["thick_tail_perc"] = df["ThickTailPerc"]
        df["width_rate"] = df["WidthRate"]
        df["width_perc"] = df["WidthPerc"]
        df["width_head_perc"] = df["WidthHeadPerc"]
        df["width_tail_perc"] = df["WidthTailPerc"]
        df["cw_rate"] = df["CWRate"]
        df["c10_perc"] = df["C10Perc"]
        df["c10_avg"] = df["C10Avg"]
        df["c10_min"] = df["C10Min"]
        df["c10_max"] = df["C10Max"]
        df["c25_perc"] = df["C25Perc"]
        df["c25_avg"] = df["C25Avg"]
        df["c25_min"] = df["C25Min"]
        df["c25_max"] = df["C25Max"]
        df["c40_perc"] = df["C40Perc"]
        df["c40_avg"] = df["C40Avg"]
        df["c40_min"] = df["C40Min"]
        df["c40_max"] = df["C40Max"]
        df["c50_perc"] = df["C50Perc"]
        df["c50_avg"] = df["C50Avg"]
        df["c50_min"] = df["C50Min"]
        df["c50_max"] = df["C50Max"]
        df["c100_perc"] = df["C100Perc"]
        df["c100_avg"] = df["C100Avg"]
        df["c100_min"] = df["C100Min"]
        df["c100_max"] = df["C100Max"]
        df["w10_perc"] = df["W10Perc"]
        df["w10_avg"] = df["W10Avg"]
        df["w10_min"] = df["W10Min"]
        df["w10_max"] = df["W10Max"]
        df["w25_perc"] = df["W25Perc"]
        df["w25_avg"] = df["W25Avg"]
        df["w25_min"] = df["W25Min"]
        df["w25_max"] = df["W25Max"]
        df["w40_perc"] = df["W40Perc"]
        df["w40_avg"] = df["W40Avg"]
        df["w40_min"] = df["W40Min"]
        df["w40_max"] = df["W40Max"]
        df["w50_perc"] = df["W50Perc"]
        df["w50_avg"] = df["W50Avg"]
        df["w50_min"] = df["W50Min"]
        df["w50_max"] = df["W50Max"]
        df["w100_perc"] = df["W100Perc"]
        df["w100_avg"] = df["W100Avg"]
        df["w100_min"] = df["W100Min"]
        df["w100_max"] = df["W100Max"]
        df["flat_rate"] = df["FlatnessRate"]
        df["flat_perc"] = df["FlatnessPerc"]
        df["flat_head_perc"] = df["FlatnessHeadPerc"]
        df["flat_tail_perc"] = df["FlatnessTailPerc"]
        df["fdt_rate"] = df["FDTRate"]
        df["fdt_perc"] = df["FDTPerc"]
        df["fdt_head_perc"] = df["FDTHead"]
        df["fdt_tail_perc"] = df["FDTTail"]
        df["fdt_mid_perc"] = df["FDTMidPerc"]
        df["ct_rate"] = df["CTRate"]
        df["ct_perc"] = df["CTPerc"]
        df["ct_head_perc"] = df["CTHead"]
        df["ct_tail_perc"] = df["CTTail"]
        df["ct_mid_perc"] = df["CTMidPerc"]
        df["rdt_rate"] = df["RDTRate"]
        df["rdt_perc"] = df["RDTPerc"]
        df["rdw_rate"] = df["RDWRate"]
        df["rdw_perc"] = df["RDWPerc"]
        df["fdw_rate"] = df["FDWRate"]
        df["fdw_perc"] = df["FDWPerc"]
        df["tbc_rate"] = df["TBCRate"]
        df["tbc"] = df["TBC"]
        df["si_rate"] = df["SiliconeRate"]
        df["si1_perc"] = df["Si1Perc"]
        df["si2_perc"] = df["Si2Perc"]
        df["si3_perc"] = df["Si3Perc"]
        return df

    def clean_nonC41_data(self, df):
        df["coil_id"] = df["卷号"]
        df["datetime"] = df["生产时间"].apply(lambda x: str(x))
        df["mean_flat"] = df["平直度平均值"]
        df["max_flat"] = df["平直度最大值"]
        df["min_flat"] = df["平直度最小值"]
        df["steel_grade"] = df["钢种"]
        df["mean_width"] = df["平均宽度"]
        df["mean_thick"] = df["平均厚度"]
        df["up_to_standard"] = df["浪形"]
        return df

    def clean_chem_data(self, df):
        df["prod_date"] = df["生产日期"]
        df["slab_id"] = df["原料批号"]
        df["convertor_id"] = df["炉号"]
        df["coil_id"] = df["批号"]
        df["aim_thick"] = df["厚"]
        df["aim_width"] = df["宽"]
        df["steel_grade_in_plan"] = df["计划牌号"]
        df["act_weight"] = df["重量"]
        df["block_reason"] = df["初验不合格项"]
        df["specs"] = df["规格（厚度*宽度）"]
        df["record_man"] = df["登记人"]
        df["test_date"] = df["初验日期"]
        df["yield_strength"] = df["屈服"]
        df["tensile_strength"] = df["抗拉"]
        df["yield_ratio"] = df["屈强比"]
        df["A"] = df["A"]
        df["test_again_result"] = df["复验判定结果"]
        df["non_conformance"] = df["不合格项"]
        df["last_steel_grade"] = df["综判牌号"]
        df["judger"] = df["综判人"]
        df["handle_date"] = df["处置日期"]
        df["degrade_reason"] = df["改判（降级）原因"]
        df["illustration"] = df["说明"]
        df["comment"] = df["备注（接通知）"]
        df["is_appear_loss"] = df["是上报损失"]
        df["is_appear"] = df["是否上报"]
        df["appear_date"] = df["上报日期"]

        df = df.loc[df["coil_id"].notnull()]
        return df

    def clean_shiftblock_data(self, df):
        df["coil_id"] = df["钢卷号"]
        df["order_thick"] = df["订单厚度mm"]
        df["order_width"] = df["订单宽度mm"]
        df["steel_grade"] = df["钢种"]
        df["next_process"] = df["下道工序"]
        df["act_weight"] = df["重量(t)"]
        df["process_defect"] = df["工艺缺陷"]
        df["process_defect_desc"] = df["工艺缺陷描述"]
        df["coil_defect"] = df["外观缺陷"]
        df["coil_defect_desc"] = df["外观缺陷描述"]
        df["surface_defect"] = df["表检缺陷"]
        df["surface_defect_desc"] = df["表检缺陷描述"]
        df["treatment"] = df["处理方案"]
        df["block_state"] = df["判定情况"].apply(lambda x: str(x))
        df["block_man"] = df["判定人"]
        df["slab_grade"] = df["铸坯级别"]
        df["surface_feedback_grade"] = df["表面检测仪反馈级别"]
        df["coil_quality_grade"] = df["外观质量级别"]
        df["shape_quality_grade"] = df["板型质量级别"]
        df["convertor_id"] = df["炉罐号"]
        df["slab_id"] = df["铸坯号"]

        # data wash
        df["block_state"] = df["block_state"].apply(lambda x: str(x))
        df = df.loc[df["steel_grade"] != "钢种"]
        df = df.loc[df["coil_id"].notnull()]
        return df

    def clean_stat_data(self, df):
        df["coil_id"] = df.index
        return df

    def clean_actblock_data(self, df):
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

    def clean_backoff_data(self, df):
        df["coil_id"] = df["成品批次号"]
        return df

    def clean_shape_data(self, df):
        df["coil_id"] = df["卷号"]
        df["steel_grade"] = df["钢种"]
        df["aim_thick"] = df["目标厚度"]
        df["act_width"] = df["实际宽度"]
        df["w40_perc"] = df["楔度公差比"]
        df["end_time"] = df["生产时间"]

        return df
