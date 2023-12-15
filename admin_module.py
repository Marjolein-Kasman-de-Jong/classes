""" Classes that represent admin privileges and an admin """

from user_module import User

class Privileges():
    """ Class that represents admin privileges """

    def __init__(self):
        """ Initialize attributes to describe privileges """
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        """ Show admin privileges """
        print("Admin privileges are:")
        for privilege in self.privileges:
            print("- " + privilege)


class Admin(User):
    """ Class that represents an admin """

    def __init__(self, first_name, last_name, email, location):
        """ Initialize attributes of the parent class and attributes specific to
         an admin """
        super().__init__(first_name, last_name, email, location)
        self.privileges = Privileges()