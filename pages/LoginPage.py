from playwright.sync_api import expect

from pages.BasePage import BasePage


class LoginPage(BasePage):
    email_input = "//input[contains(@name,'email')]"
    password_input = "//input[contains(@type,'password')]"
    login_btn = "//button[contains(text(),'Login')]"
    blankEmailValueRequiredText = "//p[contains(@class,'MuiFormHelperText-root Mui-error MuiFormHelperText-sizeMedium')]"
    blankPasswordValueRequiredText = "//p[contains(@class,'MuiFormHelperText-root Mui-error MuiFormHelperText-sizeSmall')]"

    def login(self, enterEmail, enterPassword):
        self.fill(self.email_input, enterEmail)
        self.fill(self.password_input, enterPassword)
        self.click(self.login_btn)

    def blankFieldValidation(self):
        self.click(self.login_btn)
        self.page.locator(self.blankEmailValueRequiredText).is_visible()
        expect(self.page.locator(self.blankEmailValueRequiredText)).to_contain_text("value is required")
        self.page.locator(self.blankPasswordValueRequiredText).is_visible()
        expect(self.page.locator(self.blankPasswordValueRequiredText)).to_contain_text("value is required")
