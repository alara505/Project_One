class Manager:
    def __init__(self, manager_id=0, first_name='first', last_name='last', username='username', secretword='password'):
        self.manager_id = manager_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.secretword = secretword

    def make_manager_dictionary(self):
        return {
            "managerId": self.manager_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username,
            "password": self.secretword
        }

    def __str__(self):
        return "manager Id: {}, first name: {}, last name: {}, username: {}, secretWord: {}".format(self.manager_id,
                                                                                                    self.first_name,
                                                                                                    self.last_name,
                                                                                                    self.username,
                                                                                                    self.secretword)
