import random


class Action :
    """
    This class represents an action in the game.

    Attributes:
        name (str): The name of the action.
        ID (int): The ID of the action.
        price (float): The price of the action.
        shares (int): The number of shares of the action.
        level (int): The level of the action (1,2,3,4), the higher the level, the more chance to increase the price.
    
        
    """

    def __init__(self, name,ID, price,shares ,level):
        self.name = name
        self.ID = ID
        self.price = price
        self.shares = shares
        self.level = level #the level of the action (1,2,3,4), the higher the level, the more chance to increase the price
    
    def update_price(self):
        """
        This function updates the price of the action based on the level of the action.
        The higher the level, the more chance to increase the price.
        """
        

        random_int = random.randint(1,4)
        
        if random_int >= self.level:
            self.price = self.price * (random.int(1,999) / 1000)
        else:
            self.price = self.price * (random.randint(1000,1500) / 1000)

    def update_level(self):
        """
        This function updates the level of the action randomly.
        """

        random_int = random.randint(1,2)

        if random_int == 1:
            self.level = (self.level + 1) % 4
        else:
            self.level = (self.level - 1) % 4
        
    




    