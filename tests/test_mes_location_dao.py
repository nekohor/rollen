from rollen.dao import LocationDao


d = LocationDao()


print(d.get_data_by_coil_ids(1580, ['M20021000M', 'M20021009M']))
