# Opdracht 9-1 Restaurant

class Restaurant():
    """ Class that represents a restaurant """
    
    def __init__(self, name, type):
        """ Initialize attributes to describe a restaurant """
        self.restaurant_name = name.title()
        self.cuisine_type = type.title()
    
    def describe_restaurant(self):
        """ Print neatly formatted sentences that describe the restaurant """
        print("The name of this restaurant is " + self.restaurant_name + 
              ". The cuisine type of this restaurant is " + self.cuisine_type +
              ".")
    
    def open_restaurant(self):
        """ Print a neatly formatted sentence that says that the restaurant is
        open """
        print(self.restaurant_name + " is open.")

restaurant = Restaurant("pinocchio", "italian food")

print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()