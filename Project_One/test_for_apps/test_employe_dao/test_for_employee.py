from Project_One.dao_imp.employee_dao_imp import EmployeeDAOImp
from Project_One.entities.employees import Employee

employee_dao = EmployeeDAOImp()

employee_one: Employee = Employee(1, "Linda", "Never", "Linda101", "Lindarocks")
employee_two: Employee = Employee(2, "David", "Zazulak", "David101", "Runescape")
update_employee: Employee = Employee(4, "Eric", "Strange", "eric101", "strange")


# def test_get_employee_by_id():
#     show = employee_dao.get_employee_information(1)
#     assert show.employee_id == 1

def test_get_employee_by_email():
    returned_employee: Employee = employee_dao.get_employee_by_username("eric101")
    assert returned_employee.employee_id == 4


def test_get_all_employee():
    elist = employee_dao.get_all_employee_information()
    return elist


def test_check_employee_login():
    employee_login = Employee(username="alex101", secretword="alexrocks")
    assert employee_dao.check_employee_login(employee_login)


def test_update_employee():
    updated_employee = employee_dao.update_employee(update_employee)
    assert updated_employee
