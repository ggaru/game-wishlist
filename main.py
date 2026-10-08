import pandas as pd
import json
import os

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
    beaten = input("already beat it? yes or no?")
    if beaten.lower() == "yes": beaten = "V"
    else: beaten = "X"
   
    with open("games.json") as json_file:
        json_decoded = json.load(json_file)

    json_decoded[game] = {
            "Plataforma": plataform,
            "Finalizado": beaten,
        }
    
    with open("games.json", 'w') as json_file:
        json.dump(json_decoded, json_file, indent=4, ensure_ascii=False)
        
    print("Game added")
    
def delete_game(gameList):
    print("in deletegame func")
    game = input("\nWhat game do you wish to delete?\n")
    games_found = []
    n = 1
    for i in gameList:
         if game in i.lower():
              print(f"{n} - {i}")
              n += 1
              games_found.append(i)
    game_delete = games_found[int(input(f"i've found {n-1} games matchable, wich one u wanna delete?"))-1]
    
    for j in gameList:
        if j == game_delete:
            print(gameList[j])
            gameList.pop(j)
            break


    # Output the updated file with pretty JSON                                      
    open("games.json", "w").write(
    json.dumps(gameList,indent=4)
) 
    


def list_games():
    with open("games.json", "r") as gameList:
                gameList = json.load(gameList)
    
    choose = input("1 - List all games \n2 - Search for a game/saga \n3 - List by plataform \n4 - List by Situation \n5 - Go back\n")

    if choose == "1":
        print("Your wishlist games are:")
        n = 0
        for i in gameList:
            n +=1
            beaten = gameList[i]["Finalizado"]
            print(f"{i} - {beaten}")
        print(f"You have {n} games.")
        list_games()

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
        list_games()

    elif choose == "3":
        n=0
        consoles = []
        for i in gameList:
            console = gameList[i]["Plataforma"].lower()
            if console not in consoles:
                consoles.append(console)

        for x in range(len(consoles)):
            print(f"{x+1} - {consoles[x]}")
        plataform = int(input("what plataform are u looking for? above are the available's"))

        for z in gameList:
            console = gameList[z]["Plataforma"].lower()
            if console == consoles[plataform-1]:
                n+= 1
                print(f"{z} - {gameList[z]["Finalizado"]}")
        print(f"we've found {n} games for the {consoles[plataform-1]}")
        list_games()

    elif choose == "4":
        print("oi?")
        situation = int(input("1 - Finished's\n2 - Unfinished's"))
        for i in gameList:
            game = gameList[i]["Finalizado"] == "Sim"
            if situation == 1 and game == True:
                print(i)
            elif situation == 2 and game == False:
                print(i)
    elif choose == "5":    
        menu()
    
def edit_games(gameList):
    choose = input("\n1 - Add a new game\n" \
    "2 - Edit a existing one\n" \
    "3 - Delete\n" \
    "4 - Go back\n")

    if choose == "1":
        add_game()
    elif choose == "2":
    
        game = input("Which game are u looking to edit?\n")

        games_found = []
        n = 1
        for i in gameList:
            if game in i.lower():
                    print(f"{n} - {i}")
                    n += 1
                    games_found.append(i)
        game_edited = games_found[int(input(f"i've found {n-1} games matchable, wich one u wanna edit?\n"))-1]
        print(f"\nHere are the info's about that game:\nnome: {game_edited}\nplataforma: {gameList[game_edited]["Plataforma"]}\nsituação: {gameList[game_edited]["Finalizado"]}")
        edit = input("What are u going to edit?")
        if edit == "nome":
            name = input("Write the new name for that game: ")
            gameList[name] = {
                "Plataforma": gameList[game_edited]["Plataforma"],
                "Finalizado": gameList[game_edited]["Finalizado"]
            }
            gameList.pop(game_edited)
            
        elif edit == "plataforma":
            plataform = input("Write the new plataform for that game: ")
            gameList[game_edited]["Plataforma"] = plataform
        elif edit == "situação":
            situation = input("Write the new situation for that game: ")
            gameList[game_edited]["Plataforma"] = situation

        with open("games.json", 'w') as json_file:
            json.dump(gameList, json_file, indent=4, ensure_ascii=False)
        
    elif choose == "3":
        delete_game(gameList)

initialize()

def menu():
    print("\n\nWELCOME. \n ----------------- MENU -------------------")
    choose = input("1 - List games\n2 - Edit games\n3 - Exit\n")
    return choose

while True:
    with open("games.json", "r") as gameList:
        gameList = json.load(gameList)
    match  menu():
        case "1":
            list_games()
        case "2":
            edit_games(gameList)
        case "3":
            break
            


    