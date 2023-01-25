import pandas


class RegistrationInfo:

    # def __int__(self, reg_info):
    #     self = reg_info

    def __init__(self, index):
        data = pandas.read_excel('input.xlsx', sheet_name='Registration_Info')
        self.region_index = data.at[index, 'Region Index']
        self.tmo_code = str(data.at[index, 'TMO Code'])
        self.lot_number = str(data.at[index, 'Lot Number'])
        self.alphabet_index = data.at[index, 'Alphabet Index']
        self.more = str(data.at[index, 'More'])
        self.day = str(data.at[index, 'Day'])
        self.month = str(data.at[index, 'Month'])
        self.year = str(data.at[index, 'Year'])
        self.captcha = str(data.at[index, 'Captcha'])
        self.mobile = str(data.at[index, 'Mobile'])
        self.mobile_otp = str(data.at[index, 'Mobile OTP'])
        self.email = str(data.at[index, 'Email'])
        self.email_otp = str(data.at[index, 'Email OTP'])
