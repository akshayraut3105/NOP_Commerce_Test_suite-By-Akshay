from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class SearchCustomer:
    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    tableSearchReasult_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumn_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def setEmail(self, email):
        email_field = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.txtEmail_id))
        )
        email_field.clear()
        email_field.send_keys(email)

    def setFirstName(self, fname):
        firstName = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.txtFirstName_id))
        )
        firstName.clear()
        firstName.send_keys(fname)

    def setLastName(self, lname):
        lastName = self.wait.until(
            EC.visibility_of_element_located((By.ID, self.txtLastName_id))
        )
        lastName.clear()
        lastName.send_keys(lname)

    def clickSearch(self):
        searchBtn = self.wait.until(
            EC.element_to_be_clickable((By.ID, self.btnSearch_id))
        )
        searchBtn.click()
        time.sleep(2)

    def getNoOfRows(self):
        return len(self.driver.find_elements(By.XPATH, self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements(By.XPATH, self.tableColumn_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            emailid = table.find_element(By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[2]").text
            if emailid == email:
                flag = True
                break
        return flag

    def searchCustomerByName(self, Name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            name = table.find_element(By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[3]").text
            if name == Name:
                flag = True
                break
        return flag

    def searchCustomerByRole(self, role):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element(By.XPATH, self.table_xpath)
            role_value = table.find_element(By.XPATH, f"//table[@id='customers-grid']//tbody/tr[{r}]/td[4]").text
            if role.strip().lower() in role_value.strip().lower():   # case-insensitive check
                flag = True
                break
        return flag
