import pytest
import random
import string
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.Login_page import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


# Utility function: random email generator
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    def test_addCustomer(self, setup):
        self.logger.info("******** Starting Test_003_AddCustomer ********")

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # -------- Login --------
        self.loginPage = LoginPage(self.driver)
        self.loginPage.setusername(self.username)
        self.loginPage.setpassword(self.password)
        self.loginPage.ClickLogin()
        self.logger.info("Login successful")

        # -------- Add Customer --------
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.clickOnAddnew()

        self.logger.info("Providing customer info...")

        email = random_generator() + "@gmail.com"
        self.logger.info(f"Generated Email: {email}")

        self.addcust.setEmail(email)
        self.addcust.setPassword("Akshu@3105")
        self.addcust.setFirstName("Akshay")
        self.addcust.setLastName("Raut")
        self.addcust.setGender("Male")
        self.addcust.setCompanyName("Nvidia")
        self.addcust.setCustomerRole("Registered")
        self.addcust.setManagerOrVendor("Vendor 2")
        self.addcust.setAdminContent("Jay Shree Ram")

        self.addcust.clickOnSave()
        self.logger.info("Saving customer info...")

        # -------- Validation (No try/except) --------
        success_msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
        ).text

        assert "The new customer has been added successfully." in success_msg, (
            f"Customer not added. Message shown: {success_msg}"
        )

        self.logger.info("******** Add Customer Test Passed ********")
        self.logger.info("******** Test_003_AddCustomer Finished ********")
