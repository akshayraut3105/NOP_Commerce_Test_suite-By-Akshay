import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.Login_page import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_004_SearchCustomerByEmail:
    baseURL = ReadConfig.getApplicationURl()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self, setup):
        self.logger.info("************ Test_004_SearchCustomerByEmail ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        # ---- Login ----
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.ClickLogin()
        self.logger.info("Login successful")

        # ---- Navigate to Customers ----
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        self.addcust.clickOnCustomerMenuItem()

        # ---- Search by Email ----
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setEmail("victoria_victoria@nopCommerce.com")  # Demo data
        self.searchcust.clickSearch()

        # ✅ Wait for search results table to load
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//table[@id='customers-grid']//tbody"))
        )

        status = self.searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        assert status is True
        self.logger.info("************ Search by Email Test Passed ************")

        self.driver.close()
