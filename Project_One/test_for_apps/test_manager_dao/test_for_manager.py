from Project_One.dao_imp.manager_dao_imp import ManagerDAOImp
from Project_One.entities.manager import Manager

manager_dao = ManagerDAOImp()

update_manager = Manager(3, 'Lupe', 'Lara', 'lupe505', 'lupe7070')


def test_get_manager_by_id():
    show = manager_dao.get_manager_information(1)
    assert show.manager_id == 1


def test_get_all_employee():
    elist = manager_dao.get_all_manager_information()
    return elist


def test_check_manager_login():
    manager_login = Manager(username="ericsuu", secretword="ericrules")
    assert manager_dao.check_manager_login(manager_login)


def test_update_employee():
    updated_manager = manager_dao.update_manager(update_manager)
    assert updated_manager
