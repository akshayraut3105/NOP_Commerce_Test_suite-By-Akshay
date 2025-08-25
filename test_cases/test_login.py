import pytest
from selenium import webdriver
from pageObjects.Login_page import LoginPage
from utilities.readProperties import ReadConfig
from  utilities.customLogger import LogGen

class Test001login:
    baseurl=ReadConfig.getApplicationURl()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

# create log file
    logger=LogGen.loggen()
# write first test case to get page title

    @pytest.mark.regression
    def test_pageTitle(self,setup):
        self.logger.info("******** Test001login **********")
        self.logger.info("******** Verifying Homepage Title **********")
        self.driver=setup
        self.driver.get(self.baseurl)
        actualTitle=self.driver.title

        if actualTitle=="nopCommerce demo store. Login":
            assert True
            self.logger.info("******** Verifying Homepage Title test case pased **********")
        else:
            self.driver.save_screenshot(r"C:\Users\AKSHAY\PycharmProjects\NOP_Commerce_Test_suite\Screenshots\pageTitle.png")
            self.logger.error("******** Verifying Homepage Title test case Failed **********")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
       self.logger.info("******** Verifying Test Login  **********")
       self.driver = setup
       self.driver.get(self.baseurl)
       # create object of page object class to access all action methods of login

       self.loginObj=LoginPage(self.driver)
       self.loginObj.setusername(self.username)
       self.loginObj.setpassword(self.password)
       self.loginObj.ClickLogin()

       actualTitle = self.driver.title.strip()
       if actualTitle=="Dashboard / nopCommerce administration":
           assert  True
           self.logger.info("******** Verifying Login test case Passed **********")
       else:
           self.driver.save_screenshot(r"C:\Users\AKSHAY\PycharmProjects\NOP_Commerce_Test_suite\Screenshots\test_login.png")
           self.logger.error("******** Verifying Login test case Failed **********")
           assert  False



#https://github.com/pavanoltraining/nopCommerceProject/blob/master/testCases/test_addCustomer.py
