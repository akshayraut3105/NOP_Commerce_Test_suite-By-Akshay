from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EditCustomerPage:
    # Locators
    txtEmail_id = "SearchEmail"
    btnSearch_id = "search-customers"
    table_xpath = "//table[@id='customers-grid']"
    btnSave_name = "save"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---- Search customer by email ----
    def searchCustomerByEmail(self, email):
        email_box = self.wait.until(
            EC.presence_of_element_located((By.ID, self.txtEmail_id))
        )
        email_box.clear()
        email_box.send_keys(email)
        self.driver.find_element(By.ID, self.btnSearch_id).click()

        # Wait for table reload
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.table_xpath)))

    # ---- Click Edit button for given email ----
    def clickEditButtonByEmail(self, email):
        row_xpath = f"//table[@id='customers-grid']//tbody/tr[td[text()='{email}']]"
        row = self.wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))
        edit_button = row.find_element(By.XPATH, "./td[last()]//a")
        edit_button.click()

    # ---- Update fields ----
    def setFirstName(self, fname):
        box = self.wait.until(EC.presence_of_element_located((By.ID, "FirstName")))
        box.clear()
        box.send_keys(fname)

    def setLastName(self, lname):
        box = self.wait.until(EC.presence_of_element_located((By.ID, "LastName")))
        box.clear()
        box.send_keys(lname)

    def clickSave(self):
        self.driver.find_element(By.NAME, self.btnSave_name).click()
        # Wait until back to customer grid page
        self.wait.until(EC.presence_of_element_located((By.XPATH, self.table_xpath)))

    # ---- Get first name from customer grid by email ----
    def getFirstNameByEmail(self, email):
        row_xpath = f"//table[@id='customers-grid']//tbody/tr[td[text()='{email}']]"
        row = self.wait.until(EC.presence_of_element_located((By.XPATH, row_xpath)))
        return row.find_element(By.XPATH, "./td[3]").text.strip()
