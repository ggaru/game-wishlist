import pandas as pd
import json
import os
from arquivo import Initialize
from games import Games

arq = Initialize()
games = Games()

def add_game():
    game = input("What is the name of the game?")
    plataform= input("plataform:")
    beaten = input("already beat it? yes or no?")
    if beaten.lower() == "yes": beaten = "V"
    else: beaten = "X"
   
    gameList = arq.leArquivo()

    gameList[game] = {
            "Plataforma": plataform,
            "Finalizado": beaten,
        }
    
    arq.salvaArquivo(gameList)
    
def delete_game(gameList):
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

    arq.salvaArquivo(gameList)                                 

def edit_games(gameList):
    choose = int(input("\n1 - Add a new game\n" \
            "2 - Edit a existing one\n" \
            "3 - Delete\n" \
            "4 - Go back\n"))

    while choose != 4:
        if choose == 1:
            add_game()

        elif choose == 2:
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

            arq.salvaArquivo(gameList)
            
        elif choose == 3:
            delete_game(gameList)

        choose = int(input("\n1 - Add a new game\n" \
            "2 - Edit a existing one\n" \
            "3 - Delete\n" \
            "4 - Go back\n"))
    
def menu():
    print("\n\nWELCOME. \n ----------------- MENU -------------------")
    choose = int(input("1 - List games\n2 - Edit games\n3 - Exit\n"))
    return choose

while True:
    match  menu():
        case 1:
            games.list_games()
        case 2:
            edit_games()
        case 3:
            break
