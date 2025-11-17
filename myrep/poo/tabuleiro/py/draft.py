class Player:
    def __init__(self, label:int):
        self.label = label
        self.position = 0
        self.livre = True

    def is_livre(self):
        return self.livre
    
    def get_label(self):
        return self.label
    
    def get_position(self):
        return self.position
    

    def set_position(self, position:int):
        self.position = position
    def set_livre(self, livre:bool):
        self.livre = livre


    def __str__(self):
        return f"player {self.label}"
    

class Tabuleiro:
    def __init__(self, num_players:int, board_size:int):
        self.__board_size = board_size
        self.__armadilhas:list[int] = []
        self.__players:list[Player] = [Player(i +1)for i in range(num_players)]
        self.__current:int = 0
        self.__over:bool= False
    def add_armadilha(self, position:int):
        self.__armadilhas.append(position)

    def __next_player(self):
        self.__current = (self.__current + 1) % len(self.__players)
    
    def rollDice(self, value:int):
        if self.__over:
            print("game is over")
            return
        player = self.__players[self.__current]

        if not player.is_livre():
            if value % 2 == 0:
                player.set_livre(True)
                print(f"player{player.get_label()} se libertou")
            else:
                print(f"player{player.get_label()} continua preso")
            self.__next_player()
            return
        

        new_position = player.get_position() + value
        if new_position > self.__board_size:
            player.set_position(self.__board_size)
            print(f"player{player.get_label()} ganhou")
            self.__over = True
            return
        
        player.set_position(new_position)
        print(f"player{player.get_label()} andou para {player.get_position()}")

        if new_position in self.__armadilhas:
            player.set_livre(False)
            print(f"player{player.get_label()} caiu em uma armadilha")

        self.__next_player()

    def __str__(self):
        lines = []
        size = self.__board_size + 1

        for player in self.__players:
            row = ["." for _ in range(size)]
            row[player.get_position()] = str(player.get_label())
            lines.append(f"player{player.get_label()}: {''.join(row)}")
        
        armadilhas_row = ["." for _ in range(size)]

        for trap in self.__armadilhas:
            armadilhas_row[trap] = "x"
        lines.append(f"traps__: {''.join(armadilhas_row)}")
    
        return "\n".join(lines)
    
def main():
    tabuleiro = None
    while True:
        line = input()
        args = line.split(" ")
        print("$" + line)
        cmd = args[0]
        if cmd == "end":
            break
        elif cmd == "init":
            tabuleiro = Tabuleiro(int(args[1]), int(args[2]))
        elif cmd == "addTrap":
            tabuleiro.add_armadilha(int(args[1]))
        elif cmd == "roll":
            tabuleiro.rollDice(int(args[1]))
        elif cmd == "show":
            print(tabuleiro)
        else:
            print("comando invalido")
main()