from rollen.service import LocationService


s = LocationService()

df = s.get_data_by_time(1580, 20200302, 20200303)

print(df)
