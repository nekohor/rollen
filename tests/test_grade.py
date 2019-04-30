import rollen
import pandas as pd
import logging
logging.basicConfig(
    format=(
        "%(asctime)s - %(pathname)s[line:%(lineno)d] - "
        "%(levelname)s: %(message)s"
    ),
    level=logging.DEBUG)


def test_grade_catego():

    df = pd.DataFrame()
    df["grade"] = pd.Series(
        ["MRTRG00201", "SPHC-P", "MGW290", "MRTRG00301", "SAE1022-ZC"])

    utils = rollen.tool()
    logging.info(
        utils.grade.cut(df["grade"])
    )

    logging.info(
        utils.grade.select(df, "grade", "广义冷基")
    )
