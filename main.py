import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from account_registration import AccountRegistration
from fill_info import Info
import pandas
from registration_info import RegistrationInfo
from vehicle_info import VehicleInfo
from owner_info import OwnerInfo


def initialization(index):
    driver = webdriver.Chrome(service=Service('C:\Drivers\chromedriver_win32\chromedriver.exe'))
    link = 'http://evrstmain/everest-pub'
    max_wait_time = 100

    wait = WebDriverWait(driver, max_wait_time)
    driver.maximize_window()

    reg_info = RegistrationInfo(index)
    veh_info = VehicleInfo(index)
    own_info = OwnerInfo(index)

    registration = AccountRegistration(link, driver, wait, reg_info)
    registration.home_page()
    registration.reg_no_page()
    registration.mobile_no_page()
    registration.email_page()

    info = Info(driver, wait, veh_info, own_info)
    info.vehicle_info()
    info.owner_info()
    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    total_application = 20
    for index in range(9, total_application):
        initialization(index)
