import pandas as pd
import json

def initialize():
    try:
        print("Opening data...")
        with open("games.json", "r") as games:
            print("Sucess")
    
    except FileNotFoundError:
        print("File do not Exist. Creating a new database...")
        df = pd.read_csv("lista_jogos.csv")
        resultado = df.set_index("Nome")[["Plataforma", "Finalizado"]].to_dict(orient="index")
        with open("games.json", "a", encoding="utf-8") as file:
            json.dump(resultado, file, indent=2, ensure_ascii=False)
        print("Database created.")
        initialize()

def add_game():
    game = input("What is the name of the game?")
    plataform= input("plataform:")
    beaten = input("already beat it? yer or no?")
    if beaten == "yes": beaten = "Sim"
    else: beaten = "Não"
   
    with open("games.json") as json_file:
        json_decoded = json.load(json_file)

    json_decoded[game] = {
            "Plataforma": plataform,
            "Finalizado": beaten,
        }
    
    with open("games.json", 'w') as json_file:
        json.dump(json_decoded, json_file, indent=4, ensure_ascii=False)
        3
    print("Game added")
    

def list_games():
    with open("games.json", "r") as gameList:
                gameList = json.load(gameList)
    
    choose = input("1 - List all games \n2 - Search for a game/saga \n3 - Go back\n")

    if choose == "1":
        print("Your wishlist games are:")
        n = 0
        for i in gameList:
            n +=1
            print(i)
        print(f"You have {n} games.")
    elif choose == "2":
        games = []
        name = input("What game/saga are u looking for?\n")
        for i in gameList:
            if name.lower() in i.lower():
                games.append(i)
        if games == []:
            print("You have'nt yet add that one.")
        else:
            print(f"We've found {len(games)} games that are matchable. Here are they:")
            for x in games:
                print(x)
    else:
        menu()
    list_games()

def edit_games():
    choose = input("\n1 - Add a new game\n" \
    "2 - Edit a existing one\n" \
    "3 - Delete\n" \
    "4 - Go back\n")

    if choose == "1":
        add_game()
        


initialize()
add_game()


def menu():
    print("\n\nWELCOME. \n ----------------- MENU -------------------")
    choose = input("1 - List games\n2 - Edit games\n3 - Exit\n")
    return choose

while True:
    match  menu():
        case "1":
            list_games()
        case "2":
            edit_games()
        case "3":
            break 


    