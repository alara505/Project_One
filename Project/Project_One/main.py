from flask import Flask, request, jsonify
from flask_cors import CORS

from Project_One.custom_exceptions.incorrect_login import LoginFailed
from custom_exceptions.incorrect_information import IncorrectCredentials
from dao.employee_dao import EmployeeDAO
from dao.manager_dao import ManagerDAO
from dao_imp.employee_dao_imp import EmployeeDAOImp
from dao_imp.manager_dao_imp import ManagerDAOImp
from entities.employees import Employee
from entities.manager import Manager
from service_dao.employee_service import EmployeeServiceDAO
from service_dao.manager_service import ManagerServiceDAO
from service_dao_imp.employee_service_imp import EmployeeServiceImp
from service_dao_imp.manager_service_imp import ManagerServiceImp

import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

employee_dao = EmployeeDAOImp()
employee_service = EmployeeServiceImp(employee_dao)

manager_dao = ManagerDAOImp()
manager_service = ManagerServiceImp(manager_dao)


# Make sure to add the dao for the reimbursement, and manager.


@app.get("/employee/<employee_id>")
def get_employee_information(employee_id: str):
    result = employee_service.service_get_employee_information(int(employee_id))
    result_as_dictionary = result.make_employee_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


@app.get("/employee/all")
def get_all_employee_information():
    employee_as_employee = employee_service.service_get_all_employee_information()
    employee_as_dictionary = []
    for employees in employee_as_employee:
        dictionary_employee = employees.make_employee_dictionary()
        employee_as_dictionary.append(dictionary_employee)
    return jsonify(employee_as_dictionary)


@app.post("/employee/login")
def service_check_employee_login():
    result = request.get_json()
    # if result:
    employee_username = result["username"]
    employee_password = result["password"]
        # else:
        #     return {"Username or Password were entered incorrectly, please try again."}

    try:
        employee_to_return = Employee(username=employee_username, secretword=employee_password)
        employee_as_object = employee_service.service_check_employee_login(employee_to_return)
        employee_as_dict = employee_as_object.make_employee_dictionary()
        employee_as_json = jsonify(employee_as_dict)
        return employee_as_json
    except IncorrectCredentials as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except LoginFailed as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# ----------------------------------------------- This is for the Manager ----------------------------------------------
@app.get("/manager/<manager_id>")
def get_manager_information(manager_id: str):
    result = manager_service.service_get_manager_information(int(manager_id))
    result_as_dictionary = result.make_manager_dictionary()
    result_as_json = jsonify(result_as_dictionary)
    return result_as_json


@app.get("/manager/all")
def get_all_manager_information():
    manager_as_manager = manager_service.service_get_all_manager_information()
    manager_as_dictionary = []
    for managers in manager_as_manager:
        dictionary_manager = managers.make_manager_dictionary()
        manager_as_dictionary.append(dictionary_manager)
    return jsonify(manager_as_dictionary)


@app.post("/manager/login")
def service_check_manager_login():
    result = request.get_json()
    # if result:
    manager_username = result["username"]
    manager_password = result["password"]

    try:
        manager_to_return = Manager(username=manager_username, secretword=manager_password)
        manager_as_object = manager_service.service_check_manager_login(manager_to_return)
        manager_as_dict = manager_as_object.make_manager_dictionary()
        manager_as_json = jsonify(manager_as_dict)
        return manager_as_json
    except IncorrectCredentials as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except LoginFailed as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


# Make sure to create your own feature file Along with Acceptance Criteria for your Project One
app.run()
