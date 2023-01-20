import random 

choices = ["rock","paper", "scissors"]

computer = random.choice(choices)
player = None
 
while True:
  choices = ["rock", "paper", "scissors"]
  while player not in choices: 
    player = input("rock, paper, scissors?: ").lower() 
  if player == computer:
    print("computer: ", computer)
    print("player: ", player)
    print("Tie!")
  elif player == "rock":
    if computer == "paper":
      print("computer: ", computer)
      print("player: ", player)
      print("You win!")
  elif player == "scissors":
    print("computer: ", computer)
    print("player: ", player)
    print("You lose!")
    if computer == "paper":
        print("computer: ", computer)
        print("player: ", player)
        print("You win!")

 
  
  play_again = input("Play again? (yes/no): ").lower()

  if play_again != "yes":
    break 
print("Bye!")
if play_again == "yes":
    
    
          
    