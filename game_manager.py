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
        username, self.difficulty = self.start_infos()

        # Adjust market size based on difficulty
        self.market = Market(20 - (self.difficulty * 5))

        # Adjust budget based on difficulty
        self.user = User(username, 1000 - (self.difficulty * 200))

        self.time_manager = TimeManager(
            time(hour=10, minute=0), time(hour=17, minute=0))

        self.news_manager = NewsManager()
        self.news = self.news_manager.update_news()


    def start_infos(self):
        """
        Choose the difficulty level of the game.
        """
        infos = []

        infos.append(input("Enter your username: "))

        while True:
            try:
                difficulty = int(input("Choose a number between 1 and 3: "))
                if 1 <= difficulty <= 3:
                    infos.append(difficulty)
                    break
                print("Invalid choice. Please choose a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")

        return infos

    def start_game(self):
        """
        Start the game loop.
        """

        while self.game_state == "running":
            
            self.display_menu()

            self.handle_action()


            # check the game state
            self.check_game_state()

            if not self.time_manager.is_market_open():
                self.day_update()
                self.time_manager.advance_day()



    def display_menu(self):
        """
        Display current menu
        """

        dp.clear_screen()
        print("THE ULTIMATE STOCK MARKET SIMULATOR")
        
        dp.display_table(self.market.get_market(), "market")
        print(f"\n{dp.separator}\n")
        dp.display_table(self.user.wallet, "wallet")
        self.news_manager.display_news()
        print(f"\n{dp.separator}")
        print("""Press m to advance one minute, h to advance one hour, d to advance onme day,
      b to buy, s to sell, q to quit\n\n""")
        
        #print provisiorio de data
        print(f"Current time: {self.time_manager.get_formatted_time()}")


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
            self.time_manager.advance_minute()
            self.market.update_actions(1)

        elif action_choice == 'h':
            # Advance the time by one hour
            self.time_manager.advance_hour()
            self.market.update_actions(60)

        elif action_choice == 'd':
            # Advance the time by one day
            self.day_update()
            self.time_manager.advance_day()
            
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

        
    def day_update(self):
        """
        the functions that update the game at the end of each day.
        """
        
        self.market.update_actions(60 * 12)
        self.market.daily_news_impact(self.news) # the news impact one day later
        self.news = self.news_manager.update_news()

        #new day animation
        dp.new_day_animation(self.time_manager.open_time, self.time_manager.time)


    

    
        
