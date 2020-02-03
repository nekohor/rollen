import numpy as np
from sqlalchemy.orm import sessionmaker


class LightInsertion():

    def __init__(self, engine, model_class):

        self.engine = engine
        self.model_class = model_class

    def is_nan(self, field):
        tag = False
        if field is np.nan:
            tag = True
        elif str(field) == 'nan':
            tag = True
        return tag

    def convert_field_type(self, field):
        result = None
        if type(field) == np.float64:
            result = float(field)
        elif type(field) == np.int64:
            result = int(field)
        else:
            result = field
        return result

    def get_model_instance(self, record):

        model_instance = self.model_class()
        for col in record.columns:
            field = record[col]
            if self.is_nan(field):
                pass
            else:
                setattr(
                    model_instance,
                    col,
                    self.convert_field_type(field))

        return model_instance

    def create_table(self):
        self.model_class.metadata.create_all(self.engine)

    def insert_data(self, df):

        DBSession = sessionmaker(bind=self.engine)
        session = DBSession()

        df.index = list(range(0, df.shape[0]))

        for idx in df.index:
            record = df.loc[idx]
            session.add(self.get_model_instance(record))

        session.commit()
        session.close()
