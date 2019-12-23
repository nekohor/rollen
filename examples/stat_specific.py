import pandas as pd
import numpy as np
import rollen


rln = rollen.tool()

data_dir = "E:/stat_result_data"
result_dir = "d:/work/second_stat"

line = 2250
task = "tmeic"
start_date = 20190101
end_date = 20190430

df = pd.read_excel(
    data_dir + "/stat_{}_{}_{}_{}.xlsx".format(
        line, task, start_date, end_date))


thk_bins = [1.6, 2.5, 4, 6.0, 25.4]
wid_bins = [800, 1200, 1600, 2000, 2250]
df["厚度分档"] = pd.cut(df["aim_thick"], thk_bins).apply(lambda x: str(x))
df["宽度分档"] = pd.cut(df["aim_width"], wid_bins).apply(lambda x: str(x))

# df["钢种分档"] = gp.cut(df["板坯钢种"])
df["钢种分档"] = rln.grade.cut(df["steel_grade"])


col_list = [
    "HEAD_THICK_CLG_AIMRATE_50",
    "HEAD_FDT_AIMRATE_20",
    "MAIN_FDT_AIMRATE_20",
    "MAIN_CT_AIMRATE_20"
]

# df["≥85"] = df[thk_col].apply(lambda x: 100 if x >= 85 else 0)
# df["≥70"] = df[thk_col].apply(lambda x: 100 if x >= 70 else 0)
pd.pivot_table(
    df,
    # index=["钢种分档", "宽度分档", "厚度分档"],
    index=["厚度分档"],
    values=col_list,
    aggfunc=[np.mean, np.size]
).to_excel(
    result_dir + "/{}_{}_{}_{}.xlsx"
    .format(line, task, start_date, end_date)
)
