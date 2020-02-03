from rollen.database import DataBaseManager


class CurveDao():

    def __init__(self):

        self.conn = DataBaseManager.get_qms_database()

    def get_data(self, coil_id, factor_name):

        cursor = self.conn.cursor()
        cursor.execute(
            """
            SELECT DATA
            FROM TB_CURVE_DATA
            WHERE MAT_NO = :coil_id AND NAME = 'HSM2.WEDGE40'
            """,
            coil_id=coil_id
        )
        rows = cursor.fetchall()
        arr = str(rows[0][0].read(), 'utf-8').split(",")
        cursor.close()
        return arr
