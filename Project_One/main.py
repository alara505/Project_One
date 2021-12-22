from flask import Flask, request, jsonify
from flask_cors import CORS

from Project_One.custom_exceptions.incorrect_login import LoginFailed
from custom_exceptions.incorrect_information import IncorrectCredentials
from custom_exceptions.employee_id_does_not_exist import EmployeeIdDoesNotExistException
from custom_exceptions.manager_id_not_found import ManagerIdNotFoundException
from custom_exceptions.invalid_approval import InvalidApprovalException
from custom_exceptions.reimbursement_duplicate_exception import ReimbursementIdDuplicationException
from custom_exceptions.employee_username_does_not_exist import EmployeeUsernameDoesNotExistException
from custom_exceptions.manager_username_does_not_exist import ManagerUsernameDoesNotExistException
from custom_exceptions.negative_numbers import NoNegativeNumbers
from dao.employee_dao import EmployeeDAO
from dao.manager_dao import ManagerDAO
from dao.reimbursement_dao import ReimbursementDAO
from dao_imp.employee_dao_imp import EmployeeDAOImp
from dao_imp.manager_dao_imp import ManagerDAOImp
from dao_imp.reimbursement_dao_imp import ReimbursementDAOImp
from entities.employees import Employee
from entities.manager import Manager
from entities.reimbursement import Reimbursement
from service_dao.employee_service import EmployeeServiceDAO
from service_dao.manager_service import ManagerServiceDAO
from service_dao.reimbursement_service import ReimbursementDAO
from service_dao_imp.employee_service_imp import EmployeeServiceImp
from service_dao_imp.manager_service_imp import ManagerServiceImp
from service_dao_imp.reimbursement_service_imp import ReimbursementServiceImp

import logging

logging.basicConfig(filename="records.log", level=logging.DEBUG, format=f"%(asctime)s %(levelname)s %(message)s")

app: Flask = Flask(__name__)
CORS(app)

employee_dao = EmployeeDAOImp()
employee_service = EmployeeServiceImp(employee_dao)

manager_dao = ManagerDAOImp()
manager_service = ManagerServiceImp(manager_dao)

reimbursement_dao = ReimbursementDAOImp()
reimbursement_service = ReimbursementServiceImp(reimbursement_dao)


# Make sure to add the dao for the reimbursement, and manager.

# Idea is to change employee id to username
# @app.get("/employee/<employee_id>")
# def get_employee_information(employee_id: str):
#     result = employee_service.service_get_employee_information(int(employee_id))
#     result_as_dictionary = result.make_employee_dictionary()
#     result_as_json = jsonify(result_as_dictionary)
#     return result_as_json

@app.get("/employee/<username>")
def get_employee_by_username(username: str):
    try:
        result = employee_service.service_get_employee_by_username(username)
        result_as_dictionary = result.make_employee_dictionary()
        result_as_json = jsonify(result_as_dictionary)
        return result_as_json
    except EmployeeUsernameDoesNotExistException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/employee")
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


# Make sure to make an reimbursement for the employee id and grab all the information from that employee Id
@app.get("/employee/reimbursement/<employee_id>")
def get_employee_reimbursement_by_employee_id(employee_id: str):
    reimbursement_as_reimbursement = reimbursement_service.service_select_reimbursement_by_employee_id(int(employee_id))
    reimbursement_as_dictionary = []
    for reimbursements in reimbursement_as_reimbursement:
        dictionary_reimbursement = reimbursements.make_reimbursement_dictionary()
        reimbursement_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursement_as_dictionary)


@app.patch("/employee")
def update_information():
    pass


@app.post("/reimbursement")
def service_create_reimbursement():
    try:
        result = request.get_json()
        new_reimbursement = Reimbursement(
            result["reimbursementId"],
            result["employeeId"],
            result["managerId"],
            int(result["reimbursement"]),
            result["reason"],
            result["approval"],
            result["managerComment"]
        )
        reimbursement_to_return = reimbursement_service.service_create_get_reimbursement(new_reimbursement)
        reimbursement_as_dictionary = reimbursement_to_return.make_reimbursement_dictionary()
        reimbursement_as_json = jsonify(reimbursement_as_dictionary)
        return reimbursement_as_json
    except ReimbursementIdDuplicationException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json
    except NoNegativeNumbers as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


@app.get("/reimbursement/all")
def get_all_reimbursement_information():
    reimbursement_as_reimbursement = reimbursement_service.service_select_get_all_reimbursement_information()
    reimbursement_as_dictionary = []
    for reimbursements in reimbursement_as_reimbursement:
        dictionary_reimbursement = reimbursements.make_reimbursement_dictionary()
        reimbursement_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursement_as_dictionary)


@app.get("/past/reimbursements/<manager_id>")
def get_all_past_reimbursement_information(manager_id: int):
    reimbursement_as_reimbursement = reimbursement_service.service_get_past_reimbursements_by_manager_id(
        int(manager_id))
    reimbursement_as_dictionary = []
    for reimbursements in reimbursement_as_reimbursement:
        dictionary_reimbursement = reimbursements.make_reimbursement_dictionary()
        reimbursement_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursement_as_dictionary)


@app.get("/manager/pending/reimbursement/<manager_id>")
def get_all_pending_reimbursement_by_manager_id(manager_id: int):
    reimbursement_as_reimbursement = reimbursement_service.service_get_all_pending_reimbursements_by_manager_id(
        int(manager_id))
    reimbursement_as_dictionary = []
    for reimbursements in reimbursement_as_reimbursement:
        dictionary_reimbursement = reimbursements.make_reimbursement_dictionary()
        reimbursement_as_dictionary.append(dictionary_reimbursement)
    return jsonify(reimbursement_as_dictionary)


# ----------------------------------------------- This is for the Manager ----------------------------------------------

@app.get("/manager/<username>")
def get_manager_by_username(username: str):
    try:
        result = manager_service.service_get_manager_by_username(username)
        result_as_dictionary = result.make_manager_dictionary()
        result_as_json = jsonify(result_as_dictionary)
        return result_as_json
    except ManagerUsernameDoesNotExistException as e:
        exception_dictionary = {"message": str(e)}
        exception_json = jsonify(exception_dictionary)
        return exception_json


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


@app.patch("/reimbursement/approve/<reimbursement_id>")
def service_approve_reimbursement(reimbursement_id):
    try:
        result = request.get_json()
        new_reimbursement = Reimbursement(
            int(reimbursement_id),
            result["employeeId"],
            result["managerId"],
            result["reimbursement"],
            result["reason"],
            result["approval"],
            result["managerComment"]
        )
        reimbursement_to_return = reimbursement_service.service_approve_reimbursement(new_reimbursement)
        return "Manager has updated your reimbursement information" + str(reimbursement_to_return)
    except InvalidApprovalException as e:
        return str(e)


@app.patch("/reimbursement/deny/<reimbursement_id>")
def service_deny_reimbursement(reimbursement_id):
    try:
        result = request.get_json()
        new_reimbursement = Reimbursement(
            int(reimbursement_id),
            result["employeeId"],
            result["managerId"],
            result["reimbursement"],
            result["reason"],
            result["approval"],
            result["managerComment"]
        )
        reimbursement_to_return = reimbursement_service.service_deny_reimbursement(new_reimbursement)
        return "Manager has updated your reimbursement information" + str(reimbursement_to_return)
    except InvalidApprovalException as e:
        return str(e)


# Make sure to create your own feature file Along with Acceptance Criteria for your Project One
app.run()
