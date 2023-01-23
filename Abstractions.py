import random 
play_again = input("Play again? (yes/no): ").lower()
choices = ["rock","paper", "scissors"]
computer = random.choice(choices)
user = input("rock, paper, scissors?: ").lower()
player = None

def play_game(user, computer, choices, play_again):
  while True:
    while user not in choices: 
      if user == computer:
        print("computer: ", computer)
        print("player: ", user)
        print("Tie!")
      elif user == "rock":
        if computer == "paper":
          print("computer: ", computer)
          print("player: ", user)
          print("You win!")
      elif user == "scissors":
        print("computer: ", computer)
        print("player: ", user)
        print("You lose!")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", user)
            print("You win!")
  while play_again != "yes":
    print("Bye!")
    break
               

