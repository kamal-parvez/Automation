import pandas


class VehicleInfo:

    # def __int__(self, vehicle_info):
    #     self = vehicle_info

    def __init__(self, index):
        data = pandas.read_excel('input.xlsx', sheet_name='Vehicle_Info')
        self.manufacture_year = str(data.at[index, 'Manu Year'])
        self.manufacture_month = str(data.at[index, 'Manu Month'])
        self.manufacturer_name = str(data.at[index, 'Name of Vehicle Manufacturer'])
        self.vehicle_model = str(data.at[index, 'Model of Vehicle'])
        self.engine_model = str(data.at[index, 'Engine Model'])
        self.engine_number = str(data.at[index, 'Engine Number'])
        self.chassis_number = str(data.at[index, 'Chassis Number'])
        self.weight = str(data.at[index, 'Weight'])
        self.seat_capacity = str(data.at[index, 'Seat Capacity'])
        self.cc = str(data.at[index, 'CC'])
        self.engine_power = str(data.at[index, 'Engine Power'])
        self.engine_power_rpm = str(data.at[index, 'Engine Power RPM'])
        self.engine_power_unit = data.at[index, 'Engine Power Unit Index']
        self.ownership_type = data.at[index, 'Ownership Type Index']
        self.vehicle_type = data.at[index, 'Vehicle Type Index']
