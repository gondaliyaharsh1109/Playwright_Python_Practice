from playwright.sync_api import expect, Page

from pages.BasePage import BasePage


class DashboardPage(BasePage):
    listText = "//p[contains(@class,'MuiTypography-root')]"
    clickNewBtn = "//button[contains(text(),'New')]"
    createDepartmentText = "//p[contains(@class,'MuiTypography-root MuiTypography-body1 css')]"
    toggleBtnToHideSideBar = "svg[data-testid='KeyboardDoubleArrowLeftIcon']"
    sideBarList = "//ul[contains(@class,'MuiList-root MuiList-padding css-1ontqvh')]"
    toggleBtnToShowSideBar = "svg[data-testid='MenuIcon']"
    profileBtn = "//div[contains(@class,'MuiAvatar-root MuiAvatar-circular')]"
    verifyNameOnProfileBtn = "(//p[contains(@class,'MuiTypography-body1 css-1cp532n')])[1]"
    verifyEmailOnProfileBtn = "(//span[contains(@class,'MuiTypography-caption css-19na5kj')])[1]"
    verifyRoleOnProfileBtn = "(//span[contains(@class,'MuiTypography-caption css-19na5kj')])[2]"
    sidebarSearchInputField = "//input[contains(@aria-label,'Search')]"
    departmentTextOnSideBar = "(//span[contains(text(),'Departments')])[1]"
    positionTextOnSideBar = "//span[contains(text(),'Position')]"
    employeeTextOnSideBar = "//span[contains(text(),'Employees')]"
    leaveTextOnSideBar = "//span[contains(text(),'Leave')]"
    tasksTextOnSideBar = "//span[contains(text(),'Tasks')]"
    positionTextInPositionPage = "(//span[contains(text(),'Position')])[2]"
    pickLocationNameForFiltering = "(//div[contains(@data-field,'location')])[3]"
    filterBtnOnDepartment = "(//button[contains(@variant,'contained')])[2]"
    clickClearBtnInFilterInDepartment = "//button[contains(text(),'Clear')]"
    clickAddBtnInFilterInDepartment = "//button[contains(text(),'Add')]"
    clickDropdownInFilterInDepartment = "//div[contains(@id,'id__column_0')]"
    selectLocationInFilterInDepartment = "//li[contains(@data-value,'location')]"
    valueInputFieldInFilterInDepartment = "//input[contains(@id,'value_0')]"
    clickOkBtnInFilterInDepartment = "//button[contains(text(),'OK')]"
    visibleNumberOfFilterApplied = "//span[contains(@class,'MuiBadge-anchorOriginTopRight')]"
    verifyLocationNameAfterSearchInDepartment = "(//div[contains(@data-field,'location')])[2]"
    pickDepartmentNameForFiltering = "(//div[contains(@data-field,'departmentName')])[5]"
    pickDepartmentNameForStatus = "(//div[contains(@data-field,'departmentName')])[6]"
    searchInputField = "//input[contains(@id,'search')]"
    firstDepartmentNameAfterSearch = "(//div[contains(@data-field,'departmentName')])[2]"
    clickDeactivateBtn = "//button[contains(text(),'Save')]/following-sibling::button[contains(text(),'De-Activate')]"
    verifyStatusAfterUpdatingStatus = "(//div[contains(@data-field,'inactive')])[2]"

    def verifyTextAfterLogin(self):
        expect(self.page.locator(self.listText)).to_contain_text("List")

    def clickNewButton(self):
        self.click(self.clickNewBtn)
        expect(self.page.locator(self.createDepartmentText)).to_contain_text("Create Department")

    def clickToggleBtnForSideBar(self):
        self.click(self.toggleBtnToHideSideBar)
        self.waitForElementToBeInvisible(self.sideBarList)
        self.click(self.toggleBtnToShowSideBar)
        self.waitForElementToBeVisible(self.sideBarList)

    def clickProfileBtnAndConfirmRole(self):
        self.click(self.profileBtn)
        expect(self.page.locator(self.verifyNameOnProfileBtn)).to_contain_text("PyTheta Admin")
        expect(self.page.locator(self.verifyEmailOnProfileBtn)).to_contain_text("Email:")
        expect(self.page.locator(self.verifyRoleOnProfileBtn)).to_contain_text("Admin")
        self.page.keyboard.press("Escape")

    def searchFunctionalityOnSideBar(self):
        # For Department
        self.click(self.sidebarSearchInputField)
        self.fill(self.sidebarSearchInputField, "de")
        expect(self.page.locator(self.departmentTextOnSideBar)).to_be_visible()
        # expect(self.page.locator(self.positionTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.employeeTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.leaveTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.tasksTextOnSideBar)).not_to_be_visible()
        self.page.locator(self.sidebarSearchInputField).clear()

        # For Position
        self.fill(self.sidebarSearchInputField, "po")
        # self.page.pause()
        expect(self.page.locator(self.positionTextOnSideBar)).to_be_visible()
        # expect(self.page.locator(self.departmentTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.employeeTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.leaveTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.tasksTextOnSideBar)).not_to_be_visible()
        self.page.locator(self.sidebarSearchInputField).clear()

        # For Employee
        self.fill(self.sidebarSearchInputField, "em")
        expect(self.page.locator(self.employeeTextOnSideBar)).to_be_visible()
        # expect(self.page.locator(self.departmentTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.positionTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.leaveTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.tasksTextOnSideBar)).not_to_be_visible()
        self.page.locator(self.sidebarSearchInputField).clear()

        # For Leave
        self.fill(self.sidebarSearchInputField, "le")
        expect(self.page.locator(self.leaveTextOnSideBar)).to_be_visible()
        # expect(self.page.locator(self.departmentTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.positionTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.employeeTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.tasksTextOnSideBar)).not_to_be_visible()
        self.page.locator(self.sidebarSearchInputField).clear()

        # For Tasks
        self.fill(self.sidebarSearchInputField, "ta")
        expect(self.page.locator(self.tasksTextOnSideBar)).to_be_visible()
        # expect(self.page.locator(self.departmentTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.positionTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.employeeTextOnSideBar)).not_to_be_visible()
        # expect(self.page.locator(self.leaveTextOnSideBar)).not_to_be_visible()

    def clickOnPositionTab(self):
        self.click(self.positionTextOnSideBar)
        expect(self.page.locator(self.positionTextInPositionPage)).to_contain_text("Position")

    def searchingDepartmentUsingLocationFilter(self):
        getLocationNameForFilter = self.page.locator(self.pickLocationNameForFiltering).inner_text()
        self.click(self.filterBtnOnDepartment)
        self.click(self.clickClearBtnInFilterInDepartment)
        self.click(self.clickAddBtnInFilterInDepartment)
        self.click(self.clickDropdownInFilterInDepartment)
        self.click(self.selectLocationInFilterInDepartment)
        self.fill(self.valueInputFieldInFilterInDepartment, getLocationNameForFilter)
        self.click(self.clickOkBtnInFilterInDepartment)
        expect(self.page.locator(self.visibleNumberOfFilterApplied)).to_contain_text("1")
        expect(self.page.locator(self.verifyLocationNameAfterSearchInDepartment)).to_contain_text(
            getLocationNameForFilter)

    def updateStatusOfDepartmentFromActiveToInactiveAndVerifyBySearch(self):
        getDepartmentNameForStatus = self.page.locator(self.pickDepartmentNameForStatus).inner_text()
        self.fill(self.searchInputField,getDepartmentNameForStatus)
        self.page.locator(self.searchInputField).press("Enter")
        self.page.locator(self.firstDepartmentNameAfterSearch).dblclick()
        self.click(self.clickDeactivateBtn)
        self.verifyToastMessage("Department status updated successfully.")
        self.fill(self.searchInputField,getDepartmentNameForStatus)
        self.page.locator(self.searchInputField).press("Enter")
        expect(self.page.locator(self.verifyStatusAfterUpdatingStatus)).to_contain_text("Inactive")