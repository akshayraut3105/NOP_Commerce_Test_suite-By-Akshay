from  selenium import  webdriver
from selenium.webdriver.common.by import By
class LoginPage:
    #lets get all locators first that are need to login and logout
    textBox_username_id= "Email"
    textBox_password_id= "Password"
    buttonLogin_xpath= "//button[@type='submit']"
    link_Logout_linktext="Logout"

    def __init__(self,driver):  # this will set the driver for all test case
        self.driver=driver


#Now lets set action methods for login and logout
    def setusername(self, username):
        self.driver.find_element(By.ID, self.textBox_username_id).clear()
        self.driver.find_element(By.ID, self.textBox_username_id).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.ID, self.textBox_password_id).clear()
        self.driver.find_element(By.ID, self.textBox_password_id).send_keys(password)

    def ClickLogin(self):
        self.driver.find_element(By.XPATH, self.buttonLogin_xpath).click()

    def Clicklogout(self):
        self.driver.find_element(By.LINK_TEXT, self.link_Logout_linktext).click()