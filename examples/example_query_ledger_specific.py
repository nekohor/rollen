from rollen.service import CidService
import pandas as pd

current_dir = "D:/work_sync/999other/20190109浪形预测评估"
coils_filename = current_dir + "/" + "coils.xlsx"
coils = pd.read_excel(coils_filename)
coil_ids = coils["coil_id"]


def query():

    service = CidService()
    records = service.get_data_by_coil_ids(coil_ids)

    filename = current_dir + "/" + "cid.xlsx"
    records.to_excel(filename)


if __name__ == '__main__':
    query()
