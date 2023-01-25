import pandas


class OwnerInfo:

    # def __int__(self, own_info):
    #     self = own_info

    def __init__(self, index):
        data = pandas.read_excel('input.xlsx', sheet_name='Owner_Info')
        self.first_name = str(data.at[index, 'First Name'])
        self.last_name = str(data.at[index, 'Last Name'])
        self.nationality = data.at[index, 'Nationality  Index']
        self.citizenship_number = str(data.at[index, 'Citizenship Number'])
        self.pan_number = str(data.at[index, 'Pan Number'])
        self.address = str(data.at[index, 'Address'])
        self.financed_by = str(data.at[index, 'Financed by'])
