from market import Market
from action import Action
from user import User
import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


if __name__ == "__main__":
    # Initialize the market
    market = Market(10)
        
    print("Welcome to the stock market simulation!")


    # Initialize the user
    name = input("Enter your name: ")
    difficulty = int(input("Enter your difficulty level (1, 2, 3): "))
    
    budget = 1000 - (difficulty* 200)

    user = User(name, budget)
    print(f"Your budget is: {user.budget}")


    while(True):
        # Get user input for action
        

        print("\n\nPress b to buy, s to sell, d to display, q to quit, w to see your wallet")
        action_choice = input("Enter your action: ").strip().lower()
        clear_screen()

        if action_choice == 'b':
            #receive the action ID and amount from the user
            action_id = int(input("Enter the action ID you want to buy: "))
            amount = int(input("Enter the amount you want to buy: "))
            try:
                action = market.market_sell(action_id, amount)
                user.buy(action, amount)
            except Exception as e:
                print(f"Error: {e}")

        elif action_choice == 's':
            # receive the action ID and amount from the user
            action_id = int(input("Enter the action ID you want to sell: "))
            amount = int(input("Enter the amount you want to sell: "))
            try:
                user.sell(action_id, amount)
                market.market_buy(action_id, amount)
            except Exception as e:
                print(f"Error: {e}")

        elif action_choice == 'd':
            # Display action
            market.display()

        elif action_choice == 'w':
            #Display wallet
            user.display_wallet()

        elif action_choice == 'q':
            # Exit action
            print("Exiting the program.")
            break