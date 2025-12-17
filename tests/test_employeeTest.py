import pytest

from pages.EmployeePage import EmployeePage
from pages.LoginPage import LoginPage


@pytest.mark.smoke
def test_addEmployee(page):
    loginPage = LoginPage(page)
    employeePage = EmployeePage(page)
    loginPage.navigateToWebsite()
    loginPage.login("admin@gmail.com", "Admin123!")
    employeePage.addEmployee("Ahmedabad", "Gujarat", "EC Department", "Finance Head", "Employee", "Male")
