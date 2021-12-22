from Project_One.custom_exceptions.incorrect_login import LoginFailed
from Project_One.dao_imp.manager_dao_imp import ManagerDAOImp
from Project_One.entities.manager import Manager
from Project_One.service_dao_imp.manager_service_imp import ManagerServiceImp

manager_dao = ManagerDAOImp()
manager_service = ManagerServiceImp(manager_dao)

manager_wrong_login: Manager = Manager(1, 'Eric', 'Sumetski', 'ericsu', 'ericrules')


# This method checks to see if the login information was put in correctly or not, but since it's incorrect,
# it will display exception making sure it grabs it. Here we have a method to grab the error.
def test_get_manager_login_fail():
    try:
        manager_service.manager_dao.check_manager_login(manager_wrong_login)
        assert False
    except LoginFailed as e:
        assert str(e) == "Login was not successful, please try again."
