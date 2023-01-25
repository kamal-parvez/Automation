import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from registration_info import RegistrationInfo


class AccountRegistration:

    def __init__(self, link, driver, wait, reg_info):
        self.link = link
        self.driver = driver
        self.wait = wait
        # self.reg_info = RegistrationInfo(reg_info)
        self.reg_info = reg_info

    def home_page(self):
        self.driver.get(self.link)

        # Click on Get Started
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[4]/div/div/div[1]/a[1]')))
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[4]/div/div/div[1]/a[1]').click()

    def reg_no_page(self):
        # Registration Number
        self.wait.until(EC.presence_of_element_located((By.NAME, 'region')))
        Select(self.driver.find_element(By.NAME, 'region')).select_by_index(self.reg_info.region_index)
        # self.driver.find_element(By.NAME, 'tmo').send_keys(self.reg_info.tmo_code)
        self.driver.find_element(By.NAME, 'less').send_keys(self.reg_info.lot_number)
        # Select(self.driver.find_element(By.NAME, 'alphabet')).select_by_index(2)
        Select(self.driver.find_element(By.NAME, 'alphabet')).select_by_index(
            self.reg_info.alphabet_index)  # क्ष - chhya
        self.driver.find_element(By.NAME, 'more').send_keys(self.reg_info.more)

        # Registration Date
        self.driver.find_element(By.NAME, 'day').send_keys(self.reg_info.day)
        self.driver.find_element(By.NAME, 'month').send_keys(self.reg_info.month)
        self.driver.find_element(By.NAME, 'year').send_keys(self.reg_info.year)

        # Captcha
        self.driver.find_element(By.NAME, 'captcha').send_keys(self.reg_info.captcha)

        # Click on Continue
        self.driver.find_element(By.ID, 'start').click()

    def mobile_no_page(self):
        self.wait.until(EC.presence_of_element_located((By.NAME, 'mobile')))
        self.driver.find_element(By.NAME, 'mobile').send_keys(self.reg_info.mobile)
        self.driver.find_element(By.ID, 'send-sms').click()

        self.wait.until(EC.presence_of_element_located((By.NAME, 'verificationCode')))
        self.driver.find_element(By.NAME, 'verificationCode').send_keys(self.reg_info.mobile_otp)
        self.driver.find_element(By.ID, 'verify-mobile-code').click()

    def email_page(self):
        wait_time_email = 10
        try:
            WebDriverWait(self.driver, wait_time_email).until(EC.presence_of_element_located((By.NAME, 'email')))
            self.driver.find_element(By.NAME, 'email').send_keys(self.reg_info.email)
            self.driver.find_element(By.ID, 'send-email').click()

            self.wait.until(EC.presence_of_element_located((By.NAME, 'verificationCode')))
            self.driver.find_element(By.NAME, 'verificationCode').send_keys(self.reg_info.email_otp)
            self.driver.find_element(By.ID, 'verify-email-code').click()
        except:
            print('Draft application is loading...email not required...')
