class Player:
    player_count = 0
    def __init__(self, name: str):
        Player.player_count += 1
        self.player_number = Player.player_count
        self.name = name
        self.words = []

    def add_word(self, word):
        self.words.append(word)

    def return_list(self):
        return self.words


class GameCore:
    sentence = ""
    forbidden_chars = """`~!@#$%^&*()_-+={[}]|:;'"<,>?/"""
    def __init__(self, players: dict, stop_sign="."):
        self.players = players
        self.stop_sign = stop_sign

    def enter_word(self, player_name: str, word):
        if word == ".":
            GameCore.sentence += word
            return False
        self.players[player_name].add_word(word)
        GameCore.sentence += f" {word}"
        return True



