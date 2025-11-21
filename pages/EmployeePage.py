from pages.BasePage import BasePage


class EmployeePage(BasePage):

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

    # def addEmployee(self):