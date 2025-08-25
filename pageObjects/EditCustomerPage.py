from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditCustomerPage:
    txtEmail_id = "SearchEmail"
    btnSearch_id = "search-customers"
    table_id = "customers-grid"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def searchCustomerByEmail(self, email):
        email_box = self.wait.until(EC.visibility_of_element_located((By.ID, self.txtEmail_id)))
        email_box.clear()
        email_box.send_keys(email)

        self.driver.find_element(By.ID, self.btnSearch_id).click()

        # wait until grid reload finishes
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//table[@id='customers-grid']//tbody/tr")))

    def clickEditButtonByEmail(self, email):
        # dynamically fetch rows each time (no stale refs)
        row_count = len(self.driver.find_elements(By.XPATH, "//table[@id='customers-grid']//tbody/tr"))
        for r in range(1, row_count + 1):
            # fetch email text fresh for each row
            email_xpath = f"//table[@id='customers-grid']//tbody/tr[{r}]/td[2]"
            email_text = self.wait.until(EC.presence_of_element_located((By.XPATH, email_xpath))).text

            if email_text.strip().lower() == email.strip().lower():
                edit_xpath = f"//table[@id='customers-grid']//tbody/tr[{r}]//a[contains(text(),'Edit')]"
                edit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, edit_xpath)))
                edit_button.click()
                break

    def setFirstName(self, fname):
        first_name_box = self.wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
        first_name_box.clear()
        first_name_box.send_keys(fname)

    def setLastName(self, lname):
        last_name_box = self.wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
        last_name_box.clear()
        last_name_box.send_keys(lname)

    def clickSave(self):
        save_btn = self.wait.until(EC.element_to_be_clickable((By.NAME, "save")))
        save_btn.click()
        # wait for success notification
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success")))
