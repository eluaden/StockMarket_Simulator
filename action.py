import random
from action_traits import ActionTraits
from name_generator import NameGenerator

class Action:
    """
    This class represents an action in the game.

    Attributes:
        name (str): The name of the action.
        ticker (int): The ticker of the action.
        price (float): The price of the action.
        shares (int): The number of shares of the action.
        level (int): The level of the action (1,2,3,4), the higher the level, bigger the class volatility.


    """

    def __init__(self, price, shares, level):
        self.price = price
        self.shares = shares
        self.level = level
        self.traits = ActionTraits() # randomly generated traits
        self.name = NameGenerator.generate_name(self.traits.major_sector)
        self.ticker = NameGenerator.action_ticker(self.name)

    def update_price(self):
        """
        This function updates the price of the action based on the level of the action.
        The higher the level, the bigger the class volatility.
        """

        self.price *= 1 + (random.uniform(-0.05, 0.05) * self.level)

        # The price is updated by a random percentage between -5% and 5% multiplied by the level of the action.

    def update_level(self):
        """
        This function updates the level of the action randomly.
        """

        random_int = random.randint(1, 2)

        if random_int == 1:
            if (self.level != 4):
                self.level += 1
        else:
            if (self.level != 1):
                self.level -= 1
