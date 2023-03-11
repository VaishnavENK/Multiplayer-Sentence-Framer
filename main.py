from classes import *
from util import has_forbidden_chars

print("Sentence Framer v1\n")

player_dict = {}
print("Enter the names of the player; enter '/' to exit\n")

# Player registration loop
while True:
    player_name = input("Enter player name: ").strip().capitalize()
    if player_name == "":
        continue
    if player_name == "/":
        break
    player_dict[player_name] = Player(player_name)
    print(f"{player_name} added")

if len(player_dict) <= 1:
    print("Insufficient players")
    quit()

# Main loop
game = GameCore(player_dict)
play = True
print("\nEach player shall enter a single word; enter '.' to stop the sentence\n")
while play:
    for player in game.players:
        word = input(f"{player}: ").strip()
        if " " in word:
            word, _ = word.split(" ")
        if has_forbidden_chars(game.forbidden_chars, word):
            print("Forbidden character(s) detected, word entry ignored...")
            continue
        if not game.enter_word(player, word):
            print("Sentence framed.\n")
            play = False
            break

print("Sentence: ")
print(game.sentence.strip())
