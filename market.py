import random
from action import Action
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
        self.time_manager = TimeManager()

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
            action_obj = Action(action_price, action_shares, action_level)

            # Store the action object and its shares in the dictionary
            actions[action_obj.ticker] = [action_obj, action_shares]

        return actions

    def update_actions(self):
        for action in self.actions.values():
            action[0].update_price()
            action[0].update_level()

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
