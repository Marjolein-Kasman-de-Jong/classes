# Opdracht 9-4 Aantal bediende gasten

class Restaurant():
    """ Class that represents a restaurant """
    
    def __init__(self, name, type):
        """ Initialize attributes to describe a restaurant """
        self.restaurant_name = name.title()
        self.cuisine_type = type.title()
        self.number_served = 0
    
    def describe_restaurant(self):
        """ Print neatly formatted sentences that describe the restaurant """
        print("The name of this restaurant is " + self.restaurant_name + 
              ". The cuisine type of this restaurant is " + self.cuisine_type +
              ".")
    
    def open_restaurant(self):
        """ Print a neatly formatted sentence that says that the restaurant is
        open """
        print(self.restaurant_name + " is open.")

    def set_number_served(self, number_served):
        """ Set the number of guests the restaurant has served """
        self.number_served = number_served
    
    def increment_number_served(self, increment):
        """ Increment the number of guests the restaurant has served """
        self.number_served += increment

restaurant = Restaurant("pinocchio", "italian food")

print("The " + restaurant.restaurant_name + " restaurant has served " + 
      str(restaurant.number_served) + " guests.")
restaurant.number_served = 500
print("The " + restaurant.restaurant_name + " restaurant has served " + 
      str(restaurant.number_served) + " guests.")

restaurant.set_number_served(750)
print("The " + restaurant.restaurant_name + " restaurant has served " + 
      str(restaurant.number_served) + " guests.")

restaurant.increment_number_served(250)
print("The " + restaurant.restaurant_name + " restaurant has served " + 
      str(restaurant.number_served) + " guests.")