import action
import user
import datetime
from time import sleep
import os
separator = str()

def display_table(dict: dict , type: str, alignment = "left") -> None:
    """
    Displays a table in the terminal.
    Args:
        dict (dict): The dictionary to display.
        type (str): The type of the table. Can be "market" or "wallet".
        alignment (str): The alignment of the text. Can be "left" or "right".
    Raises:
        ValueError: If the type is not "market" or "wallet".
        ValueError: If the alignment is not "left" or "right".
    """

    R_MARGIN = 3
    L_MARGIN = 1

    if type == "market":
        title = "Market"
        matriz = market_to_matriz(dict)
    elif type == "wallet":
        title = "Wallet"
        matriz = wallet_to_matriz(dict)
    else:
        raise ValueError("Invalid type. Use 'market' or 'wallet'.")
    
    col_width = [max(len(str(item))for item in col)for col in zip(*matriz)] #This returns a list that contains the max lenth of a column
    carac_total = (sum(col_width) + len(matriz[0])*(L_MARGIN+R_MARGIN) + len(matriz[0])+1)
    separator = "="*carac_total

    print("="*carac_total)
    print(" "*((carac_total-len(title))//2) + title + " "*((carac_total-len(title))//2))
    print("="*carac_total)

    if alignment == "left":
        for i, line in enumerate(matriz):
            for i, word in enumerate(line):
                print("|" + " "*L_MARGIN + str(word) + " "*(col_width[i] - len(str(word)) + R_MARGIN), end = "")
            print("|")

            if i == 0: print("="*carac_total)
    
    elif alignment == "right":
        for i,line in enumerate(matriz):
            for i, word in enumerate(line):
                print("|" + " "*(col_width[i] - len(str(word)) + L_MARGIN) + str(word) + " "*R_MARGIN, end = "")
            print("|")
            
            if i == 0: print("="*carac_total) 
    
    else:
        raise ValueError("Invalid alignment. Use 'left' or 'right'.")
    
    print(separator)
    

def market_to_matriz(dict):
    """
    Converts a dictionary to a matrix for display purposes.
    """
    matriz = []
    matriz.append(["Ticker", "Name", "Price", "Level", "Total Shares", "Avaiable Shares"])
    for key, value in dict.items():
        matriz.append(list(value[0]) + [value[1]])
    return matriz

def wallet_to_matriz(dict):
    """
    Converts a dictionary to a matrix for display purposes.
    """
    matriz = []
    matriz.append(["ID", "Name", "Price", "Level", "Toral Shares", "Amount"])
    for key, value in dict.items():
        matriz.append(list(value[0]) + [value[1]])
    return matriz

def clear_screen(): #melhorar essa função, por que ela pisca a tela
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def new_day_animation(opening: datetime, time: datetime):
    """
    Displays the time passing fast for the new day.
    Args:
        opening (datetime): The opening time of the market.
        time (datetime): The time time of the market.
    """

    while True:
        clear_screen()
        print(" MARKET CLOSED")
        print(" the day is passing...")
        time += datetime.timedelta(minutes=1)
        print(f" {time.strftime("%d/%m/%Y, %H:%M")}")
        if time.time() == opening:
            break
        
        sleep(0.01)
    
    