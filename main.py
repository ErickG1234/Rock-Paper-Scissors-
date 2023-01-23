from Abstractions import play_game
import random

play_again = input("Play again? (yes/no): ").lower()
choices = ["rock","paper", "scissors"]

computer = random.choice(choices)
user = input("rock, paper, scissors?: ").lower()

game = play_game(user, computer, choices, play_again)
print(game)