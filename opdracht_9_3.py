# Opdracht 9-3 Gebruikers

class User():
    """ Class that represents a user """

    def __init__(self, first_name, last_name, email, location):
        """ Initialize attributes to describe a user """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.location = location
    
    def describe_user(self):
        """ Print an overview of user data """
        print("\nName: " + self.first_name + " " + self.last_name + "." +
              "\nEmail: " + self.email + "." +
              "\nLocation: " + self.location + ".")
    
    def greet_user(self):
        """ Print a personalized greeting """
        print("\nHello, " + self.first_name + " " + self.last_name + ".")

user1 = User("Donald", "Duck", "donald@duckstad.ds", "Duckstad")
user2 = User("Grote", "Smurf", "g.smurf@smurfendorp.sd", "Smurfendorp")
user3 = User("AllStar", "Zeewaardig", "allstarzeewaardig@snorkelland.sl",
             "Diepe Zee")

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()