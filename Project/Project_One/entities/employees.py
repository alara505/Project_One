class Employee:  # Make sure to include the username and password for the employee and the manager
    def __init__(self, employee_id=0, first_name='first', last_name='last', username='username', secretword='password'):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.secretword = secretword

    def make_employee_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "username": self.username,
            "password": self.secretword
        }

    def __str__(self):
        return "employee Id: {}, first name: {}, last name: {},username: {}, secretWord: {}".format(self.employee_id,
                                                                                                    self.first_name,
                                                                                                    self.last_name,
                                                                                                    self.username,
                                                                                                    self.secretword)
