from rollen.dao import LocationDao


class LocationService():

    def __init__(self):

        self.dao = LocationDao()

    def get_data_by_coil_ids(self, line, coil_ids):
        df = self.dao.get_data_by_coil_ids(line, coil_ids)
        return df

    def get_data_by_time(self, line, start_time, end_time):
        df = self.dao.get_data_by_time(line, start_time, end_time)
        return df

    def get_data_by_dates(self, line, dates):
        df = self.dao.get_data_by_time(line, dates[0], dates[-1])
        return df
