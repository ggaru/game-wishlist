from arquivo import *

class Games(Initialize):

    def __init__(self):
        super().__init__()

        self.gameList = self.leArquivo()

    def list_games(self):
        """função que retorna toda a lista de jogos a depender da escolha"""
        choose = int(input("1 - List all games \n2 - Search for a game/saga \n3 - List by plataform"
                        "\n4 - List by Situation \n5 - Go back\n"))

        while choose != 5:
            match choose: 
                case 1:
                    print("\nYour wishlist games are:")
                    self.percorreGames(self.gameList, operation = "imprime", arg1 = "games")

                case 2:
                    name = input("What game/saga are u looking for?\n")
                    games = self.percorreGames(self.gameList, operation = "valida", arg1=name)
                    if games == []:
                        print("You have'nt yet add that one.")
                    else:
                        self.percorreGames(games, operation="imprime", arg1="games")
                      
                case 3:
                    games = self.percorreGames(self.gameList, operation="percorre")
                    self.percorreGames(games, operation="imprime",arg1="consoles")
                    plataform = int(input("what plataform are u looking for? above are the available's"))
                    self.percorreGames(self.gameList, operation="imprime",arg1=plataform, arg2 = games)
                    
                case 4:                        
                    situation = int(input("1 - Finished's\n2 - Unfinished's"))
                    for i in self.gameList:
                        game = self.gameList[i]["Finalizado"] == "Sim"
                        if situation == 1 and game == True:
                            print(i)
                        elif situation == 2 and game == False:
                            print(i)

            choose = int(input("1 - List all games \n2 - Search for a game/saga"
                "\n3 - List by plataform \n4 - List by Situation \n5 - Go back\n"))

    def percorreGames(self, item, operation, arg1="", arg2 = ""):
        n = 0
        controlArray = []

        if operation == "imprime":
            for jogo in item:
                if arg1 == "games":
                    situacao = self.gameList[jogo]["Finalizado"]
                    print(f"{jogo} - {situacao}")
                    n +=1
                    x = arg1

                elif arg1 == "consoles":
                    n +=1
                    print(f"{n} - {jogo}")
                    x = arg1

                elif arg1 >= 0:
                    console = self.gameList[jogo]["Plataforma"].lower()
                    if console == arg2[arg1-1]:
                        print(f"{jogo} - {self.gameList[jogo]["Finalizado"]}")
                        n +=1
                    x = arg2[arg1-1] + "games"
                                
            print(f"we've found {n} {x}")

        elif operation == "valida":
            for i in self.gameList:
                if arg1.lower() in i.lower():
                    controlArray.append(i)
            return controlArray

        elif operation == "percorre":
            for i in self.gameList:
                console = self.gameList[i]["Plataforma"].lower()
                if console not in controlArray:
                    controlArray.append(console)
            return controlArray