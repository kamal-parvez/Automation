from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from vehicle_info import VehicleInfo
from owner_info import OwnerInfo


class Info:

    def __init__(self, driver, wait, veh_info, own_info):
        self.driver = driver
        self.wait = wait
        # self.veh_info = VehicleInfo(veh_info)
        # self.own_info = OwnerInfo(own_info)
        self.veh_info = veh_info
        self.own_info = own_info

    def vehicle_info(self):
        self.wait.until(EC.presence_of_element_located((By.NAME, 'manufactureDateYear')))

        self.driver.find_element(By.NAME, 'manufactureDateYear').send_keys(
            self.veh_info.manufacture_year)  # Manufacture Year
        self.driver.find_element(By.NAME, 'manufactureDateMonth').send_keys(
            self.veh_info.manufacture_month)  # Manufacture Month

        self.driver.find_element(By.NAME, 'vehicleManufacturerName').send_keys(
            self.veh_info.manufacturer_name)  # Name of Vehicle Manufacturer
        self.driver.find_element(By.NAME, 'vehicleModel').send_keys(self.veh_info.vehicle_model)  # Model of Vehicle
        self.driver.find_element(By.NAME, 'engineModel').send_keys(self.veh_info.engine_model)  # Engine Model

        self.driver.find_element(By.NAME, 'engineNumber').send_keys(
            self.veh_info.engine_number)  # Engine/Electric Motor Number
        self.driver.find_element(By.NAME, 'chassisNumber').send_keys(
            self.veh_info.chassis_number)  # Frame/Chassis Number
        self.driver.find_element(By.NAME, 'vehicleWeight').send_keys(self.veh_info.weight)  # Weight in KG

        self.driver.find_element(By.NAME, 'seatCapacity').send_keys(self.veh_info.seat_capacity)  # Seat Capacity
        self.driver.find_element(By.NAME, 'engineDisplacement').send_keys(self.veh_info.cc)  # Engine Displacement (CC)

        # Max power
        self.driver.find_element(By.NAME, 'enginePowerValue').send_keys(self.veh_info.engine_power)  # Engine Power
        self.driver.find_element(By.NAME, 'enginePowerRpm').send_keys(
            self.veh_info.engine_power_rpm)  # Engine Power RPM
        Select(self.driver.find_element(By.NAME, 'enginePowerUnit')).select_by_index(
            self.veh_info.engine_power_unit)  # Engine Power Unit

        # Owner Type
        try:
            Select(self.driver.find_element(By.NAME, 'ownershipType')).select_by_index(self.veh_info.ownership_type)
            # self.driver.find_element(By.NAME, 'ownershipType').send_keys('Commercial')
        except:
            print('Owner Type Selection is not working....')

        # Vehicle Tye
        try:
            Select(self.driver.find_element(By.NAME, 'vehicleType')).select_by_index(self.veh_info.vehicle_type)
        except:
            print('Vehicle Type Selection is not working')

    def owner_info(self):
        # Click on Owner Info Tab
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[3]/div[2]/form/div[2]/a[2]').click()

        # Fill up Individual Info
        self.individual_owner()

        try:
            # Click on Next in Owner Info Tab
            self.driver.find_element(By.ID, 'next-document').click()

            # Click on Next in Document Page
            self.wait.until(EC.presence_of_element_located((By.ID, 'next-confirm')))
            self.driver.find_element(By.ID, 'next-confirm').click()

            # Click on Submit Button
            self.wait.until(EC.presence_of_element_located((By.ID, 'update')))
            self.driver.find_element(By.ID, 'update').click()


        except Exception as e:
            print(e)

        try:
            # Download
            self.wait.until(EC.presence_of_element_located((By.ID, 'download')))
            self.driver.find_element(By.ID, 'download').click()


        except Exception as e:
            print(e)

    def individual_owner(self):
        self.wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))

        try:
            self.driver.find_element(By.NAME, 'firstName').send_keys(self.own_info.first_name)  # First Name
            self.driver.find_element(By.NAME, 'lastName').send_keys(self.own_info.last_name)  # Last Name
            Select(self.driver.find_element(By.NAME, 'nationality')).select_by_index(
                self.own_info.nationality)  # Nationality

            self.driver.find_element(By.NAME, 'citizenshipNumber').send_keys(
                self.own_info.citizenship_number)  # Citizenship/Passport Number
            self.driver.find_element(By.NAME, 'panNumber').send_keys(self.own_info.pan_number)  # Pan Number
            self.driver.find_element(By.NAME, 'address').send_keys(self.own_info.address)  # Address
            self.driver.find_element(By.NAME, 'financedBy').send_keys(
                self.own_info.financed_by)  # Financed by (If purchased with loan)

        except:
            print('Owner Info Tab not loading.....')




