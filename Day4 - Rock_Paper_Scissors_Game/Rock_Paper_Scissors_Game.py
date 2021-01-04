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

import random

#Place images into a list
options = [rock, paper, scissors]

#Code for image output based on user's choice
user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for Scissors.\n"))

#Code to debug code thereby invalidating out of range values
if user_choice >= 3 or user_choice <0:
  print("Invalid option. You lose")
else:
  print(options[user_choice])

#Code for the computer to randomly select an options and output an image based on the "options" list
  comp_choice = random.randint(0,2)
  print(f"Computer chose: {options[comp_choice]}")

#Code for conditional statements
  if user_choice == 0 and comp_choice == 2:
    print("You win!")
  elif user_choice == 2 and comp_choice == 0:
    print("You lose!")
  elif user_choice > comp_choice:
    print("You win!")
  elif comp_choice > user_choice:
    print("You lose!")
  elif user_choice == comp_choice:
    print("It's a draw")
  else:
    print("Invalid option. You lose")

