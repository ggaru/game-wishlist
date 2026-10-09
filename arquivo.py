import json
import pandas as pd

class Initialize():
    def __init__(self):
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
            
    def salvaArquivo(self, data):
        with open("games.json", 'w') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)

    def leArquivo(self):
        with open("games.json", "r") as gameList:
                         gameList = json.load(gameList)
        return gameList