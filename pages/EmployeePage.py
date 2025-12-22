from faker import Faker

from pages.BasePage import BasePage


class EmployeePage(BasePage):

    fake = Faker("en_IN")
    clickEmployeeTab = "//span[contains(text(),'Employees')]"
    clickNewBtn = "//button[contains(text(),'New')]"
    createEmployeeText = "//p[contains(@class,'MuiTypography-root MuiTypography-body1 css')]"
    emailInputField = "//input[contains(@id,'email')]"
    clickUserTypeDropdown = "//div[contains(@id,'id__userType')]"
    selectUserTypeDropdown = "//li[contains(@data-value,'hr')]"
    firstNameInputField = "//input[contains(@id,'firstName')]"
    middleNameInputField = "//input[contains(@id,'middleName')]"
    lastNameInputField = "//input[contains(@id,'lastName')]"
    clickAddressBtn = "//button[contains(@variant,'contained')]"
    addressLine1Input = "//input[contains(@id,'addrline1')]"
    addressLine2Input = "//input[contains(@id,'addrline2')]"
    clickCitySelectionBtn = "//input[contains(@id,'city')]/../div/button"
    searchInputField = "//input[contains(@id,'search')]"
    firstCityNameAfterSearch = "(//div[contains(@data-field,'cityName')])[2]"
    clickStateSelectionBtn = "//input[contains(@id,'state')]/../div/button"
    firstStateNameAfterSearch = "(//div[contains(@data-field,'stateName')])[2]"
    postalCodeInputField = "//input[contains(@id,'postalcode')]"
    clickOkBtn = "//button[contains(text(),'OK')]"
    genderDropdown = "//div[contains(@id,'id__gender')]"
    mobileInputField = "//input[contains(@id,'mobilePhone')]"
    clickDepartmentSelectBtn = "//input[contains(@id,'departmentName')]/../div/button"
    firstDepartmentNameAfterSearch = "(//div[contains(@data-field,'departmentName')])[2]"
    clickPositionSelectBtn = "//input[contains(@id,'positionName')]/../div/button"
    firstPositionNameAfterSearch = "(//div[contains(@data-field,'positionName')])[2]"
    saveBtn = "//button[contains(text(),'Save')]"
    addedEmployeeName = "(//div[contains(@data-field,'lastName')])[2]"

    def generate_fake_employee_data(self):
        return {
            "email": self.fake.email(),
            "first_name": self.fake.first_name(),
            "middle_name": self.fake.first_name(),
            "last_name": self.fake.last_name(),
            "address_line1": self.fake.street_address(),
            "address_line2": self.fake.street_address(),
            "postal_code": self.fake.postcode()[:6],
            "mobile": self.fake.msisdn()[:10],
        }

    def navigate_to_add_employee(self):
        self.click(self.clickEmployeeTab)
        self.click(self.clickNewBtn)
        self.verify_visible(self.createEmployeeText)

    def fill_basic_details(self, data: dict, userTypeOption: str):
        self.fill(self.emailInputField, data["email"])

        self.click(self.clickUserTypeDropdown)
        self.click(f"//li[contains(text(), '{userTypeOption}')]")

        self.fill(self.firstNameInputField, data["first_name"])
        self.fill(self.middleNameInputField, data["middle_name"])
        self.fill(self.lastNameInputField, data["last_name"])

    def fill_address_details(self, data: dict, cityName: str, stateName: str):
        self.click(self.clickAddressBtn)

        self.fill(self.addressLine1Input, data["address_line1"])
        self.fill(self.addressLine2Input, data["address_line2"])

        self.click(self.clickCitySelectionBtn)
        self.fill(self.searchInputField, cityName)
        self.dblClick(self.firstCityNameAfterSearch)

        self.click(self.clickStateSelectionBtn)
        self.fill(self.searchInputField, stateName)
        self.dblClick(self.firstStateNameAfterSearch)

        self.fill(self.postalCodeInputField, data["postal_code"])
        self.click(self.clickOkBtn)
        self.verifyToastMessage("Address created successfully.")

    def fill_contact_details(self, data: dict, genderOption: str):
        self.click(self.genderDropdown)
        self.click(f"//li[contains(text(), '{genderOption}')]")

        self.fill(self.mobileInputField, data["mobile"])

    def select_department_and_position(self, departmentName: str, positionName: str):
        self.click(self.clickDepartmentSelectBtn)
        self.fill(self.searchInputField, departmentName)
        self.dblClick(self.firstDepartmentNameAfterSearch)

        self.click(self.clickPositionSelectBtn)
        self.fill(self.searchInputField, positionName)
        self.dblClick(self.firstPositionNameAfterSearch)

    def save_and_verify_employee(self, firstName: str):
        self.click(self.saveBtn)
        self.verifyToastMessage("Employee created successfully.")

        self.fill(self.searchInputField, firstName)
        self.press_key(self.searchInputField, "Enter")
        self.verify_visible(self.addedEmployeeName)

    def addEmployee(self,cityName: str,stateName: str,departmentName: str,positionName: str,userTypeOption: str,genderOption: str):
        data = self.generate_fake_employee_data()

        self.navigate_to_add_employee()
        self.fill_basic_details(data, userTypeOption)
        self.fill_address_details(data, cityName, stateName)
        self.fill_contact_details(data, genderOption)
        self.select_department_and_position(departmentName, positionName)
        self.save_and_verify_employee(data["first_name"])
