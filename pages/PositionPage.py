from faker.proxy import Faker
from playwright.sync_api import expect

from pages.BasePage import BasePage


class PositionPage(BasePage):
    faker = Faker()
    clickNewBtn = "//button[contains(text(),'New')]"
    verifyCreatePositionText = "//p[contains(@class,'MuiTypography-root MuiTypography-body1 css')]"
    positionNameInputField = "//input[contains(@id,'positionName')]"
    selectDepartmentBtn = "//button[contains(@aria-label,'open lookup')]"
    searchInputField = "//input[contains(@id,'search')]"
    selectFirstDepartment = "(//div[contains(@data-field,'departmentName')])[2]"
    responsibilitiesInputField = "//input[contains(@id,'responsibilities')]"
    qualificationsInputField = "//input[contains(@id,'qualifications')]"
    clickSaveBtn = "//button[contains(text(),'Save')]"
    firstPositionNameAfterSearch = "(//div[contains(@data-field,'positionName')])[2]"
    getTextOfFirstPosition = "(//div[contains(@data-field,'positionName')])[2]"

    def createPosition(self):
        fakePositionName = self.faker.job()
        fakeResponsibility = self.faker.sentence()
        fakeQualification = self.faker.sentence()
        self.click(self.clickNewBtn)
        expect(self.page.locator(self.verifyCreatePositionText)).to_contain_text("Create Position")
        self.fill(self.positionNameInputField, fakePositionName)
        self.click(self.selectDepartmentBtn)
        self.fill(self.searchInputField, "ec department")
        self.page.dblclick(self.selectFirstDepartment)
        self.fill(self.responsibilitiesInputField, fakeResponsibility)
        self.fill(self.qualificationsInputField, fakeQualification)
        self.click(self.clickSaveBtn)
        self.verifyToastMessage("Position created successfully")
        self.page.locator(self.searchInputField).is_visible()
        self.fill(self.searchInputField, fakePositionName)
        self.page.locator(self.searchInputField).press("Enter")
        # self.page.pause()
        expect(self.page.locator(self.firstPositionNameAfterSearch)).to_contain_text(fakePositionName)

    def editPosition(self):
        fakePositionName = self.faker.job()
        fakeResponsibility = self.faker.sentence()
        fakeQualification = self.faker.sentence()
        getFirstPositionName = self.page.locator(self.getTextOfFirstPosition).inner_text()
        self.fill(self.searchInputField, getFirstPositionName)
        self.page.locator(self.searchInputField).press("Enter")
        self.page.locator(self.firstPositionNameAfterSearch).dblclick()
        expect(self.page.locator(self.verifyCreatePositionText)).to_contain_text("Edit Position")
        self.fill(self.positionNameInputField, "")
        self.fill(self.positionNameInputField, fakePositionName)
        self.click(self.selectDepartmentBtn)
        self.fill(self.searchInputField, "water department")
        self.page.dblclick(self.selectFirstDepartment)
        self.fill(self.responsibilitiesInputField, "")
        self.fill(self.responsibilitiesInputField, fakeResponsibility)
        self.fill(self.qualificationsInputField, "")
        self.fill(self.qualificationsInputField, fakeQualification)
        self.click(self.clickSaveBtn)
        self.verifyToastMessage("Updated the position details successfully")
        self.fill(self.searchInputField, fakePositionName)
        self.page.locator(self.searchInputField).press("Enter")
        expect(self.page.locator(self.firstPositionNameAfterSearch)).to_contain_text(fakePositionName)
