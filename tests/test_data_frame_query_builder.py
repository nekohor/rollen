import rollen
import pandas as pd
import numpy as np


def test_dataframe_query():

    tool = rollen.tool()

    df = pd.DataFrame()

    df["id"] = np.arange(0, 24)
    df["aim_thick"] = np.arange(0, 24)

    result = tool.query.table(df).where(
        "aim_thick", ">", 5
    ).where(
        "aim_thick", "<=", 15
    ).get()

    print(result)
