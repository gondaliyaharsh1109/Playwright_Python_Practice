from playwright.sync_api import expect, Page


class BasePage:
    websiteUrl = "https://employee-cicd.vercel.app/login"
    toastMessage = "//p[contains(@class,'MuiTypography-body1 css-1cp532n')]"

    def __init__(self, page: Page):
        self.page = page

    def navigateToWebsite(self):
        self.page.goto(self.websiteUrl)
        # self.page.set_viewport_size({"width":1536,"height":816})

    def click(self, locator):
        self.page.locator(locator).click()

    def fill(self, locator, text):
        self.page.locator(locator).fill(text)

    def waitForElementToBeVisible(self, locator):
        self.page.locator(locator).is_visible()

    def waitForElementToBeInvisible(self, locator):
        self.page.locator(locator).is_hidden()

    def verifyToastMessage(self, text):
        expect(self.page.locator(self.toastMessage)).to_contain_text(text)