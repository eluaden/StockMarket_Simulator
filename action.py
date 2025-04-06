import random


class Action:
    """
    This class represents an action in the game.

    Attributes:
        name (str): The name of the action.
        ticker (int): The ticker of the action.
        price (float): The price of the action.
        shares (int): The number of shares of the action.
        level (int): The level of the action (1, 2, 3, 4).
        The higher the level, bigger the class volatility.


    """

    def __init__(self, name: str, ticker: int, sector: float, price: float, shares: int, level: int):
        self.name = name
        self.ticker = ticker
        self.sector = sector  # randomly generated traits
        self.price = price
        self.shares = shares
        self.level = level
        self.base_price = price

    def update_price(self, delta_minutes):
        """
        This function updates the price of the action based on the level of the action.
        The higher the level, the bigger the class volatility.
        """

        for _ in range(delta_minutes):
            price_corrector = (self.base_price - self.price) / self.base_price
            self.price *= 1 + random.normalvariate(0, 0.005 * self.level)
            self.price *= 1 + 0.01 * price_corrector

    def update_level(self):
        """
        This function updates the level of the action randomly.
        """

        random_int = random.randint(1, 2)

        if random_int == 1:
            if self.level != 4:
                self.level += 1
        else:
            if self.level != 1:
                self.level -= 1
