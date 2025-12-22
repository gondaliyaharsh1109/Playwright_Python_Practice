from faker import Faker
from playwright.sync_api import expect

from pages.BasePage import BasePage


class DepartmentPage(BasePage):
    fake = Faker()
    enterDepartmentInputField = "//input[contains(@id,'departmentName')]"
    enterLocationInputField = "//input[contains(@id,'location')]"
    clickSaveBtn = "//button[contains(text(),'Save')]"
    searchInputField = "//input[contains(@id,'search')]"
    firstDepartmentNameAfterSearch = "(//div[contains(@data-field,'departmentName')])[2]"

    def createNewDepartment(self):
        fakeDepartmentName = self.fake.job()
        fakeLocationName = self.fake.city()
        self.fill(self.enterDepartmentInputField, fakeDepartmentName)
        self.fill(self.enterLocationInputField, fakeLocationName)
        # self.page.pause()
        self.click(self.clickSaveBtn)
        self.verifyToastMessage("Department created successfully.")
        self.page.locator(self.searchInputField).is_visible()
        self.fill(self.searchInputField, fakeDepartmentName)
        self.press_key(self.searchInputField,"Enter")
        self.verify_text(self.firstDepartmentNameAfterSearch, fakeDepartmentName)
