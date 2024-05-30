import math

class Game:
    # def __init__(self, player1: Player, player2: Player) -> None:
    def __init__(self, player1: str, player2: str) -> None:
        self.players = [player1, player2]
        self.morpion = self.reset_morpion()
        self.turn = 0
    
    def display_morpion(self):
        print(self.morpion[2])
        print(self.morpion[1])
        print(self.morpion[0])

    def switch_turn(self):
        self.turn = 0 if self.turn == 1 else 1

    def __numpad_2_raw_and_line(self, numpad: int):
        numpad -= 1
        raw = math.floor(numpad/3)
        line = math.floor(numpad%3)
        return raw, line

    def is_victory(self) -> bool:
        n = len(self.morpion)

        # Check rows and columns
        for i in range(n):
            if all(self.morpion[i][j] == self.morpion[i][0] and self.morpion[i][0] != "" for j in range(n)):
                return True
            if all(self.morpion[j][i] == self.morpion[0][i] and self.morpion[0][i] != "" for j in range(n)):
                return True

        # Check diagonals
        if all(self.morpion[i][i] == self.morpion[0][0] and self.morpion[0][0] != "" for i in range(n)):
            return True
        if all(self.morpion[i][n-1-i] == self.morpion[0][n-1] and self.morpion[0][n-1] != "" for i in range(n)):
            return True
        return False

    def set_action(self, numpad: int):
        raw, line = self.__numpad_2_raw_and_line(numpad)
        if self.morpion[raw][line] == "":
            self.morpion[raw][line] = self.turn+1
            return True
        return False

    def reset_morpion(self):
        self.morpion = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]

    # def send_update_players(self, sio):
    def send_update_players(self):
        # sio.emit('game', {'morpion': str(self.morpion), 'turn': str(self.turn)})
        # print(game.morpion)
        self.display_morpion()
    

# test de logique - à implémenter en event
game = Game('joueur1', 'joueur2')
game.display_morpion()


while True:
    numpad = int(input(game.players[game.turn] + " ?"))
    game.set_action(numpad)
    game.send_update_players()
    if game.is_victory():
        print("Victoire de: ", game.players[game.turn])
        # changer statue en ENDGAME
        break
    game.switch_turn()
    