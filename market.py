from action import Action
import random



class Market:
    """
    A class representing a stock market with a collection of actions (stocks).

    Attributes:
        actions (dict): A dictionary containing action objects and their available shares.
    
    """

    def __init__(self,size):
        self.actions = self.generate_actions(size)

    
    def generate_actions(self, size):
        """
        Generate a dictionary of actions with random prices and shares.
        Args:
            size (int): The number of actions to generate.
        Returns:
            dict: A dictionary with action IDs as keys and a list containing the action object and its shares as values.
        """

        actions = {} # Dictionary to store actions and their ammount in the market Example: {action_name: [action_obj, amount]}

        for i in range(size):
            action_name = f"Action {i}"
            action_ID = i
            action_price = random.uniform(1, 100)
            action_shares = random.randint(50000, 10000000)
            action_level = random.randint(1, 4)
            action_obj = Action(action_name,action_ID ,action_price,action_shares, action_level)
            actions[action_ID] = [action_obj, action_shares] # Store the action object and its shares in the dictionary
            
        return actions



    def update_actions(self):
        for action in self.actions.values():
            action[0].update_price()
    
    def display(self):
        """
        Display the actions in the market.  
        """

        print("Actions in Market:")
        print("=====================================")
        print("ID |Name | Price | Level | Total shares | Available shares")
        print("=====================================")
        for action in self.actions.values():
            action_obj = action[0]
            shares = action[1]
            print(f"#000{action_obj.ID} | {action_obj.name} | {action_obj.price:.2f}R$ | {action_obj.level} | {action_obj.shares} | {shares}")

    
    def market_buy(self,action_id, shares):
        """
        Represents the market buying an action.
        Args:
            action_id (int): The ID of the action to buy.
            shares (int): The number of shares to buy.
        Raises:
                ValueError: If the market does not have enough shares to sell.
        
        """
        if action_id in self.actions:
            if shares >= self.actions[action_id][0].shares:
                raise ValueError("Market will have more shares than the action has to sell")
            else:
                self.actions[action_id][1] += shares
        else:
            raise ValueError("Action not found in the market")

        
    def market_sell(self,action_id, shares):
        """
        Represents the market selling an action.
        Args:
            action_id (int): The ID of the action to sell.
            shares (int): The number of shares to sell.
        Raises:
            ValueError: If the market does not have enough shares to sell.
        Returns:
            Action: the action that will be acquired by the user
        """
        if action_id in self.actions:
            if shares >= self.actions[action_id][1]:
                raise ValueError("Market dont have enough shares to sell")
            else:
                self.actions[action_id][1] -= shares
        else:
            raise ValueError("Action not found in the market")
        
        return self.actions[action_id][0]

        
    
