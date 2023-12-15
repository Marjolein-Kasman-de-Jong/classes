# Opdracht 9-2 Drie restaurants

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

chazzz_food = Restaurant("chazz food", "colombian food")
king_of_india = Restaurant("king of india", "indian food")
amigo = Restaurant("amigo", "mexican food")

chazzz_food.describe_restaurant()
king_of_india.describe_restaurant()
amigo.describe_restaurant()