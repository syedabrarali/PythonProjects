import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
player_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_input = random.randint(0, 2)
if player_input >= 3 or player_input < 0:
  print("Invalid Input, please add a different input")
else:
  print("Player chose: \n ")
  print(game_images[player_input])

  print("computer chose:\n")
  print(game_images[computer_input])
  

  if player_input == 0 and computer_input == 2:
    print("You win")
  if computer_input == 0 and player_input == 2:
    print("Computer wins")
  elif computer_input > player_input:
    print("Computer wins")
  elif player_input > computer_input:
    print("You win")
  elif player_input == computer_input:
    print("Its a draw")
