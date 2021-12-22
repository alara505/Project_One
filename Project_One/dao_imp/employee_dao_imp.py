from Project_One.entities.employees import Employee
from Project_One.dao.employee_dao import EmployeeDAO
from Project_One.util.database_connection import connection
from Project_One.custom_exceptions.incorrect_login import LoginFailed


# To make it more robust add update to have employee change their reimbursement after submitting.

class EmployeeDAOImp(EmployeeDAO):


    # add username instead...
    # def get_employee_information(self, employee_id) -> Employee:
    #     sql = 'select * from "Project_one".employee where employee_id = %s'
    #     cursor = connection.cursor()
    #     cursor.execute(sql, [employee_id])
    #     employee_record = cursor.fetchone()
    #     employee = Employee(*employee_record)
    #     return employee

    def get_employee_by_username(self, username) -> Employee:
        sql = 'select * from "Project_one".employee where username = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [username])
        employee_record = cursor.fetchone()
        employee = Employee(*employee_record)
        return employee

    def get_all_employee_information(self) -> list[Employee]:
        sql = 'select * from "Project_one".employee'
        cursor = connection.cursor()
        cursor.execute(sql)
        employee_records = cursor.fetchall()
        employee_list = []
        for employee in employee_records:
            employee_list.append(Employee(*employee))
        return employee_list

    def update_employee(self, employee: Employee) -> Employee:
        sql = 'update "Project_one".employee set first_name = %s, last_name = %s, username = %s, secretword = %s where employee_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, (
             employee.first_name, employee.last_name, employee.username, employee.secretword, employee.employee_id))
        connection.commit()
        return employee

    def check_employee_login(self, employee: Employee) -> Employee:
        sql = 'select * from "Project_one".employee where username = %s and secretword = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [employee.username, employee.secretword])
        employee_record = cursor.fetchone()
        if employee_record:
            current_employee = Employee(*employee_record)
            return current_employee
        raise LoginFailed("Login was not successful, please try again.")
