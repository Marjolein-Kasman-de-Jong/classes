# Opdracht 9-7 Beheerder

class User():
    """ Class that represents a user """

    def __init__(self, first_name, last_name, email, location):
        """ Initialize attributes to describe a user """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
        self.login_attempts = 0
    
    def describe_user(self):
        """ Print an overview of user data """
        print("\nName: " + self.first_name + " " + self.last_name + "." +
              "\nEmail: " + self.email + "." +
              "\nLocation: " + self.location + ".")
    
    def greet_user(self):
        """ Print a personalized greeting """
        print("\nHello, " + self.first_name + " " + self.last_name + ".")
    
    def increment_login_attempts(self):
        " Increase self.login_attempts by 1 "
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        " Reset self.login_attempts "
        self.login_attempts = 0


class Admin(User):
    """ Class that represents an admin """

    def __init__(self, first_name, last_name, email, location):
        """ Initialize attributes of the parent class and attributes specific to
         an admin """
        super().__init__(first_name, last_name, email, location)
        self.privileges = ['can add post', 'can delete post', 'can ban user']
    
    def show_privileges(self):
        """ Show admin priviliges """
        print("Admin priviliges are:")
        for privilege in self.privileges:
            print("- " + privilege)


user1 = Admin('marjolein', 'kasman-de jong', 'marjolein@marjolein.nl', 'driel') # Kun je hier ook een waarde voor self.privileges doorgeven, of kun je waarden in een child class alleen hardcoden in de class zelf?
user1.show_privileges()