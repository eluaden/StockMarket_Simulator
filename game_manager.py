from market import Market
from user import User
import os #temporario enquanto nao temos a interface de terminal


class GameManager:
    """
    GameManager class to manage the game state and interactions.
    it manages the game loop, player input, and game state transitions.
    it also handles victory and defeat conditions.
    """

    def __init__(self):
        self.game_state = "running"  # Possible states: running, victory, defeat


    def choose_difficulty(self):
        """
        Choose the difficulty level of the game.
        """
        print("Choose difficulty level (1-3):")
        while True:
            try:
                self.difficulty = int(input())
                if 1 <= self.difficulty <= 3:
                    break
                else:
                    print("Invalid choice. Please choose a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")  

    def initialize_game(self):
        """
        Initialize the game state.
        """
        print("Welcome to the stock market simulation!")
        username = input("Enter your name: ")
        self.choose_difficulty()


        self.market = Market(20 - (self.difficulty * 5))  # Adjust market size based on difficulty
        self.user = User(username, 1000 - (self.difficulty * 200))  # Adjust budget based on difficulty
        self.game_state = "running"


    def start_game(self):
        """
        Start the game loop.
        """ 


        while self.game_state == "running":
            os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console for better readability
            self.display_menu()
            action_choice = input("Enter your action: ").strip().lower()
            self.handle_action(action_choice)



    #essa função deve ser desempenhada pelo terminal_interface, aqui é provisória apenas(por isso feia)
    def display_menu(self):
        """
        Display the game menu.
        """
        print("THE ULTIMATE STOCK MARKET SIMULATOR")
        print("=====================================")
        self.market.display()
        print("\n=====================================\n")
        self.user.display_wallet()
        print("\n=====================================")
        print("Press b to buy, s to sell, q to quit\n\n")

    
    def handle_action(self, action_choice):
        """
        Handle user input actions.
        """
        if action_choice == 'b':
            # Receive the action ID and amount from the user
            action_id = int(input("Enter the action ID you want to buy: "))
            amount = int(input("Enter the amount you want to buy: "))
            try:
                action = self.market.market_sell(action_id, amount)
                self.user.buy(action, amount)
            except Exception as e:
                print(f"Error: {e}")

        elif action_choice == 's':
            # Receive the action ID and amount from the user
            action_id = int(input("Enter the action ID you want to sell: "))
            amount = int(input("Enter the amount you want to sell: "))
            try:
                self.user.sell(action_id, amount)
                self.market.market_buy(action_id, amount)
            except Exception as e:
                print(f"Error: {e}")

        elif action_choice == 'q':
            self.game_state = "quit"
            print("Thanks for playing!")

    
    
    
    