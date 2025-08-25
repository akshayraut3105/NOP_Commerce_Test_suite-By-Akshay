import pytest
from selenium import webdriver
from pageObjects.Login_page import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtilities

class Test002_DDT_Login:
    baseURL = ReadConfig.getApplicationURl()
    path = ".//Test_Data/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******** Test002_DDT_Login Started ********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)

        self.rows = XLUtilities.getRowCount(self.path, "Sheet1")
        print("Number of Rows:", self.rows)

        lst_status = []   # store Pass/Fail of each test

        for r in range(2, self.rows + 1):
            self.username = XLUtilities.readData(self.path, "Sheet1", r, 1)
            self.password = XLUtilities.readData(self.path, "Sheet1", r, 2)
            self.exp = XLUtilities.readData(self.path, "Sheet1", r, 3)

            self.lp.setusername(self.username)
            self.lp.setpassword(self.password)
            self.lp.ClickLogin()

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info(f"Test Passed with user: {self.username}")
                    lst_status.append("Pass")
                    self.lp.ClickLogout()
                elif self.exp == "Fail":
                    self.logger.error(f"Test Failed (unexpected login) with user: {self.username}")
                    lst_status.append("Fail")
                    self.lp.ClickLogout()

            else:
                if self.exp == "Pass":
                    self.logger.error(f"Test Failed (login not successful) with user: {self.username}")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info(f"Test Passed (login blocked) with user: {self.username}")
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("******** Login DDT Test Passed ********")
            assert True
        else:
            self.logger.error("******** Login DDT Test Faicled ********")
            assert False

        self.driver.close()
