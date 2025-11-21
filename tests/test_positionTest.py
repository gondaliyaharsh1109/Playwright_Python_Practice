from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.PositionPage import PositionPage


def test_createPosition(page):
    loginPage = LoginPage(page)
    dashboardPage = DashboardPage(page)
    positionPage = PositionPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    dashboardPage.verifyTextAfterLogin()
    dashboardPage.clickOnPositionTab()
    positionPage.createPosition()

def test_editPosition(page):
    loginPage = LoginPage(page)
    dashboardPage = DashboardPage(page)
    positionPage = PositionPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    dashboardPage.verifyTextAfterLogin()
    dashboardPage.clickOnPositionTab()
    positionPage.editPosition()
