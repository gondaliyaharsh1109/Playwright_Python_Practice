from conftest import page
from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage


def test_positiveLoginTest(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com","Admin123!")
    dashboardPage = DashboardPage(page)
    dashboardPage.verifyTextAfterLogin()

def test_incorrectUsernameTest(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@yahoo.com","Admin123!")
    loginPage.verifyToastMessage("No account with this email has been registered.")

def test_incorrectPasswordTest(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com","Admin123@")
    loginPage.verifyToastMessage("Invalid credentials.")

def test_blankFieldValidation(page):
    loginPage = LoginPage(page)
    loginPage.navigateToWebsite()
    loginPage.blankFieldValidation()