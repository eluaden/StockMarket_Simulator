import os  # temporario enquanto nao temos a interface de terminal
from datetime import time
from market import Market
from time_manager import TimeManager
from user import User
import display_utils as dp
from menu_controler import MenuPage
from news_manager import NewsManager


class GameManager:
    """
    GameManager class to manage the game state and interactions.
    it manages the game loop, player input, and game state transitions.
    it also handles victory and defeat conditions.
    """

    def __init__(self):
        print("Welcome to the stock market simulation!")

        self.game_state = "running"  # Possible states: running, victory, defeat
        self.difficulty = self.choose_difficulty()

        # Adjust market size based on difficulty
        self.market = Market(20 - (self.difficulty * 5))

        username = input("Enter your name: ")

        # Adjust budget based on difficulty
        self.user = User(username, 1000 - (self.difficulty * 200))

        self.time_manager = TimeManager(
            time(hour=10, minute=0), time(hour=17, minute=0))

        self.news_manager = NewsManager()

    def choose_difficulty(self):
        """
        Choose the difficulty level of the game.
        """
        print("Choose difficulty level (1-3):")
        while True:
            try:
                difficulty = int(input())
                if 1 <= difficulty <= 3:
                    return difficulty
                print("Invalid choice. Please choose a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")

    def start_game(self):
        """
        Start the game loop.
        """

        while self.game_state == "running":
            # Clear the console for better readability
            os.system('cls' if os.name == 'nt' else 'clear')
            news = self.news_manager.update_news()

            self.display_menu()

            self.handle_action()

            # Update the game state
            self.market.daily_news_impact(news)

            # check the game state
            self.check_game_state()


    def display_menu(self):
        """
        Display current menu
        """
        print("THE ULTIMATE STOCK MARKET SIMULATOR")

        dp.display_table(self.market.get_market(), "market")
        print(f"\n{dp.separator}\n")
        dp.display_table(self.user.wallet, "wallet")
        self.news_manager.display_news()
        print(f"\n{dp.separator}")
        print("""Press m to advance one minute, h to advance one hour, d to advance one day,
      b to buy, s to sell, q to quit\n\n""")

    def handle_action(self):
        """
        Handle user input actions.
        """
        action_choice = input("Enter your action: ").strip().lower()

        if action_choice == 'b':
            # Receive the action ID and amount from the user
            action_id = input("Enter the action ID you want to buy: ")
            amount = int(input("Enter the amount you want to buy: "))
            try:
                action = self.market.market_sell(action_id, amount)
                self.user.buy(action, amount)
                self.market.update_actions(1)
            except Exception as e:
                print(f"Error: {e}")

        elif action_choice == 's':
            # Receive the action ID and amount from the user
            action_id = input("Enter the action ID you want to sell: ")
            amount = int(input("Enter the amount you want to sell: "))
            try:
                self.user.sell(action_id, amount)
                self.market.market_buy(action_id, amount)
                self.market.update_actions(1)
            except Exception as e:
                print(f"Error: {e}")

        elif action_choice == 'm':
            # Advance the time by one minute
            self.market.time_manager.advance_minute()
            self.market.update_actions(1)

        elif action_choice == 'h':
            # Advance the time by one hour
            self.market.time_manager.advance_hour()
            self.market.update_actions(60)

        elif action_choice == 'd':
            # Advance the time by one day
            self.market.time_manager.advance_day()
            self.market.update_actions(60 * 12)

        elif action_choice == 'q':
            self.game_state = "quit"
            print("Thanks for playing!")

    # os prints abaixo devem ser feitos pelo terminal_interface, aqui é provisório apenas

    def check_game_state(self):
        """
        Check the game state for victory or defeat conditions.
        this should be an optional function to be called at the end of each turn.
        """
        pass



    def update_game(self):
        """
        The functions that update the game infos.
        """
        pass
        
