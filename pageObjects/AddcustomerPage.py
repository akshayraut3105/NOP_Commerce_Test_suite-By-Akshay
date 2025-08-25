from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:
    # Locators
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),' Customers')]"
    btnAddnew_xpath = "//a[@class='btn btn-primary']"
    txtEmail_id = "Email"
    txtPassword_id = "Password"
    txtFirstName_id = "FirstName"
    txtLastName_id = "LastName"
    rdMaleGender_id = "Gender_Male"
    rdFemaleGender_id = "Gender_Female"
    txtCompanyName_id = "Company"
    txtAdminContent_id = "AdminComment"
    drpmgrOfVendor_id = "VendorId"
    btnSave_name = "save"

    # Customer roles
    txtCustomerRoles_xpath = "//div[@class='input-group-append input-group-required']/parent::div//input"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains(text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains(text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains(text(),'Vendors')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # ---------- Actions ----------
    def clickOnCustomerMenu(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menu_xpath))).click()

    def clickOnCustomerMenuItem(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lnkCustomers_menuitem_xpath))).click()

    def clickOnAddnew(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.btnAddnew_xpath))).click()

    def setEmail(self, email):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.txtEmail_id))).send_keys(email)

    def setPassword(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.txtPassword_id))).send_keys(password)

    def setFirstName(self, fname):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.txtFirstName_id))).send_keys(fname)

    def setLastName(self, lname):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.txtLastName_id))).send_keys(lname)

    def setGender(self, gender):
        if gender == "Male":
            self.wait.until(EC.element_to_be_clickable((By.ID, self.rdMaleGender_id))).click()
        else:
            self.wait.until(EC.element_to_be_clickable((By.ID, self.rdFemaleGender_id))).click()

    def setCompanyName(self, comname):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.txtCompanyName_id))).send_keys(comname)

    def setCustomerRole(self, role):
        # Clear default selection (if "Registered" already exists)
        try:
            self.driver.find_element(By.XPATH, "//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
        except:
            pass

        # Click inside input to open dropdown
        role_input = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, self.txtCustomerRoles_xpath))
        )
        role_input.click()

        # Pick role
        if role == "Registered":
            listitem = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lstitemRegistered_xpath)))
        elif role == "Administrators":
            listitem = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lstitemAdministrators_xpath)))
        elif role == "Guests":
            listitem = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lstitemGuests_xpath)))
        elif role == "Vendors":
            listitem = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lstitemVendors_xpath)))
        else:
            listitem = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.lstitemGuests_xpath)))

        listitem.click()

    def setManagerOrVendor(self, value):
        drp = self.wait.until(EC.presence_of_element_located((By.ID, self.drpmgrOfVendor_id)))
        Select(drp).select_by_visible_text(value)

    def setAdminContent(self, content):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.txtAdminContent_id))).send_keys(content)

    def clickOnSave(self):
        self.wait.until(EC.element_to_be_clickable((By.NAME, self.btnSave_name))).click()
