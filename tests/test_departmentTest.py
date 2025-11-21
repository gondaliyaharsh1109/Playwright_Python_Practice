from pages.DashboardPage import DashboardPage
from pages.DepartmentPage import DepartmentPage
from pages.LoginPage import LoginPage


def test_createDepartment(page):
    loginPage = LoginPage(page)
    dashboardPage = DashboardPage(page)
    departmentPage = DepartmentPage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    dashboardPage.verifyTextAfterLogin()
    dashboardPage.clickNewButton()
    departmentPage.createNewDepartment()