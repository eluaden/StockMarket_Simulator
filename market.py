import random
import datetime
from action import Action
from market_sector import *
from name_generator import NameGenerator
from display_utils import header, separator
from time_manager import TimeManager



class Market:
    """
    A class representing a stock market with a collection of actions (stocks).

    Attributes:
        actions (dict): A dictionary containing action objects and their available shares.

    """

    def __init__(self, size):
        """
        Initialize the Market with a specified number of actions.
        Args:
            size (int): The number of actions to generate in the market.
        """
        self.actions = self.generate_actions(size)
        self.time_manager = TimeManager(
            datetime.time(10, 0), datetime.time(17, 0)
        )

    def generate_actions(self, size):
        """
        Generate a dictionary of actions with random prices and shares.
        Args:
            size (int): The number of actions to generate.
        Returns:
            dict: A dictionary with action tickers as keys and a list containing the action object and its shares as values.
        """

        # Dictionary to store actions and their ammount in the market Example: {action_name: [action_obj, amount]}
        actions = {}

        for _ in range(size):

            action_price = random.uniform(1, 100)
            action_shares = random.randint(50000, 10000000)
            action_level = random.randint(1, 4)
            action_sector = Sector()

            # generate a name without repeating it
            while True:
                action_name = NameGenerator.generate_name(
                    action_sector.major_sector)
                action_ticker = NameGenerator.action_ticker(action_name)
                if action_ticker not in actions:
                    break

            action_obj = Action(action_name, action_ticker, action_sector,
                                action_price, action_shares, action_level)

            # Store the action object and its shares in the dictionary
            actions[action_obj.ticker] = [action_obj, action_shares]

        return actions

    def update_actions(self, delta_minutes: int):
        for action in self.actions.values():
            action[0].update_price(delta_minutes)
            action[0].update_level()


    def get_market(self):
        return self.actions

    def display(self):
        """
        Display the actions in the market.  
        """

        print(f"Actions in Market: {self.time_manager.get_formatted_time()}")
        print(separator)
        print(header)
        print(separator)
        for action in self.actions.values():
            action_obj = action[0]
            shares = action[1]
            print(f"{f'#{action_obj.ticker}':<6} | {action_obj.name:<10} | " +
                  f"{f'R$ {action_obj.price:.2f}':<10} | {action_obj.level:<10} | " +
                  f"{action_obj.shares:<13} | {shares:<17}")


    def market_buy(self, action_ticker, shares):
        """
        Represents the market buying an action.
        Args:
            action_ticker (int): The ticker of the action to buy.
            shares (int): The number of shares to buy.
        Raises:
                ValueError: If the market does not have enough shares to sell.

        """
        if action_ticker in self.actions.values():
            if shares >= self.actions[action_ticker][0].shares:
                raise ValueError(
                    "Market will have more shares than the action has to sell")
            self.actions[action_ticker][1] += shares
        else:
            raise ValueError("Action not found in the market")

    def market_sell(self, action_ticker, shares):
        """
        Represents the market selling an action.
        Args:
            action_ticker (int): The ticker of the action to sell.
            shares (int): The number of shares to sell.
        Raises:
            ValueError: If the market does not have enough shares to sell.
        Returns:
            Action: the action that will be acquired by the user
        """
        if action_ticker in self.actions:
            if shares >= self.actions[action_ticker][1]:
                raise ValueError("Market doesn't have enough shares to sell")
            self.actions[action_ticker][1] -= shares
        else:
            raise ValueError("Action not found in the market")

        return self.actions[action_ticker][0]
    
    def daily_news_impact(self, news_sector):
        """
        Apply the daily news impact on the market.
        Args:
            news (str): The news that will impact the market.
        """
        
        major_sector = news_sector[0]
        minor_sectors = news_sector[1:]

        for action in self.actions.values():
            action_obj = action[0]
            if action_obj.sector.major_sector == major_sector[0]:
                if major_sector[1] == "up":
                    action_obj.price *= 1.1
                else:
                    action_obj.price *= 0.9

        for minor_sector in minor_sectors:
            for action in self.actions.values():
                action_obj = action[0]
                if action_obj.sector.minor_sector == minor_sector[0]:
                    if minor_sector[1] == "up":
                        action_obj.price *= 1.05
                    else:
                        action_obj.price *= 0.95      
