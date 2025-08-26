import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pageObjects.EditCustomerPage import EditCustomerPage


@pytest.mark.usefixtures("setup")
class Test_005_EditCustomer:

    @pytest.mark.regression
    def test_editCustomer(self, setup):
        driver = setup
        driver.get("https://admin-demo.nopcommerce.com/login")
        driver.maximize_window()

        # ---- Login ----
        driver.find_element(By.ID, "Email").clear()
        driver.find_element(By.ID, "Email").send_keys("admin@yourstore.com")
        driver.find_element(By.ID, "Password").clear()
        driver.find_element(By.ID, "Password").send_keys("admin")
        driver.find_element(By.XPATH, "//button[text()='Log in']").click()

        # ---- Navigate to Customer List ----
        driver.get("https://admin-demo.nopcommerce.com/Admin/Customer/List")

        ec = EditCustomerPage(driver)
        email_to_edit = "victoria_victoria@nopCommerce.com"

        # ---- Search + Open Edit Page ----
        ec.searchCustomerByEmail(email_to_edit)
        ec.clickEditButtonByEmail(email_to_edit)

        # ---- Update Customer Info ----
        ec.setFirstName("VictoriaUpdated")
        ec.setLastName("TercesUpdated")
        ec.clickSave()

        # ---- Re-search after save (fresh grid) ----
        ec.searchCustomerByEmail(email_to_edit)

        # ---- Locate row fresh by email ----
        row_xpath = f"//table[@id='customers-grid']//tbody/tr[td[text()='{email_to_edit}']]"
        row = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, row_xpath))
        )

        # ---- Now get the first name cell from that row ----
        updated_name = row.find_element(By.XPATH, "./td[3]").text.strip()

        # ---- Assertion ----
        assert "VictoriaUpdated" in updated_name, (
            f"Expected 'VictoriaUpdated' in customer name, but got: {updated_name}"
        )
