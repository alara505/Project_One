from Project_One.custom_exceptions.incorrect_login import LoginFailed
from Project_One.dao_imp.employee_dao_imp import EmployeeDAOImp
from Project_One.entities.employees import Employee
from Project_One.service_dao_imp.employee_service_imp import EmployeeServiceImp

employee_dao = EmployeeDAOImp()
employee_service = EmployeeServiceImp(employee_dao)

employee_wrong_login: Employee = Employee(2, "Eric", "Strange", "ericc101", "stranges1")


# This method checks to see if the login information was put in correctly or not, but since it's incorrect,
# it will display exception making sure it grabs it. Here we have a method to grab the error.
def test_get_employee_login_fail():
    try:
        employee_service.service_check_employee_login(employee_wrong_login)
        assert False
    except LoginFailed as e:
        assert str(e) == "Login was not successful, please try again."
