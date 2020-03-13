from rollen.service import ResultService
import pandas as pd


file_dir = "D:/NutCloudSync/work/collegue/杜军"
file_dir = "D:/work_sync/999other/20200216浪形积分统计分析"
# filename = "/coils.xlsx"
filename = "/浪形异议热卷号.xlsx"

df = pd.read_excel(file_dir + filename)
coil_ids = df["coil_id"]

s = ResultService()
data = s.get_data_by_coil_ids(coil_ids)


result_filename = (
    file_dir + "/mes_result_specific.xlsx"
)

data.to_excel(result_filename)
