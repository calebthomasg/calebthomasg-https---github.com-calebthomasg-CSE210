import random


# TODO: Implement the Die class as follows...


#THIS IS WHERE WE CREATE THE Die CLASS:
class Die:
#THIS IS THE METHOD WHERE WE INITIALIZE THE ATTRIBUTES:
    def __init__(self):
        self.value = 0
        self.points = 0
#THIS IS THE METHOD FOR ROLLING. IT WILL GENERATE NEW RANDOM VALUES ON A
#ROLL AND IT WILL CALCULATE THE POINTS
    def roll(self):
        self.value = random.randint(1,6)
        self.points = 50 if self.value == 5 else 100 if self.value == 1 else 0

# 1) Add the class declaration. Use the following class comment.
"""A small cube with a different number of spots on each of its six sides.

    The responsibility of Die is to keep track of the side facing up and calculate the points for 
    it.
   
    Attributes:
        value (int): The number of spots on the side facing up.
        points (int): The number of points the die is worth.
    """


# 2) Create the class constructor. Use the following method comment.
"""Constructs a new instance of Die with a value and points attribute.

        Args:
            self (Die): An instance of Die.
        """

# 3) Create the roll(self) method. Use the following method comment.
"""Generates a new random value and calculates the points.
        
        Args:
            self (Die): An instance of Die.
        """