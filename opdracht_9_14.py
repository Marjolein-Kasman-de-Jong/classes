# Opdracht 9-14 Dobbelsteen

from random import randint


class Die():
    """ Class that represents a die """

    def __init__(self, sides):
        """Initialize attributes to describe a die."""
        self.sides = sides
    
    def roll_die(self):
        print(randint(1, self.sides))


def create_die_and_roll_it_ten_times(number_of_sides):
    """ Create an instance of Die with the given number of sides and roll it 10 times """
    new_die = Die(number_of_sides)
    print("Roll a die with " + str(number_of_sides) + " sides ten times:")
    for i in range(10):
        new_die.roll_die()


create_die_and_roll_it_ten_times(6)
create_die_and_roll_it_ten_times(10)
create_die_and_roll_it_ten_times(20)