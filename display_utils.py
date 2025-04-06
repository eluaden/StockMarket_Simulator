import action
import user
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